from typing import Callable

log_path = "sim_exp_0305_diff_num_clients_baselines.log"
with open(log_path, 'r') as f:
    lines = f.read().split('\n')

def get_every_exp_lines(lines: list):
    all_exp_lines = []
    one_exp_lines = []
    start_flag = False
    for line in lines:
        if "[EXPERIMENT #" in line and not start_flag:
            start_flag = True
            one_exp_lines = []
        if start_flag:
            one_exp_lines.append(line)
        if "[EXPERIMENT #" in line and "DONE" in line:
            start_flag = False
            exp_num = line.split("#")[-1].split("]")[0]
            print(f"Experiment {exp_num} end, with {len(one_exp_lines)} lines")
            all_exp_lines.append(one_exp_lines)
            one_exp_lines = []
    return all_exp_lines

def get_hyperparameter_from_one_exp_lines(one_exp_lines: list, target="num_clients", split_func: Callable = None):
    for line in one_exp_lines:
        if target in line:
            if split_func is not None:
                return split_func(line)
            return line

def get_all_hyperparamters_from_one_exp_lines(one_exp_lines: list):
    hyperparameters = {
        "server_rounds": None,
        "num_clients": None,
        "epochs": None,
        "learning_rate": None,
        "batch_size": None,
    }
    hyperparameters["server_rounds"] = get_hyperparameter_from_one_exp_lines(
        one_exp_lines=all_exp_lines[0],
        target="num-server-rounds",
        split_func=lambda x: x.split(" = ")[-1]
    )
    hyperparameters["num_clients"] = get_hyperparameter_from_one_exp_lines(
        one_exp_lines=all_exp_lines[0],
        target="options.num-supernodes", # be aware that there should be only 1 "options.num-supernodes" in the log, originally 2 for cpu and gpu sim mode
        split_func=lambda x: x.split(" = ")[-1]
    )
    hyperparameters["epochs"] = get_hyperparameter_from_one_exp_lines(
        one_exp_lines=all_exp_lines[0],
        target="local-epochs",
        split_func=lambda x: x.split(" = ")[-1]
    )
    hyperparameters["learning_rate"] = get_hyperparameter_from_one_exp_lines(
        one_exp_lines=all_exp_lines[0],
        target="learning-rate",
        split_func=lambda x: x.split(" = ")[-1]
    )
    hyperparameters["batch_size"] = get_hyperparameter_from_one_exp_lines(
        one_exp_lines=all_exp_lines[0],
        target="batch-size",
        split_func=lambda x: x.split(" = ")[-1]
    )
    return hyperparameters

def get_losses_from_one_exp_lines(one_exp_lines: list, server_rounds: int):
    losses = []
    summary_flag = False
    for line in one_exp_lines:
        if "[SUMMARY]" in line:
            summary_flag = True
        
        if summary_flag:
            if "round " in line:
                tmp_list = line.split(": ")
                loss = float(tmp_list[-1])
                losses.append(loss)

        if "History (metrics, distributed, evaluate):" in line:
            break
    assert str(len(losses)) == server_rounds
    return losses

def get_accuracies_from_one_exp_lines(one_exp_lines: list, server_rounds: int):
    accuracies = []
    summary_flag = False
    for line in one_exp_lines:

        if "History (metrics, distributed, evaluate):" in line:
            summary_flag = True
            continue
        
        if ")]}" in line and summary_flag:
            tmp_list = line.split(", ")
            acc = float(tmp_list[-1][:-3])
            accuracies.append(acc)
            break
        if summary_flag:
            tmp_list = line.split(", ")
            acc = float(tmp_list[-1][:-2])
            accuracies.append(acc)
    print(f"accuracies: {accuracies}")
    print(f"len(accuracies): {len(accuracies)}")
    assert str(len(accuracies)) == server_rounds
    return accuracies


import matplotlib.pyplot as plt

def plot_loss(experiments, y_label, title, fig_name="tmp.jpg", max_show_rnd=-1):
    """
    Plot loss curves for multiple experiments on the same graph.
    :param experiments: dict, keys are experiment names, values are lists of loss values
    """
    plt.figure(figsize=(10, 6))
    
    for exp_name, losses in experiments.items():
        plt.plot(range(1, len(losses[:max_show_rnd]) + 1), losses[:max_show_rnd], label=exp_name, alpha=0.7)
    
    plt.xlabel("Server Rounds")
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.savefig(fig_name)

