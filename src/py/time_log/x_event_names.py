import json
from flwr.common.constant import MessageType

# EVENTS_SERVER = [
#     "start run_server",
#     "operator starts",
#     "going queue_checker",
#     "start_training",
#     "local models OK, going aggregate",
#     "aggregate OK",
#     "going evaluation",
#     "evaluation OK",
#     "rounds end, metrics_logging",
#     "metrics_logging OK (going next round)",
#     "FINISH TRAINING",
#     "END run_server",
# ]
# DURATION_KEYWORDS_SERVER = {
#     "server_duration": (EVENTS_SERVER[0], EVENTS_SERVER[-1]),
#     "server_controller_init": (EVENTS_SERVER[0], EVENTS_SERVER[1]),
#     "operator_init(np.save)": (EVENTS_SERVER[1], EVENTS_SERVER[2]),
#     "training": (EVENTS_SERVER[2], EVENTS_SERVER[-2]),
#     "round****": (EVENTS_SERVER[3], EVENTS_SERVER[-3]), # ****=round number
# }

EVENTS_SERVER = [
    "start run_sim",
    "before server.fit()",
    "gonna get init params",
    "got init params / evaluate inin params",
    "done evaluate inin params / log init metrics",
    "start_training", # round #{} # i=5 # current round START
    "done configuration", # round #{}
    "local models OK, going aggregate", # round #{}
    "aggregate OK", # round #{}
    "going evaluation (strategy.evaluate)", # round #{}
    "evaluation OK / start metrics_logging (strategy.evaluate)", # round #{} # i=10
    "done metrics_logging (strategy.evaluate)", # round #{}
    "going evaluation (strategy.evaluate_round [distributed])", # round #{}
    "evaluation OK / start metrics_logging (strategy.evaluate_round [distributed])", # round #{}
    "done metrics_logging (strategy.evaluate_round [distributed]) going next round", # round #{} # current round END
    "FINISH TRAINING server.fit() done",
    "END run_sim",
]

DURATION_KEYWORDS_SERVER = {
    "sim_duration": (EVENTS_SERVER[0], EVENTS_SERVER[-1]),
    "server_init": (EVENTS_SERVER[0], EVENTS_SERVER[1]),
    "get_init_param": (EVENTS_SERVER[2], EVENTS_SERVER[3]),
    "evaluate_init_param": (EVENTS_SERVER[3], EVENTS_SERVER[4]),
    "training": (EVENTS_SERVER[5], EVENTS_SERVER[-2]), # be careful with the round number #1, to the FINISHING TRAINING
    "round****": (EVENTS_SERVER[5], EVENTS_SERVER[-3]), # ****=round number
}

DURATION_KEYWORDS_PERROUND = {
    "configuration": (EVENTS_SERVER[5], EVENTS_SERVER[6]),
    "local_training": (EVENTS_SERVER[6], EVENTS_SERVER[7]), # check DURATION_KEYWORDS_CLIENTS
    "aggregate": (EVENTS_SERVER[7], EVENTS_SERVER[8]),
    "evaluation (strategy.evaluate)": (EVENTS_SERVER[9], EVENTS_SERVER[10]),
    "metrics_logging (strategy.evaluate)": (EVENTS_SERVER[10], EVENTS_SERVER[11]),
    "evaluation (strategy.evaluate_round [distributed])": (EVENTS_SERVER[12], EVENTS_SERVER[13]), # check DURATION_KEYWORDS_CLIENTS
    "metrics_logging (strategy.evaluate_round [distributed])": (EVENTS_SERVER[13], EVENTS_SERVER[14]),
}

