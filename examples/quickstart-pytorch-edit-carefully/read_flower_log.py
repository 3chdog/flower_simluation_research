import matplotlib.pyplot as plt
from typing import Callable
from dataclasses import dataclass



@dataclass
class Metrics:
    loss: list[float]
    accuracy: list[float]
    other_metrics: dict = None

@dataclass
class Experiment_Result:
    exp_name: str
    hyperparameters: dict # check fn: get_all_hyperparamters_from_one_exp_lines()
    metrics: Metrics



def get_every_exp_lines(lines: list) -> list[list[str]]:
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
            # print(f"Experiment {exp_num} end, with {len(one_exp_lines)} lines")
            all_exp_lines.append(one_exp_lines)
            one_exp_lines = []
    return all_exp_lines

def check_type(value, type_assignation: Callable, log_str: str):
    try:
        return type_assignation(value)
    except Exception as e:
        raise ValueError(
            "{}\nMaybe type error: Value [{}], its type should be {} but it is {}. Original line:\n{}".format(
                e, value, type_assignation, type(value), log_str
            )
        )

def get_hyperparameter_from_one_exp_lines(
        one_exp_lines: list,
        target,
        exclude: list = ["found in pyproject.toml", "replace"],
        split_func: Callable = None,
        type_assignation: Callable = None
):
    def no_excluded_words(line) -> bool:
        for et in exclude:
            if et in line:
                return False
        return True

    # Main Part: find target in one_exp_lines
    result = None
    for line in one_exp_lines:
        if target in line and no_excluded_words(line):
            result = line
            break

    # Not Found
    if result is None:
        print("Warning: target {} not found in one_exp_lines.\n(Excluded words: {})".format(target, exclude))
        return None

    # Split
    if split_func is not None:
        result = split_func(result)

    # Type Assignation
    if type_assignation is not None:
        result = check_type(result, type_assignation, result)

    return result