all_exp_lines = get_every_exp_lines(lines)
print(len(all_exp_lines))
print("every exp lines: {}".format([len(one_exp_lines) for one_exp_lines in all_exp_lines]))
# print(all_exp_lines[0])
hyperparameters = get_all_hyperparamters_from_one_exp_lines(all_exp_lines[0])
a = get_accuracies_from_one_exp_lines(all_exp_lines[0], server_rounds=hyperparameters["server_rounds"])
print(a)
range(1, 13)
all_exp_losses = {f"exp_{i}": None for i in range(1, 13)}
all_exp_acc = {f"exp_{i}": None for i in range(1, 13)}
for i in range(1, 13):
    hyperparameters = get_all_hyperparamters_from_one_exp_lines(all_exp_lines[i-1])
    losses = get_losses_from_one_exp_lines(all_exp_lines[i-1], server_rounds=hyperparameters["server_rounds"])[:100]
    accuracies = get_accuracies_from_one_exp_lines(all_exp_lines[i-1], server_rounds=hyperparameters["server_rounds"])[:100]
    all_exp_losses[f"exp_{i}"] = losses
    all_exp_acc[f"exp_{i}"] = accuracies

# # lr 0.01
# tmp_losses = {}
# for i, (key, value) in enumerate(all_exp_losses.items()):
#     if i % 2 == 0:
#         tmp_losses[key] = value
# all_exp_losses = tmp_losses
# tmp_acc = {}
# for i, (key, value) in enumerate(all_exp_acc.items()):
#     if i % 2 == 0:
#         tmp_acc[key] = value
# all_exp_acc = tmp_acc

# # lr 0.001
tmp_losses = {}
for i, (key, value) in enumerate(all_exp_losses.items()):
    if i % 2 == 1:
        tmp_losses[key] = value
all_exp_losses = tmp_losses
tmp_acc = {}
for i, (key, value) in enumerate(all_exp_acc.items()):
    if i % 2 == 1:
        tmp_acc[key] = value
all_exp_acc = tmp_acc

# start plotting
max_show_rnd = 100
plot_loss(
    all_exp_losses,
    y_label="Loss",
    title="Loss Curves of Multiple Experiments",
    fig_name=f"Loss_for_exps_lre_3_{max_show_rnd}.jpg",
    max_show_rnd=max_show_rnd
)
plot_loss(
    all_exp_acc,
    y_label="Accuracy",
    title="Accuracy Curves of Multiple Experiments",
    fig_name=f"Accuracy_for_exps_lre_3_{max_show_rnd}.jpg",
    max_show_rnd=max_show_rnd
)
max_show_rnd = 20
plot_loss(
    all_exp_losses,
    y_label="Loss",
    title="Loss Curves of Multiple Experiments",
    fig_name=f"Loss_for_exps_lre_3_{max_show_rnd}.jpg",
    max_show_rnd=max_show_rnd
)
plot_loss(
    all_exp_acc,
    y_label="Accuracy",
    title="Accuracy Curves of Multiple Experiments",
    fig_name=f"Accuracy_for_exps_lre_3_{max_show_rnd}.jpg",
    max_show_rnd=max_show_rnd
)
max_show_rnd = 10
plot_loss(
    all_exp_losses,
    y_label="Loss",
    title="Loss Curves of Multiple Experiments",
    fig_name=f"Loss_for_exps_lre_3_{max_show_rnd}.jpg",
    max_show_rnd=max_show_rnd
)
plot_loss(
    all_exp_acc,
    y_label="Accuracy",
    title="Accuracy Curves of Multiple Experiments",
    fig_name=f"Accuracy_for_exps_lre_3_{max_show_rnd}.jpg",
    max_show_rnd=max_show_rnd
)
max_show_rnd = 5
plot_loss(
    all_exp_losses,
    y_label="Loss",
    title="Loss Curves of Multiple Experiments",
    fig_name=f"Loss_for_exps_lre_3_{max_show_rnd}.jpg",
    max_show_rnd=max_show_rnd
)
plot_loss(
    all_exp_acc,
    y_label="Accuracy",
    title="Accuracy Curves of Multiple Experiments",
    fig_name=f"Accuracy_for_exps_lre_3_{max_show_rnd}.jpg",
    max_show_rnd=max_show_rnd
)