# EVENTS_MESSAGE = [
#     "message GET ****", # training or evaluating
#     "decode **** message OK",
#     "going ray worker ****",
#     "ray worker START ****", # into ray worker
#     "start setDataLoader ****",
#     "done setDataLoader / start setModel ****",
#     "done setModel / start create model dir ****",
#     "done create model dir / going into epochs loop ****",
#     "done training / start evaluate for **** after",
#     "done evaluate / start ray session reporting for ****",
#     "done ray session reporting / start model saving for ****",
#     "done model saving / ray worker END for ****", # gonna quit ray worker
#     "back from ray worker ****",
#     "message FIN ****",
# ]
# DURATION_KEYWORDS_CE = {
#     # "ce_duration": (EVENTS_CE[0], EVENTS_CE[-1]),
#     # "ce_server_init": (EVENTS_CE[0], EVENTS_CE[1]),
#     # "msg_handing": None,
#     "message": (EVENTS_MESSAGE[0], EVENTS_MESSAGE[-1]),
#     "decode_msg": (EVENTS_MESSAGE[0], EVENTS_MESSAGE[1]),
#     "ce_initiate_er": (EVENTS_MESSAGE[1], EVENTS_MESSAGE[2]),
#     "distributing_to_ray_worker": (EVENTS_MESSAGE[2], EVENTS_MESSAGE[3]),
#     "ray_hyperparams_init": (EVENTS_MESSAGE[3], EVENTS_MESSAGE[4]),
#     "ray_setDataLoader": (EVENTS_MESSAGE[4], EVENTS_MESSAGE[5]),
#     "ray_setModel": (EVENTS_MESSAGE[5], EVENTS_MESSAGE[6]),
#     "ray_create_model_dir": (EVENTS_MESSAGE[6], EVENTS_MESSAGE[7]),
#     "ray_epochs_loop": (EVENTS_MESSAGE[7], EVENTS_MESSAGE[8]),
#     "ray_evaluate": (EVENTS_MESSAGE[8], EVENTS_MESSAGE[9]),
#     "ray_session_reporting": (EVENTS_MESSAGE[9], EVENTS_MESSAGE[10]),
#     "ray_model_saving": (EVENTS_MESSAGE[10], EVENTS_MESSAGE[11]),
#     "back_to_head_from_worker": (EVENTS_MESSAGE[11], EVENTS_MESSAGE[12]),
#     "encode_msg": (EVENTS_MESSAGE[12], EVENTS_MESSAGE[13]),
# }

EVENTS_CLIENTS = [ # all with {msgtype}, {cid}, {round#}
    "message GET",
    "ClientProxy.fit() gonna _submit_job()",
    "gonna call actor_pool to submit_client_job()",
    "VCEActorPool gonna submit()",
    "VCEActorPool.submit() gonna call fn(actor, app_fn, mssg, cid, context)", # go FlowerClient.__init__() then into client.fit()
    "get_client_result from actor_pool",
    "message FIN",
]
EVENTS_RAY_WORKER = [ # all with {msgtype}, {cid}, {round#} # ray worker start
    "ray_client_fn start",
    "done load_partition / split and transform dataset",
    "done split and transform dataset / call FlowerClient",
    "FlowerClient __init__() start",
    "FlowerClient __init__() / self.model",
    "FlowerClient __init__() done Net()",
    "FlowerClient __init__() END", #6
    "into client.func() / gonna set_params()",
    "done set_params() / gonna set DataLoader(not create dataset)",
    "done set DataLoader(not create dataset) / gonna set optimizer",
    "done set optimizer / gonna train()/test() epochs",
    "done train()/test() epochs / gonna return to ray_client_proxy", # ray worker end
]

DURATION_KEYWORDS_CLIENTS = {
    "message": (EVENTS_CLIENTS[0], EVENTS_CLIENTS[-1]),
    "msg_passing_from_clientproxy_to_actorpool": (EVENTS_CLIENTS[0], EVENTS_CLIENTS[4]),
    "from_head(actorpool)_to_worker": (EVENTS_CLIENTS[4], EVENTS_RAY_WORKER[0]),
    "ray_worker_training": (EVENTS_RAY_WORKER[0], EVENTS_RAY_WORKER[-1]),
    "back_to_head_from_worker": (EVENTS_RAY_WORKER[-1], EVENTS_CLIENTS[-2]),
    "clientporxy_ending": (EVENTS_CLIENTS[-2], EVENTS_CLIENTS[-1]),
}

DURATION_RAY_WORKER = {
    "ray_load_partition": (EVENTS_RAY_WORKER[0], EVENTS_RAY_WORKER[1]),
    "ray_split_transform_dataset": (EVENTS_RAY_WORKER[1], EVENTS_RAY_WORKER[2]),
    "ray_client_init_setModel": (EVENTS_RAY_WORKER[2], EVENTS_RAY_WORKER[8]), # init + setParam # check DURATION_RAY_CLIENT_INIT_SETMODEL
    "ray_setDataLoader": (EVENTS_RAY_WORKER[8], EVENTS_RAY_WORKER[9]),
    "ray_setOptimizer": (EVENTS_RAY_WORKER[9], EVENTS_RAY_WORKER[10]), # in train, not in evaluate
    "ray_epochs_loop": (EVENTS_RAY_WORKER[10], EVENTS_RAY_WORKER[11]),
}