def get_all_hyperparamters_from_one_exp_lines(one_exp_lines: list):
    hyperparameters = {
        "server_rounds": None,
        "num_clients": None,
        "epochs": None,
        "learning_rate": None,
        "batch_size": None,
        "hetero": None,
    }
    hyperparameters["server_rounds"] = get_hyperparameter_from_one_exp_lines(
        one_exp_lines=one_exp_lines,
        target="num-server-rounds",
        split_func=lambda x: x.split(" = ")[-1],
        type_assignation=int,
    )
    hyperparameters["num_clients"] = get_hyperparameter_from_one_exp_lines(
        one_exp_lines=one_exp_lines,
        target="options.num-supernodes", # be aware that there should be only 1 "options.num-supernodes" in the log, originally 2 for cpu and gpu sim mode
        split_func=lambda x: x.split(" = ")[-1],
        type_assignation=int,
    )
    hyperparameters["epochs"] = get_hyperparameter_from_one_exp_lines(
        one_exp_lines=one_exp_lines,
        target="local-epochs",
        split_func=lambda x: x.split(" = ")[-1],
        type_assignation=int,
    )
    hyperparameters["learning_rate"] = get_hyperparameter_from_one_exp_lines(
        one_exp_lines=one_exp_lines,
        target="learning-rate",
        split_func=lambda x: x.split(" = ")[-1],
        type_assignation=float,
    )
    hyperparameters["batch_size"] = get_hyperparameter_from_one_exp_lines(
        one_exp_lines=one_exp_lines,
        target="batch-size",
        split_func=lambda x: x.split(" = ")[-1],
        type_assignation=int,
    )
    hyperparameters["hetero"] = get_hyperparameter_from_one_exp_lines(
        one_exp_lines=one_exp_lines,
        target="hetero",
        split_func=lambda x: x.split(" = ")[-1],
        type_assignation=int,
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
    assert len(losses) == server_rounds, f"len(losses): {len(losses)}, server_rounds: {server_rounds}"
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
    assert len(accuracies) == server_rounds, f"len(accuracies): {len(accuracies)}, server_rounds: {server_rounds}"
    return accuracies

# generate plots
def prepare_for_plot(all_exp_results: list[Experiment_Result], metric_name: str, max_show_rnd=None) -> dict[str, list[float]]:
    experiments = {}
    for exp in all_exp_results:
        one_exp_metric = exp.metrics.__getattribute__(metric_name)
        if max_show_rnd is not None:
            one_exp_metric = one_exp_metric[:max_show_rnd]
        experiments[exp.exp_name] = one_exp_metric
    return experiments

def plot_metric(
        experiments: dict[str, list[float]], # key: exp_name, value: list of metrics (one kind of metrics)
        y_label,
        fig_title,
        file_name="tmp.jpg",
):
    """
    Plot loss curves for multiple experiments on the same graph.
    :param experiments: dict, keys are experiment names, values are lists of loss values
    """
    plt.figure(figsize=(10, 6))
    
    for exp_name, losses in experiments.items():
        plt.plot(range(1, len(losses) + 1), losses, label=exp_name, alpha=0.7)
    
    plt.xlabel("Server Rounds")
    plt.ylabel(y_label)
    plt.title(fig_title)
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.savefig(file_name)

def get_exp_results_from_log(log_path: str, mode="original") -> list[Experiment_Result]:
    # read log
    with open(log_path, 'r') as f:
        lines = f.read().split('\n')
    all_exp_lines = get_every_exp_lines(lines)
    print("{} exps, every exp lines: {}".format(len(all_exp_lines), [len(one_exp_lines) for one_exp_lines in all_exp_lines]))

    # get all exp results
    all_exp_results: list[Experiment_Result] = []
    for i in range(1, len(all_exp_lines) + 1):
        hyperparameters = get_all_hyperparamters_from_one_exp_lines(all_exp_lines[i-1])
        num_clients = hyperparameters["num_clients"]
        lr_str = "0_01" if hyperparameters["learning_rate"]==0.01 else "0_001"
        losses = get_losses_from_one_exp_lines(all_exp_lines[i-1], server_rounds=hyperparameters["server_rounds"])
        accuracies = get_accuracies_from_one_exp_lines(all_exp_lines[i-1], server_rounds=hyperparameters["server_rounds"])
        all_exp_results.append(
            Experiment_Result(
                exp_name=f"{num_clients}_clients_lr_{lr_str}_{i}th_{mode}",
                hyperparameters=hyperparameters,
                metrics=Metrics(loss=losses, accuracy=accuracies)
            )
        )
    return all_exp_results

def main(list_log_path: list[str]):
    # read flwr log
    all_exp_results = []
    modes = ["original", "edited"]
    for log_path, mode in zip(list_log_path, modes):
        all_exp_results += get_exp_results_from_log(log_path, mode)[:24]
    # for exp in all_exp_results: print(exp.exp_name, exp.hyperparameters, len(exp.metrics.loss), len(exp.metrics.accuracy))

    # start plotting
    # fig name template: "diff_num_clients_exp_under_same_lr_e_2_iid_500rounds_Loss.jpg"
    list_lr = ["e_2"]*5 + ["e_3"]*5 + ["e_2"]*5 + ["e_3"]*5
    list_iid = ["iid"]*10 + ["non_iid"]*10
    list_exp_ids = [[0,1,2,3,4,5,6]]*5 + [[7,8,9,10,11,12,13]]*5 + [[14,15,16,17,18,19,20]]*5 + [[21,22,23,24,25,26,27]]*5
    list_max_show_rnd = [5, 10, 20, 100, 500] + [5, 10, 20, 100, 500] + [5, 10, 20, 100, 500] + [5, 10, 20, 100, 500]

    # plot Loss
    titles_loss = ["Loss Curves with lr {} and {} under Different Number of Clients".format(
        lr, distrib) for lr, distrib in zip(list_lr, list_iid)]
    fig_name_loss = ["exp_charts/diff_num_clients_exp_under_same_lr_{}_{}_{}rounds_Loss.jpg".format(
        lr, distrib, mx_show_rnd) for lr, distrib, mx_show_rnd in zip(list_lr, list_iid, list_max_show_rnd)]
    for exp_ids, title, fig_name, max_show_rnd in zip(list_exp_ids, titles_loss, fig_name_loss, list_max_show_rnd):
        experiments = prepare_for_plot([all_exp_results[i] for i in exp_ids], "loss", max_show_rnd)
        y_label="Loss"
        # plot_metric(
        #     experiments=experiments,
        #     y_label=y_label,
        #     fig_title=title,
        #     file_name=fig_name,
        # )

    # plot Accuracy
    titles_acc = ["Accuracy Curves with lr {} and {} under Different Number of Clients".format(
        lr, distrib) for lr, distrib in zip(list_lr, list_iid)]
    fig_name_acc = ["exp_charts/diff_num_clients_exp_under_same_lr_{}_{}_{}rounds_Accuracy.jpg".format(
        lr, distrib, mx_show_rnd) for lr, distrib, mx_show_rnd in zip(list_lr, list_iid, list_max_show_rnd)]
    for exp_ids, title, fig_name, max_show_rnd in zip(list_exp_ids, titles_acc, fig_name_acc, list_max_show_rnd):
        experiments = prepare_for_plot([all_exp_results[i] for i in exp_ids], "accuracy", max_show_rnd)
        y_label="Accuracy"
        # plot_metric(
        #     experiments=experiments,
        #     y_label=y_label,
        #     fig_title=title,
        #     file_name=fig_name,
        # )

    return all_exp_results

if __name__ == "__main__":
    main(
        [
            "/home/jack/jacklab/flowerHome/flower_simluation_research/examples/quickstart-pytorch/sim_exp_0324_76.log",
            "/home/jack/jacklab/flowerHome/flower_simluation_research/examples/quickstart-pytorch/sim_exp_0324_not_full.log",
        ]
    )