DURATION_RAY_CLIENT_INIT_SETMODEL = {
    "ray_client_call_and_init": (EVENTS_RAY_WORKER[2], EVENTS_RAY_WORKER[4]),
    "ray_client_setModel": (EVENTS_RAY_WORKER[4], EVENTS_RAY_WORKER[5]),
    "ray_client_model_to_device": (EVENTS_RAY_WORKER[5], EVENTS_RAY_WORKER[6]),
}


def print_in_json(data):
    print(json.dumps(data, indent=4))

def get_time_log_into_list(time_log_path:str) -> list[tuple[str, float]]:
    with open(time_log_path, "r") as file:
        event_names = [line.strip() for line in file]

    event_info = []
    for event in event_names:
        event_parts = event.split(" | ")
        name_slot = event_parts[3]
        event_name = name_slot.split(": ")[1]
        time_slot = event_parts[-1]
        event_time = float(time_slot.split(": ")[1])
        event_info.append((event_name, event_time))
    
    return event_info

def check_keywords_in_event(event_name:dict, keywords:list[str]) -> bool:
    for keyword in keywords:
        if keyword not in event_name:
            return False
    return True

def get_time_from_keyword(time_list:dict, keywords:list[str]) -> float:
    res_list = []
    for event_name, event_time in time_list:
        if check_keywords_in_event(event_name, keywords):
            res_list.append((event_name, event_time))

    # no result found
    if len(res_list) == 0:
        print("Cannot find the keywords \"{}\" in the time_list.".format(keywords))
        return -1

    # found 2 results -> error
    if len(res_list) > 1:
        print("Multiple events found with the keyword \"{}\" in the time_list.\n{}".format(keywords, res_list))
        return -1
    return res_list[0][-1]

def get_duration_from_keyword(time_list:dict, start_keyword:str, end_keyword:str, other_keywords:list[str] = None) -> float:
    if other_keywords is None:
        other_keywords = []
    start_time = get_time_from_keyword(time_list, [start_keyword] + other_keywords)
    end_time = get_time_from_keyword(time_list, [end_keyword] + other_keywords)
    return end_time - start_time


round = 20
sim_time_log_path = "/home/jack/jacklab/flowerHome/flowerTest_flwr17/simulation-pytorch-resnet50/time_log/flwrsim_time_log.txt"
sim_time_log_list = get_time_log_into_list(sim_time_log_path)
print(sim_time_log_list, "\n")

# wirte "round #{}" for FlowerClient __init__()


# sim_duration = {
#     "duration": 28.302478790283203,
#     "steps": {
#         "server_init": {
#             "duration": 2.38617205619812,
#             "steps": {}
#         },
#         "get_init_param": {
#             "duration": 2.5387167930603027,
#             "steps": {}
#         },
#         "evaluate_init_param": {
#             "duration": 3.384044885635376,
#             "steps": {}
#         },
#         "training": {
#             "duration": 19.992247104644775,
#             "steps": {
#                 "round1": {
#                     "duration": 11.182354927062988,
#                     "messages": {
#                         "round1_cid1_training": {
#                             "duration": 11.182354927062988,
#                             "steps": {}
#                         }
#                         "round1_cid2_training": {
#                             "duration": 11.182354927062988,
#                             "steps": {}
#                         }
#                 },
#                 "round2": {
#                     "duration": 8.809763193130493,
#                     "messages": {}
#                 }
#             }
#         }
#     }
# }

### create "steps" section for sim_duration -> server_init, get_init_param, evaluate_init_param
## calculate time (server_init, get_init_param, evaluate_init_param)
sim_duration_steps = {}
for step, (start, end) in list(DURATION_KEYWORDS_SERVER.items())[1:-2]: # server_init, get_init_param, evaluate_init_param
    sim_duration_steps[step] = {
        "duration": get_duration_from_keyword(sim_time_log_list, start, end),
        "steps": {},
    }
## create "training" for sim_duration) -> training
sim_duration_steps["training"] = {
    "duration": get_time_from_keyword(sim_time_log_list, DURATION_KEYWORDS_SERVER["training"][1]) - get_time_from_keyword(sim_time_log_list, [DURATION_KEYWORDS_SERVER["training"][0], "round #1"]),
    "steps": {},
}
training_steps = {}
# create "steps" section for training -> round1, round2, ...
for i in range(1, round+1):
    round_start = DURATION_KEYWORDS_SERVER["round****"][0]
    round_end = DURATION_KEYWORDS_SERVER["round****"][1]
    other_keywords = [f"round #{i}"]
    training_steps[f"round{i}"] = {
        "duration": get_duration_from_keyword(sim_time_log_list, round_start, round_end, other_keywords),
        "steps": {},
    }

    # create round_events (under round1, round2, ...) -> configuration, local_training, ...
    for step, (start, end) in DURATION_KEYWORDS_PERROUND.items():
        # "clients" not "steps" when local_training
        if step=="local_training":
            training_steps[f"round{i}"]["steps"][step] = {
                "duration": get_duration_from_keyword(sim_time_log_list, start, end, [f"round #{i}"]),
                "clients": {},
            }
            continue

        training_steps[f"round{i}"]["steps"][step] = {
            "duration": get_duration_from_keyword(sim_time_log_list, start, end, [f"round #{i}"]),
            "steps": {},
        }

# ### create "sim_duration" as whole
sim_duration_steps["training"]["steps"] = training_steps
sim_duration = {
    "duration": get_duration_from_keyword(sim_time_log_list, DURATION_KEYWORDS_SERVER["sim_duration"][0],  DURATION_KEYWORDS_SERVER["sim_duration"][1]),
    "steps": sim_duration_steps,
}
# print_in_json(sim_duration)

### create client events (under round{i} / local_training / {cid}) -> message, msg_passing_from_clientproxy_to_actorpool, ...
## get cids
cids = []
for oneline, _ in sim_time_log_list:
    if "===" in oneline:
        segmented_oneline = oneline.split("===")
        for i, segment in enumerate(segmented_oneline):
            if "cid " == segment[-4:]:
                cid = segmented_oneline[i+1]
                break
        cids.append(cid)
cids = list(set(cids))
print("cids in sim:", cids) # assume that train/evaluate with all cids #TODO

## create client_events according to cids under round{i} / local_training
for i in range(1, round+1):
    clients_training_steps_per_round = {} # init for round{i}
    for cid in cids:
        clients_training_steps_per_round[cid] = {"duration": -1, "steps": {}} # init for client
        for step, (start, end) in DURATION_KEYWORDS_CLIENTS.items():
            other_keywords = [f"{MessageType.TRAIN};", f"cid ==={cid}===", f"round #{i}"]
            if step == "message":
                clients_training_steps_per_round[cid]["duration"] = get_duration_from_keyword(sim_time_log_list, start, end, other_keywords)
                continue

            clients_training_steps_per_round[cid]["steps"][step] = {
                "duration": get_duration_from_keyword(sim_time_log_list, start, end, other_keywords),
                "steps": {},
            }

            if step == "ray_worker_training":
                for ray_worker_step, (ray_start, ray_end) in DURATION_RAY_WORKER.items():
                    clients_training_steps_per_round[cid]["steps"][step]["steps"][ray_worker_step] = {
                        "duration": get_duration_from_keyword(sim_time_log_list, ray_start, ray_end, other_keywords),
                        "steps": {},
                    }

                    if ray_worker_step == "ray_client_init_setModel":
                        for ray_client_step, (ray_client_start, ray_client_end) in DURATION_RAY_CLIENT_INIT_SETMODEL.items():
                            clients_training_steps_per_round[cid]["steps"][step]["steps"][ray_worker_step]["steps"][ray_client_step] = {
                                "duration": get_duration_from_keyword(sim_time_log_list, ray_client_start, ray_client_end, other_keywords),
                                "steps": {},
                            }

    sim_duration_steps["training"]["steps"][f"round{i}"]["steps"]["local_training"]["clients"] = clients_training_steps_per_round
print_in_json(sim_duration)

# for i in range(round):
#     cids = sim_duration_steps["training"]["steps"][f"round{i+1}"]["steps"]["local_training"]["clients"].keys()
#     for cid in cids:
#         print(sim_duration_steps["training"]["steps"][f"round{i+1}"]["steps"]["local_training"]["clients"][cid]["steps"]["ray_worker_training"]["steps"]["ray_client_init_setModel"]["steps"]["ray_client_model_to_device"])
