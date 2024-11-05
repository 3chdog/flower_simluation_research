a = {
    "duration": 101.24029517173767,
    "steps": {
        "server_init": {
            "duration": 0.12942218780517578,
            "steps": {}
        },
        "get_init_param": {
            "duration": 2.260493278503418,
            "steps": {}
        },
        "evaluate_init_param": {
            "duration": 3.503298044204712,
            "steps": {}
        },
        "training": {
            "duration": 95.3446261882782,
            "steps": {
                "round1": {
                    "duration": 11.271578311920166,
                    "steps": {
                        "configuration": {
                            "duration": 9.107589721679688e-05,
                            "steps": {}
                        },
                        "local_training": {
                            "duration": 8.776681423187256,
                            "clients": {
                                "0": {
                                    "duration": 8.771928071975708,
                                    "steps": {
                                        "msg_passing_from_clientproxy_to_actorpool": {
                                            "duration": 0.0011572837829589844,
                                            "steps": {}
                                        },
                                        "from_head(actorpool)_to_worker": {
                                            "duration": 0.8072547912597656,
                                            "steps": {}
                                        },
                                        "ray_worker_training": {
                                            "duration": 7.959616661071777,
                                            "steps": {
                                                "ray_load_partition": {
                                                    "duration": 0.0019736289978027344,
                                                    "steps": {}
                                                },
                                                "ray_split_transform_dataset": {
                                                    "duration": 0.003609180450439453,
                                                    "steps": {}
                                                },
                                                "ray_client_init_setModel": {
                                                    "duration": 0.009268522262573242,
                                                    "steps": {
                                                        "ray_client_call_and_init": {
                                                            "duration": 8.7738037109375e-05,
                                                            "steps": {}
                                                        },
                                                        "ray_client_setModel": {
                                                            "duration": 0.0015332698822021484,
                                                            "steps": {}
                                                        },
                                                        "ray_client_model_to_device": {
                                                            "duration": 0.006292819976806641,
                                                            "steps": {}
                                                        }
                                                    }
                                                },
                                                "ray_setDataLoader": {
                                                    "duration": 0.0001544952392578125,
                                                    "steps": {}
                                                },
                                                "ray_setOptimizer": {
                                                    "duration": 0.00010037422180175781,
                                                    "steps": {}
                                                },
                                                "ray_epochs_loop": {
                                                    "duration": 7.944510459899902,
                                                    "steps": {}
                                                }
                                            }
                                        },
                                        "back_to_head_from_worker": {
                                            "duration": 0.0038149356842041016,
                                            "steps": {}
                                        },
                                        "clientporxy_ending": {
                                            "duration": 8.440017700195312e-05,
                                            "steps": {}
                                        }
                                    }
                                },
                                "1": {
                                    "duration": 8.163033485412598,
                                    "steps": {
                                        "msg_passing_from_clientproxy_to_actorpool": {
                                            "duration": 0.0003211498260498047,
                                            "steps": {}
                                        },
                                        "from_head(actorpool)_to_worker": {
                                            "duration": 0.00847935676574707,
                                            "steps": {}
                                        },
                                        "ray_worker_training": {
                                            "duration": 8.150382280349731,
                                            "steps": {
                                                "ray_load_partition": {
                                                    "duration": 0.0018963813781738281,
                                                    "steps": {}
                                                },
                                                "ray_split_transform_dataset": {
                                                    "duration": 0.004629373550415039,
                                                    "steps": {}
                                                },
                                                "ray_client_init_setModel": {
                                                    "duration": 0.0023255348205566406,
                                                    "steps": {
                                                        "ray_client_call_and_init": {
                                                            "duration": 0.00010728836059570312,
                                                            "steps": {}
                                                        },
                                                        "ray_client_setModel": {
                                                            "duration": 0.0007662773132324219,
                                                            "steps": {}
                                                        },
                                                        "ray_client_model_to_device": {
                                                            "duration": 0.00013685226440429688,
                                                            "steps": {}
                                                        }
                                                    }
                                                },
                                                "ray_setDataLoader": {
                                                    "duration": 0.00020599365234375,
                                                    "steps": {}
                                                },
                                                "ray_setOptimizer": {
                                                    "duration": 9.965896606445312e-05,
                                                    "steps": {}
                                                },
                                                "ray_epochs_loop": {
                                                    "duration": 8.141225337982178,
                                                    "steps": {}
                                                }
                                            }
                                        },
                                        "back_to_head_from_worker": {
                                            "duration": 0.003737926483154297,
                                            "steps": {}
                                        },
                                        "clientporxy_ending": {
                                            "duration": 0.00011277198791503906,
                                            "steps": {}
                                        }
                                    }
                                }
                            }
                        },
                        "aggregate": {
                            "duration": 0.0017113685607910156,
                            "steps": {}
                        },
                        "evaluation (strategy.evaluate)": {
                            "duration": 1.8204712867736816,
                            "steps": {}
                        },
                        "metrics_logging (strategy.evaluate)": {
                            "duration": 0.0001575946807861328,
                            "steps": {}
                        },
                        "evaluation (strategy.evaluate_round [distributed])": {
                            "duration": 0.6723494529724121,
                            "steps": {}
                        },
                        "metrics_logging (strategy.evaluate_round [distributed])": {
                            "duration": 4.172325134277344e-05,
                            "steps": {}
                        }
                    }
                },
                "round2": {
                    "duration": 10.45262622833252,
                    "steps": {
                        "configuration": {
                            "duration": 6.532669067382812e-05,
                            "steps": {}
                        },
                        "local_training": {
                            "duration": 8.025393009185791,
                            "clients": {
                                "0": {
                                    "duration": 8.024858236312866,
                                    "steps": {
                                        "msg_passing_from_clientproxy_to_actorpool": {
                                            "duration": 0.0006537437438964844,
                                            "steps": {}
                                        },
                                        "from_head(actorpool)_to_worker": {
                                            "duration": 0.0071413516998291016,
                                            "steps": {}
                                        },
                                        "ray_worker_training": {
                                            "duration": 8.013283967971802,
                                            "steps": {
                                                "ray_load_partition": {
                                                    "duration": 0.0016202926635742188,
                                                    "steps": {}
                                                },
                                                "ray_split_transform_dataset": {
                                                    "duration": 0.005809307098388672,
                                                    "steps": {}
                                                },
                                                "ray_client_init_setModel": {
                                                    "duration": 0.003221750259399414,
                                                    "steps": {
                                                        "ray_client_call_and_init": {
                                                            "duration": 0.00012087821960449219,
                                                            "steps": {}
                                                        },
                                                        "ray_client_setModel": {
                                                            "duration": 0.0012145042419433594,
                                                            "steps": {}
                                                        },
                                                        "ray_client_model_to_device": {
                                                            "duration": 0.00019121170043945312,
                                                            "steps": {}
                                                        }
                                                    }
                                                },
                                                "ray_setDataLoader": {
                                                    "duration": 0.00010895729064941406,
                                                    "steps": {}
                                                },
                                                "ray_setOptimizer": {
                                                    "duration": 0.0001220703125,
                                                    "steps": {}
                                                },
                                                "ray_epochs_loop": {
                                                    "duration": 8.00240159034729,
                                                    "steps": {}
                                                }
                                            }
                                        },
                                        "back_to_head_from_worker": {
                                            "duration": 0.003690481185913086,
                                            "steps": {}
                                        },
                                        "clientporxy_ending": {
                                            "duration": 8.869171142578125e-05,
                                            "steps": {}
                                        }
                                    }
                                },
                                "1": {
                                    "duration": 7.946979284286499,
                                    "steps": {
                                        "msg_passing_from_clientproxy_to_actorpool": {
                                            "duration": 0.004764556884765625,
                                            "steps": {}
                                        },
                                        "from_head(actorpool)_to_worker": {
                                            "duration": 0.00826883316040039,
                                            "steps": {}
                                        },
                                        "ray_worker_training": {
                                            "duration": 7.929732084274292,
                                            "steps": {
                                                "ray_load_partition": {
                                                    "duration": 0.002274751663208008,
                                                    "steps": {}
                                                },
                                                "ray_split_transform_dataset": {
                                                    "duration": 0.005689859390258789,
                                                    "steps": {}
                                                },
                                                "ray_client_init_setModel": {
                                                    "duration": 0.0031571388244628906,
                                                    "steps": {
                                                        "ray_client_call_and_init": {
                                                            "duration": 0.000110626220703125,
                                                            "steps": {}
                                                        },
                                                        "ray_client_setModel": {
                                                            "duration": 0.0012273788452148438,
                                                            "steps": {}
                                                        },
                                                        "ray_client_model_to_device": {
                                                            "duration": 0.00019288063049316406,
                                                            "steps": {}
                                                        }
                                                    }
                                                },
                                                "ray_setDataLoader": {
                                                    "duration": 0.00010824203491210938,
                                                    "steps": {}
                                                },
                                                "ray_setOptimizer": {
                                                    "duration": 0.00011563301086425781,
                                                    "steps": {}
                                                },
                                                "ray_epochs_loop": {
                                                    "duration": 7.918386459350586,
                                                    "steps": {}
                                                }
                                            }
                                        },
                                        "back_to_head_from_worker": {
                                            "duration": 0.004117727279663086,
                                            "steps": {}
                                        },
                                        "clientporxy_ending": {
                                            "duration": 9.608268737792969e-05,
                                            "steps": {}
                                        }
                                    }
                                }
                            }
                        },
                        "aggregate": {
                            "duration": 0.0015871524810791016,
                            "steps": {}
                        },
                        "evaluation (strategy.evaluate)": {
                            "duration": 1.7607710361480713,
                            "steps": {}
                        },
                        "metrics_logging (strategy.evaluate)": {
                            "duration": 0.0001571178436279297,
                            "steps": {}
                        },
                        "evaluation (strategy.evaluate_round [distributed])": {
                            "duration": 0.6645112037658691,
                            "steps": {}
                        },
                        "metrics_logging (strategy.evaluate_round [distributed])": {
                            "duration": 4.2438507080078125e-05,
                            "steps": {}
                        }
                    }
                },
                "round3": {
                    "duration": 10.533491134643555,
                    "steps": {
                        "configuration": {
                            "duration": 5.0067901611328125e-05,
                            "steps": {}
                        },
                        "local_training": {
                            "duration": 8.03459882736206,
                            "clients": {
                                "0": {
                                    "duration": 8.005332469940186,
                                    "steps": {
                                        "msg_passing_from_clientproxy_to_actorpool": {
                                            "duration": 0.00498652458190918,
                                            "steps": {}
                                        },
                                        "from_head(actorpool)_to_worker": {
                                            "duration": 0.007446765899658203,
                                            "steps": {}
                                        },
                                        "ray_worker_training": {
                                            "duration": 7.988419771194458,
                                            "steps": {
                                                "ray_load_partition": {
                                                    "duration": 0.001476287841796875,
                                                    "steps": {}
                                                },
                                                "ray_split_transform_dataset": {
                                                    "duration": 0.0035338401794433594,
                                                    "steps": {}
                                                },
                                                "ray_client_init_setModel": {
                                                    "duration": 0.002002716064453125,
                                                    "steps": {
                                                        "ray_client_call_and_init": {
                                                            "duration": 8.106231689453125e-05,
                                                            "steps": {}
                                                        },
                                                        "ray_client_setModel": {
                                                            "duration": 0.0007605552673339844,
                                                            "steps": {}
                                                        },
                                                        "ray_client_model_to_device": {
                                                            "duration": 0.00012040138244628906,
                                                            "steps": {}
                                                        }
                                                    }
                                                },
                                                "ray_setDataLoader": {
                                                    "duration": 7.796287536621094e-05,
                                                    "steps": {}
                                                },
                                                "ray_setOptimizer": {
                                                    "duration": 7.843971252441406e-05,
                                                    "steps": {}
                                                },
                                                "ray_epochs_loop": {
                                                    "duration": 7.981250524520874,
                                                    "steps": {}
                                                }
                                            }
                                        },
                                        "back_to_head_from_worker": {
                                            "duration": 0.004339456558227539,
                                            "steps": {}
                                        },
                                        "clientporxy_ending": {
                                            "duration": 0.0001399517059326172,
                                            "steps": {}
                                        }
                                    }
                                },
                                "1": {
                                    "duration": 8.034081935882568,
                                    "steps": {
                                        "msg_passing_from_clientproxy_to_actorpool": {
                                            "duration": 0.0007543563842773438,
                                            "steps": {}
                                        },
                                        "from_head(actorpool)_to_worker": {
                                            "duration": 0.007130146026611328,
                                            "steps": {}
                                        },
                                        "ray_worker_training": {
                                            "duration": 8.022159337997437,
                                            "steps": {
                                                "ray_load_partition": {
                                                    "duration": 0.0017659664154052734,
                                                    "steps": {}
                                                },
                                                "ray_split_transform_dataset": {
                                                    "duration": 0.004011631011962891,
                                                    "steps": {}
                                                },
                                                "ray_client_init_setModel": {
                                                    "duration": 0.0019767284393310547,
                                                    "steps": {
                                                        "ray_client_call_and_init": {
                                                            "duration": 9.179115295410156e-05,
                                                            "steps": {}
                                                        },
                                                        "ray_client_setModel": {
                                                            "duration": 0.0007109642028808594,
                                                            "steps": {}
                                                        },
                                                        "ray_client_model_to_device": {
                                                            "duration": 0.0001220703125,
                                                            "steps": {}
                                                        }
                                                    }
                                                },
                                                "ray_setDataLoader": {
                                                    "duration": 7.939338684082031e-05,
                                                    "steps": {}
                                                },
                                                "ray_setOptimizer": {
                                                    "duration": 7.843971252441406e-05,
                                                    "steps": {}
                                                },
                                                "ray_epochs_loop": {
                                                    "duration": 8.014247179031372,
                                                    "steps": {}
                                                }
                                            }
                                        },
                                        "back_to_head_from_worker": {
                                            "duration": 0.0039288997650146484,
                                            "steps": {}
                                        },
                                        "clientporxy_ending": {
                                            "duration": 0.00010919570922851562,
                                            "steps": {}
                                        }
                                    }
                                }
                            }
                        },
                        "aggregate": {
                            "duration": 0.0015072822570800781,
                            "steps": {}
                        },
                        "evaluation (strategy.evaluate)": {
                            "duration": 1.8058583736419678,
                            "steps": {}
                        },
                        "metrics_logging (strategy.evaluate)": {
                            "duration": 0.00014662742614746094,
                            "steps": {}
                        },
                        "evaluation (strategy.evaluate_round [distributed])": {
                            "duration": 0.6911969184875488,
                            "steps": {}
                        },
                        "metrics_logging (strategy.evaluate_round [distributed])": {
                            "duration": 4.267692565917969e-05,
                            "steps": {}
                        }
                    }
                },
                "round4": {
                    "duration": 10.533304214477539,
                    "steps": {
                        "configuration": {
                            "duration": 5.1975250244140625e-05,
                            "steps": {}
                        },
                        "local_training": {
                            "duration": 8.079255104064941,
                            "clients": {
                                "0": {
                                    "duration": 8.078780174255371,
                                    "steps": {
                                        "msg_passing_from_clientproxy_to_actorpool": {
                                            "duration": 0.0006101131439208984,
                                            "steps": {}
                                        },
                                        "from_head(actorpool)_to_worker": {
                                            "duration": 0.007242441177368164,
                                            "steps": {}
                                        },
                                        "ray_worker_training": {
                                            "duration": 8.067027568817139,
                                            "steps": {
                                                "ray_load_partition": {
                                                    "duration": 0.0015709400177001953,
                                                    "steps": {}
                                                },
                                                "ray_split_transform_dataset": {
                                                    "duration": 0.0038547515869140625,
                                                    "steps": {}
                                                },
                                                "ray_client_init_setModel": {
                                                    "duration": 0.0019876956939697266,
                                                    "steps": {
                                                        "ray_client_call_and_init": {
                                                            "duration": 9.107589721679688e-05,
                                                            "steps": {}
                                                        },
                                                        "ray_client_setModel": {
                                                            "duration": 0.00070953369140625,
                                                            "steps": {}
                                                        },
                                                        "ray_client_model_to_device": {
                                                            "duration": 0.00012254714965820312,
                                                            "steps": {}
                                                        }
                                                    }
                                                },
                                                "ray_setDataLoader": {
                                                    "duration": 0.00011539459228515625,
                                                    "steps": {}
                                                },
                                                "ray_setOptimizer": {
                                                    "duration": 8.225440979003906e-05,
                                                    "steps": {}
                                                },
                                                "ray_epochs_loop": {
                                                    "duration": 8.05941653251648,
                                                    "steps": {}
                                                }
                                            }
                                        },
                                        "back_to_head_from_worker": {
                                            "duration": 0.0037889480590820312,
                                            "steps": {}
                                        },
                                        "clientporxy_ending": {
                                            "duration": 0.00011110305786132812,
                                            "steps": {}
                                        }
                                    }
                                },
                                "1": {
                                    "duration": 7.984987258911133,
                                    "steps": {
                                        "msg_passing_from_clientproxy_to_actorpool": {
                                            "duration": 0.0048749446868896484,
                                            "steps": {}
                                        },
                                        "from_head(actorpool)_to_worker": {
                                            "duration": 0.00731658935546875,
                                            "steps": {}
                                        },
                                        "ray_worker_training": {
                                            "duration": 7.969162464141846,
                                            "steps": {
                                                "ray_load_partition": {
                                                    "duration": 0.0014319419860839844,
                                                    "steps": {}
                                                },
                                                "ray_split_transform_dataset": {
                                                    "duration": 0.0035049915313720703,
                                                    "steps": {}
                                                },
                                                "ray_client_init_setModel": {
                                                    "duration": 0.0019378662109375,
                                                    "steps": {
                                                        "ray_client_call_and_init": {
                                                            "duration": 8.0108642578125e-05,
                                                            "steps": {}
                                                        },
                                                        "ray_client_setModel": {
                                                            "duration": 0.0006811618804931641,
                                                            "steps": {}
                                                        },
                                                        "ray_client_model_to_device": {
                                                            "duration": 0.000118255615234375,
                                                            "steps": {}
                                                        }
                                                    }
                                                },
                                                "ray_setDataLoader": {
                                                    "duration": 7.700920104980469e-05,
                                                    "steps": {}
                                                },
                                                "ray_setOptimizer": {
                                                    "duration": 8.559226989746094e-05,
                                                    "steps": {}
                                                },
                                                "ray_epochs_loop": {
                                                    "duration": 7.962125062942505,
                                                    "steps": {}
                                                }
                                            }
                                        },
                                        "back_to_head_from_worker": {
                                            "duration": 0.003504514694213867,
                                            "steps": {}
                                        },
                                        "clientporxy_ending": {
                                            "duration": 0.00012874603271484375,
                                            "steps": {}
                                        }
                                    }
                                }
                            }
                        },
                        "aggregate": {
                            "duration": 0.0015232563018798828,
                            "steps": {}
                        },
                        "evaluation (strategy.evaluate)": {
                            "duration": 1.780543327331543,
                            "steps": {}
                        },
                        "metrics_logging (strategy.evaluate)": {
                            "duration": 0.00014972686767578125,
                            "steps": {}
                        },
                        "evaluation (strategy.evaluate_round [distributed])": {
                            "duration": 0.6716506481170654,
                            "steps": {}
                        },
                        "metrics_logging (strategy.evaluate_round [distributed])": {
                            "duration": 4.1961669921875e-05,
                            "steps": {}
                        }
                    }
                },
                "round5": {
                    "duration": 10.487369060516357,
                    "steps": {
                        "configuration": {
                            "duration": 5.173683166503906e-05,
                            "steps": {}
                        },
                        "local_training": {
                            "duration": 8.036783695220947,
                            "clients": {
                                "0": {
                                    "duration": 8.035953283309937,
                                    "steps": {
                                        "msg_passing_from_clientproxy_to_actorpool": {
                                            "duration": 0.004581928253173828,
                                            "steps": {}
                                        },
                                        "from_head(actorpool)_to_worker": {
                                            "duration": 0.0074999332427978516,
                                            "steps": {}
                                        },
                                        "ray_worker_training": {
                                            "duration": 8.020063877105713,
                                            "steps": {
                                                "ray_load_partition": {
                                                    "duration": 0.0014705657958984375,
                                                    "steps": {}
                                                },
                                                "ray_split_transform_dataset": {
                                                    "duration": 0.0035588741302490234,
                                                    "steps": {}
                                                },
                                                "ray_client_init_setModel": {
                                                    "duration": 0.0019865036010742188,
                                                    "steps": {
                                                        "ray_client_call_and_init": {
                                                            "duration": 8.034706115722656e-05,
                                                            "steps": {}
                                                        },
                                                        "ray_client_setModel": {
                                                            "duration": 0.0007357597351074219,
                                                            "steps": {}
                                                        },
                                                        "ray_client_model_to_device": {
                                                            "duration": 0.00011968612670898438,
                                                            "steps": {}
                                                        }
                                                    }
                                                },
                                                "ray_setDataLoader": {
                                                    "duration": 7.653236389160156e-05,
                                                    "steps": {}
                                                },
                                                "ray_setOptimizer": {
                                                    "duration": 8.654594421386719e-05,
                                                    "steps": {}
                                                },
                                                "ray_epochs_loop": {
                                                    "duration": 8.012884855270386,
                                                    "steps": {}
                                                }
                                            }
                                        },
                                        "back_to_head_from_worker": {
                                            "duration": 0.0036847591400146484,
                                            "steps": {}
                                        },
                                        "clientporxy_ending": {
                                            "duration": 0.0001227855682373047,
                                            "steps": {}
                                        }
                                    }
                                },
                                "1": {
                                    "duration": 8.016688585281372,
                                    "steps": {
                                        "msg_passing_from_clientproxy_to_actorpool": {
                                            "duration": 0.0005228519439697266,
                                            "steps": {}
                                        },
                                        "from_head(actorpool)_to_worker": {
                                            "duration": 0.007145404815673828,
                                            "steps": {}
                                        },
                                        "ray_worker_training": {
                                            "duration": 8.00493049621582,
                                            "steps": {
                                                "ray_load_partition": {
                                                    "duration": 0.0014986991882324219,
                                                    "steps": {}
                                                },
                                                "ray_split_transform_dataset": {
                                                    "duration": 0.003977060317993164,
                                                    "steps": {}
                                                },
                                                "ray_client_init_setModel": {
                                                    "duration": 0.002025127410888672,
                                                    "steps": {
                                                        "ray_client_call_and_init": {
                                                            "duration": 9.083747863769531e-05,
                                                            "steps": {}
                                                        },
                                                        "ray_client_setModel": {
                                                            "duration": 0.0007572174072265625,
                                                            "steps": {}
                                                        },
                                                        "ray_client_model_to_device": {
                                                            "duration": 0.0001246929168701172,
                                                            "steps": {}
                                                        }
                                                    }
                                                },
                                                "ray_setDataLoader": {
                                                    "duration": 7.700920104980469e-05,
                                                    "steps": {}
                                                },
                                                "ray_setOptimizer": {
                                                    "duration": 7.867813110351562e-05,
                                                    "steps": {}
                                                },
                                                "ray_epochs_loop": {
                                                    "duration": 7.997273921966553,
                                                    "steps": {}
                                                }
                                            }
                                        },
                                        "back_to_head_from_worker": {
                                            "duration": 0.003948688507080078,
                                            "steps": {}
                                        },
                                        "clientporxy_ending": {
                                            "duration": 0.000141143798828125,
                                            "steps": {}
                                        }
                                    }
                                }
                            }
                        },
                        "aggregate": {
                            "duration": 0.0015711784362792969,
                            "steps": {}
                        },
                        "evaluation (strategy.evaluate)": {
                            "duration": 1.7818171977996826,
                            "steps": {}
                        },
                        "metrics_logging (strategy.evaluate)": {
                            "duration": 0.0001494884490966797,
                            "steps": {}
                        },
                        "evaluation (strategy.evaluate_round [distributed])": {
                            "duration": 0.666867733001709,
                            "steps": {}
                        },
                        "metrics_logging (strategy.evaluate_round [distributed])": {
                            "duration": 4.1484832763671875e-05,
                            "steps": {}
                        }
                    }
                },
                "round6": {
                    "duration": 10.549634456634521,
                    "steps": {
                        "configuration": {
                            "duration": 6.67572021484375e-05,
                            "steps": {}
                        },
                        "local_training": {
                            "duration": 8.08762240409851,
                            "clients": {
                                "0": {
                                    "duration": 8.086696863174438,
                                    "steps": {
                                        "msg_passing_from_clientproxy_to_actorpool": {
                                            "duration": 0.004651308059692383,
                                            "steps": {}
                                        },
                                        "from_head(actorpool)_to_worker": {
                                            "duration": 0.007166147232055664,
                                            "steps": {}
                                        },
                                        "ray_worker_training": {
                                            "duration": 8.071135759353638,
                                            "steps": {
                                                "ray_load_partition": {
                                                    "duration": 0.0015344619750976562,
                                                    "steps": {}
                                                },
                                                "ray_split_transform_dataset": {
                                                    "duration": 0.003583669662475586,
                                                    "steps": {}
                                                },
                                                "ray_client_init_setModel": {
                                                    "duration": 0.0020864009857177734,
                                                    "steps": {
                                                        "ray_client_call_and_init": {
                                                            "duration": 8.273124694824219e-05,
                                                            "steps": {}
                                                        },
                                                        "ray_client_setModel": {
                                                            "duration": 0.0006871223449707031,
                                                            "steps": {}
                                                        },
                                                        "ray_client_model_to_device": {
                                                            "duration": 0.00017261505126953125,
                                                            "steps": {}
                                                        }
                                                    }
                                                },
                                                "ray_setDataLoader": {
                                                    "duration": 8.0108642578125e-05,
                                                    "steps": {}
                                                },
                                                "ray_setOptimizer": {
                                                    "duration": 7.987022399902344e-05,
                                                    "steps": {}
                                                },
                                                "ray_epochs_loop": {
                                                    "duration": 8.06377124786377,
                                                    "steps": {}
                                                }
                                            }
                                        },
                                        "back_to_head_from_worker": {
                                            "duration": 0.0036191940307617188,
                                            "steps": {}
                                        },
                                        "clientporxy_ending": {
                                            "duration": 0.00012445449829101562,
                                            "steps": {}
                                        }
                                    }
                                },
                                "1": {
                                    "duration": 8.012169599533081,
                                    "steps": {
                                        "msg_passing_from_clientproxy_to_actorpool": {
                                            "duration": 0.0006170272827148438,
                                            "steps": {}
                                        },
                                        "from_head(actorpool)_to_worker": {
                                            "duration": 0.0071790218353271484,
                                            "steps": {}
                                        },
                                        "ray_worker_training": {
                                            "duration": 8.000279426574707,
                                            "steps": {
                                                "ray_load_partition": {
                                                    "duration": 0.0015726089477539062,
                                                    "steps": {}
                                                },
                                                "ray_split_transform_dataset": {
                                                    "duration": 0.004080772399902344,
                                                    "steps": {}
                                                },
                                                "ray_client_init_setModel": {
                                                    "duration": 0.0020220279693603516,
                                                    "steps": {
                                                        "ray_client_call_and_init": {
                                                            "duration": 9.298324584960938e-05,
                                                            "steps": {}
                                                        },
                                                        "ray_client_setModel": {
                                                            "duration": 0.0007100105285644531,
                                                            "steps": {}
                                                        },
                                                        "ray_client_model_to_device": {
                                                            "duration": 0.00012230873107910156,
                                                            "steps": {}
                                                        }
                                                    }
                                                },
                                                "ray_setDataLoader": {
                                                    "duration": 7.700920104980469e-05,
                                                    "steps": {}
                                                },
                                                "ray_setOptimizer": {
                                                    "duration": 7.963180541992188e-05,
                                                    "steps": {}
                                                },
                                                "ray_epochs_loop": {
                                                    "duration": 7.992447376251221,
                                                    "steps": {}
                                                }
                                            }
                                        },
                                        "back_to_head_from_worker": {
                                            "duration": 0.004000663757324219,
                                            "steps": {}
                                        },
                                        "clientporxy_ending": {
                                            "duration": 9.34600830078125e-05,
                                            "steps": {}
                                        }
                                    }
                                }
                            }
                        },
                        "aggregate": {
                            "duration": 0.0015721321105957031,
                            "steps": {}
                        },
                        "evaluation (strategy.evaluate)": {
                            "duration": 1.7849667072296143,
                            "steps": {}
                        },
                        "metrics_logging (strategy.evaluate)": {
                            "duration": 0.00014519691467285156,
                            "steps": {}
                        },
                        "evaluation (strategy.evaluate_round [distributed])": {
                            "duration": 0.6751213073730469,
                            "steps": {}
                        },
                        "metrics_logging (strategy.evaluate_round [distributed])": {
                            "duration": 4.57763671875e-05,
                            "steps": {}
                        }
                    }
                },
                "round7": {
                    "duration": 10.524900913238525,
                    "steps": {
                        "configuration": {
                            "duration": 8.988380432128906e-05,
                            "steps": {}
                        },
                        "local_training": {
                            "duration": 8.080822229385376,
                            "clients": {
                                "0": {
                                    "duration": 8.080255508422852,
                                    "steps": {
                                        "msg_passing_from_clientproxy_to_actorpool": {
                                            "duration": 0.0005831718444824219,
                                            "steps": {}
                                        },
                                        "from_head(actorpool)_to_worker": {
                                            "duration": 0.007360219955444336,
                                            "steps": {}
                                        },
                                        "ray_worker_training": {
                                            "duration": 8.067986011505127,
                                            "steps": {
                                                "ray_load_partition": {
                                                    "duration": 0.001657724380493164,
                                                    "steps": {}
                                                },
                                                "ray_split_transform_dataset": {
                                                    "duration": 0.004029750823974609,
                                                    "steps": {}
                                                },
                                                "ray_client_init_setModel": {
                                                    "duration": 0.0020394325256347656,
                                                    "steps": {
                                                        "ray_client_call_and_init": {
                                                            "duration": 9.1552734375e-05,
                                                            "steps": {}
                                                        },
                                                        "ray_client_setModel": {
                                                            "duration": 0.0007107257843017578,
                                                            "steps": {}
                                                        },
                                                        "ray_client_model_to_device": {
                                                            "duration": 0.00012540817260742188,
                                                            "steps": {}
                                                        }
                                                    }
                                                },
                                                "ray_setDataLoader": {
                                                    "duration": 0.00010776519775390625,
                                                    "steps": {}
                                                },
                                                "ray_setOptimizer": {
                                                    "duration": 8.0108642578125e-05,
                                                    "steps": {}
                                                },
                                                "ray_epochs_loop": {
                                                    "duration": 8.060071229934692,
                                                    "steps": {}
                                                }
                                            }
                                        },
                                        "back_to_head_from_worker": {
                                            "duration": 0.00423884391784668,
                                            "steps": {}
                                        },
                                        "clientporxy_ending": {
                                            "duration": 8.726119995117188e-05,
                                            "steps": {}
                                        }
                                    }
                                },
                                "1": {
                                    "duration": 7.900950908660889,
                                    "steps": {
                                        "msg_passing_from_clientproxy_to_actorpool": {
                                            "duration": 0.004629373550415039,
                                            "steps": {}
                                        },
                                        "from_head(actorpool)_to_worker": {
                                            "duration": 0.00732731819152832,
                                            "steps": {}
                                        },
                                        "ray_worker_training": {
                                            "duration": 7.885043144226074,
                                            "steps": {
                                                "ray_load_partition": {
                                                    "duration": 0.0014586448669433594,
                                                    "steps": {}
                                                },
                                                "ray_split_transform_dataset": {
                                                    "duration": 0.003728628158569336,
                                                    "steps": {}
                                                },
                                                "ray_client_init_setModel": {
                                                    "duration": 0.0019834041595458984,
                                                    "steps": {
                                                        "ray_client_call_and_init": {
                                                            "duration": 8.940696716308594e-05,
                                                            "steps": {}
                                                        },
                                                        "ray_client_setModel": {
                                                            "duration": 0.0007050037384033203,
                                                            "steps": {}
                                                        },
                                                        "ray_client_model_to_device": {
                                                            "duration": 0.0001201629638671875,
                                                            "steps": {}
                                                        }
                                                    }
                                                },
                                                "ray_setDataLoader": {
                                                    "duration": 7.653236389160156e-05,
                                                    "steps": {}
                                                },
                                                "ray_setOptimizer": {
                                                    "duration": 7.772445678710938e-05,
                                                    "steps": {}
                                                },
                                                "ray_epochs_loop": {
                                                    "duration": 7.877718210220337,
                                                    "steps": {}
                                                }
                                            }
                                        },
                                        "back_to_head_from_worker": {
                                            "duration": 0.003833770751953125,
                                            "steps": {}
                                        },
                                        "clientporxy_ending": {
                                            "duration": 0.00011730194091796875,
                                            "steps": {}
                                        }
                                    }
                                }
                            }
                        },
                        "aggregate": {
                            "duration": 0.0015571117401123047,
                            "steps": {}
                        },
                        "evaluation (strategy.evaluate)": {
                            "duration": 1.7715232372283936,
                            "steps": {}
                        },
                        "metrics_logging (strategy.evaluate)": {
                            "duration": 0.000148773193359375,
                            "steps": {}
                        },
                        "evaluation (strategy.evaluate_round [distributed])": {
                            "duration": 0.6706101894378662,
                            "steps": {}
                        },
                        "metrics_logging (strategy.evaluate_round [distributed])": {
                            "duration": 5.698204040527344e-05,
                            "steps": {}
                        }
                    }
                },
                "round8": {
                    "duration": 10.440447568893433,
                    "steps": {
                        "configuration": {
                            "duration": 8.177757263183594e-05,
                            "steps": {}
                        },
                        "local_training": {
                            "duration": 7.986159801483154,
                            "clients": {
                                "0": {
                                    "duration": 7.98568320274353,
                                    "steps": {
                                        "msg_passing_from_clientproxy_to_actorpool": {
                                            "duration": 0.0005233287811279297,
                                            "steps": {}
                                        },
                                        "from_head(actorpool)_to_worker": {
                                            "duration": 0.0070095062255859375,
                                            "steps": {}
                                        },
                                        "ray_worker_training": {
                                            "duration": 7.974316596984863,
                                            "steps": {
                                                "ray_load_partition": {
                                                    "duration": 0.001676321029663086,
                                                    "steps": {}
                                                },
                                                "ray_split_transform_dataset": {
                                                    "duration": 0.00397491455078125,
                                                    "steps": {}
                                                },
                                                "ray_client_init_setModel": {
                                                    "duration": 0.0019707679748535156,
                                                    "steps": {
                                                        "ray_client_call_and_init": {
                                                            "duration": 8.940696716308594e-05,
                                                            "steps": {}
                                                        },
                                                        "ray_client_setModel": {
                                                            "duration": 0.0007114410400390625,
                                                            "steps": {}
                                                        },
                                                        "ray_client_model_to_device": {
                                                            "duration": 0.00012063980102539062,
                                                            "steps": {}
                                                        }
                                                    }
                                                },
                                                "ray_setDataLoader": {
                                                    "duration": 7.987022399902344e-05,
                                                    "steps": {}
                                                },
                                                "ray_setOptimizer": {
                                                    "duration": 8.344650268554688e-05,
                                                    "steps": {}
                                                },
                                                "ray_epochs_loop": {
                                                    "duration": 7.966531276702881,
                                                    "steps": {}
                                                }
                                            }
                                        },
                                        "back_to_head_from_worker": {
                                            "duration": 0.0037186145782470703,
                                            "steps": {}
                                        },
                                        "clientporxy_ending": {
                                            "duration": 0.00011515617370605469,
                                            "steps": {}
                                        }
                                    }
                                },
                                "1": {
                                    "duration": 7.964925765991211,
                                    "steps": {
                                        "msg_passing_from_clientproxy_to_actorpool": {
                                            "duration": 0.004411220550537109,
                                            "steps": {}
                                        },
                                        "from_head(actorpool)_to_worker": {
                                            "duration": 0.007483005523681641,
                                            "steps": {}
                                        },
                                        "ray_worker_training": {
                                            "duration": 7.949156284332275,
                                            "steps": {
                                                "ray_load_partition": {
                                                    "duration": 0.0014204978942871094,
                                                    "steps": {}
                                                },
                                                "ray_split_transform_dataset": {
                                                    "duration": 0.003513336181640625,
                                                    "steps": {}
                                                },
                                                "ray_client_init_setModel": {
                                                    "duration": 0.0019137859344482422,
                                                    "steps": {
                                                        "ray_client_call_and_init": {
                                                            "duration": 7.915496826171875e-05,
                                                            "steps": {}
                                                        },
                                                        "ray_client_setModel": {
                                                            "duration": 0.0006656646728515625,
                                                            "steps": {}
                                                        },
                                                        "ray_client_model_to_device": {
                                                            "duration": 0.0001518726348876953,
                                                            "steps": {}
                                                        }
                                                    }
                                                },
                                                "ray_setDataLoader": {
                                                    "duration": 8.082389831542969e-05,
                                                    "steps": {}
                                                },
                                                "ray_setOptimizer": {
                                                    "duration": 7.963180541992188e-05,
                                                    "steps": {}
                                                },
                                                "ray_epochs_loop": {
                                                    "duration": 7.942148208618164,
                                                    "steps": {}
                                                }
                                            }
                                        },
                                        "back_to_head_from_worker": {
                                            "duration": 0.003777742385864258,
                                            "steps": {}
                                        },
                                        "clientporxy_ending": {
                                            "duration": 9.751319885253906e-05,
                                            "steps": {}
                                        }
                                    }
                                }
                            }
                        },
                        "aggregate": {
                            "duration": 0.0015528202056884766,
                            "steps": {}
                        },
                        "evaluation (strategy.evaluate)": {
                            "duration": 1.7728066444396973,
                            "steps": {}
                        },
                        "metrics_logging (strategy.evaluate)": {
                            "duration": 0.00014495849609375,
                            "steps": {}
                        },
                        "evaluation (strategy.evaluate_round [distributed])": {
                            "duration": 0.6795728206634521,
                            "steps": {}
                        },
                        "metrics_logging (strategy.evaluate_round [distributed])": {
                            "duration": 4.267692565917969e-05,
                            "steps": {}
                        }
                    }
                },
                "round9": {
                    "duration": 10.550434350967407,
                    "steps": {
                        "configuration": {
                            "duration": 5.125999450683594e-05,
                            "steps": {}
                        },
                        "local_training": {
                            "duration": 8.094422340393066,
                            "clients": {
                                "0": {
                                    "duration": 7.906556129455566,
                                    "steps": {
                                        "msg_passing_from_clientproxy_to_actorpool": {
                                            "duration": 0.00481867790222168,
                                            "steps": {}
                                        },
                                        "from_head(actorpool)_to_worker": {
                                            "duration": 0.007728099822998047,
                                            "steps": {}
                                        },
                                        "ray_worker_training": {
                                            "duration": 7.890214681625366,
                                            "steps": {
                                                "ray_load_partition": {
                                                    "duration": 0.0014281272888183594,
                                                    "steps": {}
                                                },
                                                "ray_split_transform_dataset": {
                                                    "duration": 0.003536224365234375,
                                                    "steps": {}
                                                },
                                                "ray_client_init_setModel": {
                                                    "duration": 0.0020880699157714844,
                                                    "steps": {
                                                        "ray_client_call_and_init": {
                                                            "duration": 7.82012939453125e-05,
                                                            "steps": {}
                                                        },
                                                        "ray_client_setModel": {
                                                            "duration": 0.0006785392761230469,
                                                            "steps": {}
                                                        },
                                                        "ray_client_model_to_device": {
                                                            "duration": 0.00011920928955078125,
                                                            "steps": {}
                                                        }
                                                    }
                                                },
                                                "ray_setDataLoader": {
                                                    "duration": 8.559226989746094e-05,
                                                    "steps": {}
                                                },
                                                "ray_setOptimizer": {
                                                    "duration": 8.0108642578125e-05,
                                                    "steps": {}
                                                },
                                                "ray_epochs_loop": {
                                                    "duration": 7.882996559143066,
                                                    "steps": {}
                                                }
                                            }
                                        },
                                        "back_to_head_from_worker": {
                                            "duration": 0.003683328628540039,
                                            "steps": {}
                                        },
                                        "clientporxy_ending": {
                                            "duration": 0.00011134147644042969,
                                            "steps": {}
                                        }
                                    }
                                },
                                "1": {
                                    "duration": 8.093960285186768,
                                    "steps": {
                                        "msg_passing_from_clientproxy_to_actorpool": {
                                            "duration": 0.0006380081176757812,
                                            "steps": {}
                                        },
                                        "from_head(actorpool)_to_worker": {
                                            "duration": 0.0072286128997802734,
                                            "steps": {}
                                        },
                                        "ray_worker_training": {
                                            "duration": 8.081718444824219,
                                            "steps": {
                                                "ray_load_partition": {
                                                    "duration": 0.0016856193542480469,
                                                    "steps": {}
                                                },
                                                "ray_split_transform_dataset": {
                                                    "duration": 0.003949642181396484,
                                                    "steps": {}
                                                },
                                                "ray_client_init_setModel": {
                                                    "duration": 0.0020246505737304688,
                                                    "steps": {
                                                        "ray_client_call_and_init": {
                                                            "duration": 9.274482727050781e-05,
                                                            "steps": {}
                                                        },
                                                        "ray_client_setModel": {
                                                            "duration": 0.00070953369140625,
                                                            "steps": {}
                                                        },
                                                        "ray_client_model_to_device": {
                                                            "duration": 0.0001227855682373047,
                                                            "steps": {}
                                                        }
                                                    }
                                                },
                                                "ray_setDataLoader": {
                                                    "duration": 7.963180541992188e-05,
                                                    "steps": {}
                                                },
                                                "ray_setOptimizer": {
                                                    "duration": 8.0108642578125e-05,
                                                    "steps": {}
                                                },
                                                "ray_epochs_loop": {
                                                    "duration": 8.073898792266846,
                                                    "steps": {}
                                                }
                                            }
                                        },
                                        "back_to_head_from_worker": {
                                            "duration": 0.004268646240234375,
                                            "steps": {}
                                        },
                                        "clientporxy_ending": {
                                            "duration": 0.00010657310485839844,
                                            "steps": {}
                                        }
                                    }
                                }
                            }
                        },
                        "aggregate": {
                            "duration": 0.0016965866088867188,
                            "steps": {}
                        },
                        "evaluation (strategy.evaluate)": {
                            "duration": 1.789036750793457,
                            "steps": {}
                        },
                        "metrics_logging (strategy.evaluate)": {
                            "duration": 0.0001480579376220703,
                            "steps": {}
                        },
                        "evaluation (strategy.evaluate_round [distributed])": {
                            "duration": 0.6649136543273926,
                            "steps": {}
                        },
                        "metrics_logging (strategy.evaluate_round [distributed])": {
                            "duration": 6.0558319091796875e-05,
                            "steps": {}
                        }
                    }
                }
            }
        }
    }
}

b = {
    "duration": 195.7807960510254,
    "steps": {
        "server_controller_init": {
            "duration": 4.4467551708221436,
            "steps": {}
        },
        "operator_init(np.save)": {
            "duration": 0.030018329620361328,
            "steps": {}
        },
        "training": {
            "duration": 142.19475269317627,
            "steps": {
                "round1": {
                    "duration": 15.882375240325928,
                    "steps": {
                        "loca_training": {
                            "duration": 10.850158929824829,
                            "steps": {}
                        },
                        "aggregate": {
                            "duration": 0.0018813610076904297,
                            "steps": {}
                        },
                        "evaluation": {
                            "duration": 5.027807712554932,
                            "steps": {}
                        },
                        "metrics_logging": {
                            "duration": 0.002423524856567383,
                            "steps": {}
                        }
                    }
                },
                "round2": {
                    "duration": 15.766690969467163,
                    "steps": {
                        "loca_training": {
                            "duration": 10.769582033157349,
                            "steps": {}
                        },
                        "aggregate": {
                            "duration": 0.0014729499816894531,
                            "steps": {}
                        },
                        "evaluation": {
                            "duration": 4.993768692016602,
                            "steps": {}
                        },
                        "metrics_logging": {
                            "duration": 0.0017690658569335938,
                            "steps": {}
                        }
                    }
                },
                "round3": {
                    "duration": 15.89953327178955,
                    "steps": {
                        "loca_training": {
                            "duration": 10.83247423171997,
                            "steps": {}
                        },
                        "aggregate": {
                            "duration": 0.0014443397521972656,
                            "steps": {}
                        },
                        "evaluation": {
                            "duration": 5.063194274902344,
                            "steps": {}
                        },
                        "metrics_logging": {
                            "duration": 0.0022852420806884766,
                            "steps": {}
                        }
                    }
                },
                "round4": {
                    "duration": 15.68301010131836,
                    "steps": {
                        "loca_training": {
                            "duration": 10.665897846221924,
                            "steps": {}
                        },
                        "aggregate": {
                            "duration": 0.0014622211456298828,
                            "steps": {}
                        },
                        "evaluation": {
                            "duration": 5.013972759246826,
                            "steps": {}
                        },
                        "metrics_logging": {
                            "duration": 0.0015897750854492188,
                            "steps": {}
                        }
                    }
                },
                "round5": {
                    "duration": 15.795335531234741,
                    "steps": {
                        "loca_training": {
                            "duration": 10.770692586898804,
                            "steps": {}
                        },
                        "aggregate": {
                            "duration": 0.0016603469848632812,
                            "steps": {}
                        },
                        "evaluation": {
                            "duration": 5.021063804626465,
                            "steps": {}
                        },
                        "metrics_logging": {
                            "duration": 0.0018312931060791016,
                            "steps": {}
                        }
                    }
                },
                "round6": {
                    "duration": 15.6895592212677,
                    "steps": {
                        "loca_training": {
                            "duration": 10.679847478866577,
                            "steps": {}
                        },
                        "aggregate": {
                            "duration": 0.0016934871673583984,
                            "steps": {}
                        },
                        "evaluation": {
                            "duration": 5.005275726318359,
                            "steps": {}
                        },
                        "metrics_logging": {
                            "duration": 0.0026209354400634766,
                            "steps": {}
                        }
                    }
                },
                "round7": {
                    "duration": 15.866981744766235,
                    "steps": {
                        "loca_training": {
                            "duration": 10.84145474433899,
                            "steps": {}
                        },
                        "aggregate": {
                            "duration": 0.0016012191772460938,
                            "steps": {}
                        },
                        "evaluation": {
                            "duration": 5.0220232009887695,
                            "steps": {}
                        },
                        "metrics_logging": {
                            "duration": 0.0017850399017333984,
                            "steps": {}
                        }
                    }
                },
                "round8": {
                    "duration": 15.796399116516113,
                    "steps": {
                        "loca_training": {
                            "duration": 10.724325180053711,
                            "steps": {}
                        },
                        "aggregate": {
                            "duration": 0.0013275146484375,
                            "steps": {}
                        },
                        "evaluation": {
                            "duration": 5.068702697753906,
                            "steps": {}
                        },
                        "metrics_logging": {
                            "duration": 0.0019409656524658203,
                            "steps": {}
                        }
                    }
                },
                "round9": {
                    "duration": 15.80870509147644,
                    "steps": {
                        "loca_training": {
                            "duration": 10.74228572845459,
                            "steps": {}
                        },
                        "aggregate": {
                            "duration": 0.0017278194427490234,
                            "steps": {}
                        },
                        "evaluation": {
                            "duration": 5.061551094055176,
                            "steps": {}
                        },
                        "metrics_logging": {
                            "duration": 0.0030014514923095703,
                            "steps": {}
                        }
                    }
                }
            }
        }
    }
}

c = {
    "duration": 194.36742496490479,
    "steps": {
        "ce_server_init": {
            "duration": 0.4037048816680908,
            "steps": {}
        },
        "msg_handing": {
            "duration": -1,
            "messages": {
                "round1_02904357ccf9409d975a351f9ea3c297_training": {
                    "duration": 9.706549167633057,
                    "steps": {
                        "decode_msg": {
                            "duration": 0.0002472400665283203,
                            "details": {}
                        },
                        "ce_initiate_er": {
                            "duration": 0.0002484321594238281,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 1.6416716575622559,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0.15126967430114746,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0.0467066764831543,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 1.0984899997711182,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0.00013327598571777344,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 5.107161045074463,
                            "details": {}
                        },
                        "ray_evaluate": {
                            "duration": 1.6525294780731201,
                            "details": {}
                        },
                        "ray_session_reporting": {
                            "duration": 0.00029754638671875,
                            "details": {}
                        },
                        "ray_model_saving": {
                            "duration": 0.0013055801391601562,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 0.00402069091796875,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0.0024678707122802734,
                            "details": {}
                        }
                    }
                },
                "round1_02904357ccf9409d975a351f9ea3c297_evaluating": {
                    "duration": 0,
                    "steps": {
                        "ce_initiate_er": {
                            "duration": 0,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 0,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 0,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0,
                            "details": {}
                        }
                    }
                },
                "round2_02904357ccf9409d975a351f9ea3c297_training": {
                    "duration": 9.660969018936157,
                    "steps": {
                        "decode_msg": {
                            "duration": 0.0002689361572265625,
                            "details": {}
                        },
                        "ce_initiate_er": {
                            "duration": 0.00028395652770996094,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 1.6577305793762207,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0.14322900772094727,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0.047248125076293945,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 1.0966145992279053,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0.0001533031463623047,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 5.100253343582153,
                            "details": {}
                        },
                        "ray_evaluate": {
                            "duration": 1.6086068153381348,
                            "details": {}
                        },
                        "ray_session_reporting": {
                            "duration": 0.00021576881408691406,
                            "details": {}
                        },
                        "ray_model_saving": {
                            "duration": 0.001004934310913086,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 0.0031599998474121094,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0.0021996498107910156,
                            "details": {}
                        }
                    }
                },
                "round2_02904357ccf9409d975a351f9ea3c297_evaluating": {
                    "duration": 0,
                    "steps": {
                        "ce_initiate_er": {
                            "duration": 0,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 0,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 0,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0,
                            "details": {}
                        }
                    }
                },
                "round3_02904357ccf9409d975a351f9ea3c297_training": {
                    "duration": 9.685831069946289,
                    "steps": {
                        "decode_msg": {
                            "duration": 0.00016808509826660156,
                            "details": {}
                        },
                        "ce_initiate_er": {
                            "duration": 0.00042319297790527344,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 1.7179982662200928,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0.13841795921325684,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0.04662466049194336,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 1.070554494857788,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0.00016927719116210938,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 5.032532215118408,
                            "details": {}
                        },
                        "ray_evaluate": {
                            "duration": 1.6716794967651367,
                            "details": {}
                        },
                        "ray_session_reporting": {
                            "duration": 0.00020313262939453125,
                            "details": {}
                        },
                        "ray_model_saving": {
                            "duration": 0.000978708267211914,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 0.003232717514038086,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0.0028488636016845703,
                            "details": {}
                        }
                    }
                },
                "round3_02904357ccf9409d975a351f9ea3c297_evaluating": {
                    "duration": 0,
                    "steps": {
                        "ce_initiate_er": {
                            "duration": 0,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 0,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 0,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0,
                            "details": {}
                        }
                    }
                },
                "round4_02904357ccf9409d975a351f9ea3c297_training": {
                    "duration": 9.68561840057373,
                    "steps": {
                        "decode_msg": {
                            "duration": 0.0003902912139892578,
                            "details": {}
                        },
                        "ce_initiate_er": {
                            "duration": 0.0004172325134277344,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 1.6427395343780518,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0.14207911491394043,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0.047675132751464844,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 1.0829994678497314,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0.0001571178436279297,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 5.112838983535767,
                            "details": {}
                        },
                        "ray_evaluate": {
                            "duration": 1.6498808860778809,
                            "details": {}
                        },
                        "ray_session_reporting": {
                            "duration": 0.00021529197692871094,
                            "details": {}
                        },
                        "ray_model_saving": {
                            "duration": 0.00098419189453125,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 0.003049612045288086,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0.0021915435791015625,
                            "details": {}
                        }
                    }
                },
                "round4_02904357ccf9409d975a351f9ea3c297_evaluating": {
                    "duration": 0,
                    "steps": {
                        "ce_initiate_er": {
                            "duration": 0,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 0,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 0,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0,
                            "details": {}
                        }
                    }
                },
                "round5_02904357ccf9409d975a351f9ea3c297_training": {
                    "duration": 9.584167957305908,
                    "steps": {
                        "decode_msg": {
                            "duration": 0.0002465248107910156,
                            "details": {}
                        },
                        "ce_initiate_er": {
                            "duration": 0.00021886825561523438,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 1.690796136856079,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0.13919687271118164,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0.046181440353393555,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 1.077683925628662,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0.00016045570373535156,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 5.006007671356201,
                            "details": {}
                        },
                        "ray_evaluate": {
                            "duration": 1.6171255111694336,
                            "details": {}
                        },
                        "ray_session_reporting": {
                            "duration": 0.00021028518676757812,
                            "details": {}
                        },
                        "ray_model_saving": {
                            "duration": 0.0010251998901367188,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 0.0031583309173583984,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0.0021567344665527344,
                            "details": {}
                        }
                    }
                },
                "round5_02904357ccf9409d975a351f9ea3c297_evaluating": {
                    "duration": 0,
                    "steps": {
                        "ce_initiate_er": {
                            "duration": 0,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 0,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 0,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0,
                            "details": {}
                        }
                    }
                },
                "round6_02904357ccf9409d975a351f9ea3c297_training": {
                    "duration": 9.608877420425415,
                    "steps": {
                        "decode_msg": {
                            "duration": 0.0002658367156982422,
                            "details": {}
                        },
                        "ce_initiate_er": {
                            "duration": 0.0002086162567138672,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 1.6730906963348389,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0.14164257049560547,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0.047824859619140625,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 1.0792450904846191,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0.00017833709716796875,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 5.029221773147583,
                            "details": {}
                        },
                        "ray_evaluate": {
                            "duration": 1.6300809383392334,
                            "details": {}
                        },
                        "ray_session_reporting": {
                            "duration": 0.0002129077911376953,
                            "details": {}
                        },
                        "ray_model_saving": {
                            "duration": 0.0009763240814208984,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 0.0030663013458251953,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0.002863168716430664,
                            "details": {}
                        }
                    }
                },
                "round6_02904357ccf9409d975a351f9ea3c297_evaluating": {
                    "duration": 0,
                    "steps": {
                        "ce_initiate_er": {
                            "duration": 0,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 0,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 0,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0,
                            "details": {}
                        }
                    }
                },
                "round7_02904357ccf9409d975a351f9ea3c297_training": {
                    "duration": 9.743195056915283,
                    "steps": {
                        "decode_msg": {
                            "duration": 0.000347137451171875,
                            "details": {}
                        },
                        "ce_initiate_er": {
                            "duration": 0.00036716461181640625,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 1.6751103401184082,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0.14297103881835938,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0.04712486267089844,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 1.0967051982879639,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0.0001621246337890625,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 5.082301378250122,
                            "details": {}
                        },
                        "ray_evaluate": {
                            "duration": 1.6915748119354248,
                            "details": {}
                        },
                        "ray_session_reporting": {
                            "duration": 0.00021386146545410156,
                            "details": {}
                        },
                        "ray_model_saving": {
                            "duration": 0.000986337661743164,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 0.0030922889709472656,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0.0022385120391845703,
                            "details": {}
                        }
                    }
                },
                "round7_02904357ccf9409d975a351f9ea3c297_evaluating": {
                    "duration": 0,
                    "steps": {
                        "ce_initiate_er": {
                            "duration": 0,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 0,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 0,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0,
                            "details": {}
                        }
                    }
                },
                "round8_02904357ccf9409d975a351f9ea3c297_training": {
                    "duration": 9.515390634536743,
                    "steps": {
                        "decode_msg": {
                            "duration": 0.00023698806762695312,
                            "details": {}
                        },
                        "ce_initiate_er": {
                            "duration": 0.00022864341735839844,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 1.6484689712524414,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0.1408693790435791,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0.046801090240478516,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 1.0852670669555664,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0.0001537799835205078,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 4.968348503112793,
                            "details": {}
                        },
                        "ray_evaluate": {
                            "duration": 1.618480920791626,
                            "details": {}
                        },
                        "ray_session_reporting": {
                            "duration": 0.0002079010009765625,
                            "details": {}
                        },
                        "ray_model_saving": {
                            "duration": 0.0009920597076416016,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 0.003111124038696289,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0.0022242069244384766,
                            "details": {}
                        }
                    }
                },
                "round8_02904357ccf9409d975a351f9ea3c297_evaluating": {
                    "duration": 0,
                    "steps": {
                        "ce_initiate_er": {
                            "duration": 0,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 0,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 0,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0,
                            "details": {}
                        }
                    }
                },
                "round9_02904357ccf9409d975a351f9ea3c297_training": {
                    "duration": 9.597901582717896,
                    "steps": {
                        "decode_msg": {
                            "duration": 0.0009605884552001953,
                            "details": {}
                        },
                        "ce_initiate_er": {
                            "duration": 0.0007712841033935547,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 1.6756949424743652,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0.13894271850585938,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0.047801971435546875,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 1.0696704387664795,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0.00019478797912597656,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 5.050553798675537,
                            "details": {}
                        },
                        "ray_evaluate": {
                            "duration": 1.6068003177642822,
                            "details": {}
                        },
                        "ray_session_reporting": {
                            "duration": 0.00020074844360351562,
                            "details": {}
                        },
                        "ray_model_saving": {
                            "duration": 0.0010104179382324219,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 0.0030472278594970703,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0.002252340316772461,
                            "details": {}
                        }
                    }
                },
                "round9_02904357ccf9409d975a351f9ea3c297_evaluating": {
                    "duration": 0,
                    "steps": {
                        "ce_initiate_er": {
                            "duration": 0,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 0,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 0,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0,
                            "details": {}
                        }
                    }
                },
                "round1_4e33bde1f81d434ea4a80531c91b2d6b_training": {
                    "duration": 10.843888759613037,
                    "steps": {
                        "decode_msg": {
                            "duration": 0.0018835067749023438,
                            "details": {}
                        },
                        "ce_initiate_er": {
                            "duration": 0.00016927719116210938,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 1.6347041130065918,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0.146378755569458,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0.04683709144592285,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 1.103898048400879,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0.00016498565673828125,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 6.266633987426758,
                            "details": {}
                        },
                        "ray_evaluate": {
                            "duration": 1.6368296146392822,
                            "details": {}
                        },
                        "ray_session_reporting": {
                            "duration": 0.00020694732666015625,
                            "details": {}
                        },
                        "ray_model_saving": {
                            "duration": 0.0009846687316894531,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 0.0031082630157470703,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0.0020895004272460938,
                            "details": {}
                        }
                    }
                },
                "round1_4e33bde1f81d434ea4a80531c91b2d6b_evaluating": {
                    "duration": 5.025203227996826,
                    "steps": {
                        "ce_initiate_er": {
                            "duration": 0.00022840499877929688,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 1.6405982971191406,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0.13188481330871582,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0.044757843017578125,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 0.9973938465118408,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0.00015044212341308594,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 2.2042694091796875,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 1722777447.3469913,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0.002245187759399414,
                            "details": {}
                        }
                    }
                },
                "round2_4e33bde1f81d434ea4a80531c91b2d6b_training": {
                    "duration": 10.764718532562256,
                    "steps": {
                        "decode_msg": {
                            "duration": 0.0011823177337646484,
                            "details": {}
                        },
                        "ce_initiate_er": {
                            "duration": 0.00043487548828125,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 1.6567656993865967,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0.14798212051391602,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0.04766345024108887,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 1.0973024368286133,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0.00015664100646972656,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 6.166927337646484,
                            "details": {}
                        },
                        "ray_evaluate": {
                            "duration": 1.6397135257720947,
                            "details": {}
                        },
                        "ray_session_reporting": {
                            "duration": 0.000202178955078125,
                            "details": {}
                        },
                        "ray_model_saving": {
                            "duration": 0.0009794235229492188,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 0.003126382827758789,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0.0022821426391601562,
                            "details": {}
                        }
                    }
                },
                "round2_4e33bde1f81d434ea4a80531c91b2d6b_evaluating": {
                    "duration": 4.991360902786255,
                    "steps": {
                        "ce_initiate_er": {
                            "duration": 0.0002510547637939453,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 1.6287379264831543,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0.1336507797241211,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0.04497075080871582,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 1.0018062591552734,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0.0001571178436279297,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 2.1756021976470947,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 1722777463.114409,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0.0023708343505859375,
                            "details": {}
                        }
                    }
                },
                "round3_4e33bde1f81d434ea4a80531c91b2d6b_training": {
                    "duration": 10.829330921173096,
                    "steps": {
                        "decode_msg": {
                            "duration": 0.00022602081298828125,
                            "details": {}
                        },
                        "ce_initiate_er": {
                            "duration": 0.00034618377685546875,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 1.6952645778656006,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0.14118075370788574,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0.04647374153137207,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 1.1089587211608887,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0.0001583099365234375,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 6.237665891647339,
                            "details": {}
                        },
                        "ray_evaluate": {
                            "duration": 1.5926792621612549,
                            "details": {}
                        },
                        "ray_session_reporting": {
                            "duration": 0.0002448558807373047,
                            "details": {}
                        },
                        "ray_model_saving": {
                            "duration": 0.0009834766387939453,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 0.002994537353515625,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0.0021545886993408203,
                            "details": {}
                        }
                    }
                },
                "round3_4e33bde1f81d434ea4a80531c91b2d6b_evaluating": {
                    "duration": 5.0171449184417725,
                    "steps": {
                        "ce_initiate_er": {
                            "duration": 0.0002961158752441406,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 1.6236956119537354,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0.1347954273223877,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0.04445695877075195,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 1.0068860054016113,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0.00015497207641601562,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 2.2002997398376465,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 1722777478.969294,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0.0029134750366210938,
                            "details": {}
                        }
                    }
                },
                "round4_4e33bde1f81d434ea4a80531c91b2d6b_training": {
                    "duration": 10.656028985977173,
                    "steps": {
                        "decode_msg": {
                            "duration": 0.0006549358367919922,
                            "details": {}
                        },
                        "ce_initiate_er": {
                            "duration": 0.0008466243743896484,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 1.6392278671264648,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0.14606308937072754,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0.04886770248413086,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 1.070810317993164,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0.0001652240753173828,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 6.178966283798218,
                            "details": {}
                        },
                        "ray_evaluate": {
                            "duration": 1.5632524490356445,
                            "details": {}
                        },
                        "ray_session_reporting": {
                            "duration": 0.00020384788513183594,
                            "details": {}
                        },
                        "ray_model_saving": {
                            "duration": 0.0009715557098388672,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 0.0037937164306640625,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0.002205371856689453,
                            "details": {}
                        }
                    }
                },
                "round4_4e33bde1f81d434ea4a80531c91b2d6b_evaluating": {
                    "duration": 5.011563062667847,
                    "steps": {
                        "ce_initiate_er": {
                            "duration": 0.0003039836883544922,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 1.6141026020050049,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0.1339876651763916,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0.04558086395263672,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 1.0010170936584473,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0.00015592575073242188,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 2.210195779800415,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 1722777494.6975217,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0.002370119094848633,
                            "details": {}
                        }
                    }
                },
                "round5_4e33bde1f81d434ea4a80531c91b2d6b_training": {
                    "duration": 10.766320705413818,
                    "steps": {
                        "decode_msg": {
                            "duration": 0.0002238750457763672,
                            "details": {}
                        },
                        "ce_initiate_er": {
                            "duration": 0.00042176246643066406,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 1.7008888721466064,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0.14086151123046875,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0.04752612113952637,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 1.0916450023651123,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0.00018095970153808594,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 6.16576361656189,
                            "details": {}
                        },
                        "ray_evaluate": {
                            "duration": 1.6123435497283936,
                            "details": {}
                        },
                        "ray_session_reporting": {
                            "duration": 0.0002014636993408203,
                            "details": {}
                        },
                        "ray_model_saving": {
                            "duration": 0.0009520053863525391,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 0.0031261444091796875,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0.002185821533203125,
                            "details": {}
                        }
                    }
                },
                "round5_4e33bde1f81d434ea4a80531c91b2d6b_evaluating": {
                    "duration": 5.018723011016846,
                    "steps": {
                        "ce_initiate_er": {
                            "duration": 0.0002200603485107422,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 1.6022837162017822,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0.131209135055542,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0.045426130294799805,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 1.0193181037902832,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0.00015687942504882812,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 2.2141921520233154,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 1722777510.4928658,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0.0021452903747558594,
                            "details": {}
                        }
                    }
                },
                "round6_4e33bde1f81d434ea4a80531c91b2d6b_training": {
                    "duration": 10.67540955543518,
                    "steps": {
                        "decode_msg": {
                            "duration": 0.0002837181091308594,
                            "details": {}
                        },
                        "ce_initiate_er": {
                            "duration": 0.0009601116180419922,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 1.6657681465148926,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0.13962435722351074,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0.047928810119628906,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 1.066298007965088,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0.00015974044799804688,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 6.16437840461731,
                            "details": {}
                        },
                        "ray_evaluate": {
                            "duration": 1.5835001468658447,
                            "details": {}
                        },
                        "ray_session_reporting": {
                            "duration": 0.00021195411682128906,
                            "details": {}
                        },
                        "ray_model_saving": {
                            "duration": 0.000985860824584961,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 0.003083467483520508,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0.0022268295288085938,
                            "details": {}
                        }
                    }
                },
                "round6_4e33bde1f81d434ea4a80531c91b2d6b_evaluating": {
                    "duration": 4.956663608551025,
                    "steps": {
                        "ce_initiate_er": {
                            "duration": 0.00020456314086914062,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 1.6049630641937256,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0.13283181190490723,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0.045049428939819336,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 1.0031459331512451,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0.0001552104949951172,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 2.1643292903900146,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 1722777526.135424,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0.0022389888763427734,
                            "details": {}
                        }
                    }
                },
                "round7_4e33bde1f81d434ea4a80531c91b2d6b_training": {
                    "duration": 10.835907936096191,
                    "steps": {
                        "decode_msg": {
                            "duration": 0.002121448516845703,
                            "details": {}
                        },
                        "ce_initiate_er": {
                            "duration": 0.0005159378051757812,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 1.6714396476745605,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0.15243291854858398,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0.04942655563354492,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 1.113250494003296,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0.00017452239990234375,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 6.204060077667236,
                            "details": {}
                        },
                        "ray_evaluate": {
                            "duration": 1.6360890865325928,
                            "details": {}
                        },
                        "ray_session_reporting": {
                            "duration": 0.00021505355834960938,
                            "details": {}
                        },
                        "ray_model_saving": {
                            "duration": 0.000997781753540039,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 0.003118753433227539,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0.0020656585693359375,
                            "details": {}
                        }
                    }
                },
                "round7_4e33bde1f81d434ea4a80531c91b2d6b_evaluating": {
                    "duration": 5.019585609436035,
                    "steps": {
                        "ce_initiate_er": {
                            "duration": 0.00023889541625976562,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 1.612839937210083,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0.13282012939453125,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0.04465603828430176,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 1.0212554931640625,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0.00015687942504882812,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 2.2014682292938232,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 1722777542.0495696,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0.0022704601287841797,
                            "details": {}
                        }
                    }
                },
                "round8_4e33bde1f81d434ea4a80531c91b2d6b_training": {
                    "duration": 10.719990253448486,
                    "steps": {
                        "decode_msg": {
                            "duration": 0.001127004623413086,
                            "details": {}
                        },
                        "ce_initiate_er": {
                            "duration": 0.0002472400665283203,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 1.6471195220947266,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0.1459653377532959,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0.05658602714538574,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 1.0745182037353516,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0.00016307830810546875,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 6.196218252182007,
                            "details": {}
                        },
                        "ray_evaluate": {
                            "duration": 1.5915789604187012,
                            "details": {}
                        },
                        "ray_session_reporting": {
                            "duration": 0.0002040863037109375,
                            "details": {}
                        },
                        "ray_model_saving": {
                            "duration": 0.0010349750518798828,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 0.0030672550201416016,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0.002160310745239258,
                            "details": {}
                        }
                    }
                },
                "round8_4e33bde1f81d434ea4a80531c91b2d6b_evaluating": {
                    "duration": 5.066271066665649,
                    "steps": {
                        "ce_initiate_er": {
                            "duration": 0.00021648406982421875,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 1.632591962814331,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0.13232111930847168,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0.045035362243652344,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 1.0207653045654297,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0.00015783309936523438,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 2.2285428047180176,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 1722777557.8450818,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0.0029532909393310547,
                            "details": {}
                        }
                    }
                },
                "round9_4e33bde1f81d434ea4a80531c91b2d6b_training": {
                    "duration": 10.738960027694702,
                    "steps": {
                        "decode_msg": {
                            "duration": 0.0002980232238769531,
                            "details": {}
                        },
                        "ce_initiate_er": {
                            "duration": 0.00030612945556640625,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 1.6630902290344238,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0.13900423049926758,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0.04718923568725586,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 1.0922863483428955,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0.00016069412231445312,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 6.165191411972046,
                            "details": {}
                        },
                        "ray_evaluate": {
                            "duration": 1.6249756813049316,
                            "details": {}
                        },
                        "ray_session_reporting": {
                            "duration": 0.00020241737365722656,
                            "details": {}
                        },
                        "ray_model_saving": {
                            "duration": 0.0009884834289550781,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 0.003089427947998047,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0.002177715301513672,
                            "details": {}
                        }
                    }
                },
                "round9_4e33bde1f81d434ea4a80531c91b2d6b_evaluating": {
                    "duration": 5.0175089836120605,
                    "steps": {
                        "ce_initiate_er": {
                            "duration": 0.00027942657470703125,
                            "details": {}
                        },
                        "distributing_to_ray_worker": {
                            "duration": 1.6079943180084229,
                            "details": {}
                        },
                        "ray_hyperparams_init": {
                            "duration": 0.13624119758605957,
                            "details": {}
                        },
                        "ray_setDataLoader": {
                            "duration": 0.04544425010681152,
                            "details": {}
                        },
                        "ray_setModel": {
                            "duration": 1.0169153213500977,
                            "details": {}
                        },
                        "ray_create_model_dir": {
                            "duration": 0.00015997886657714844,
                            "details": {}
                        },
                        "ray_epochs_loop": {
                            "duration": 2.2045958042144775,
                            "details": {}
                        },
                        "back_to_head_from_worker": {
                            "duration": 1722777573.6122284,
                            "details": {}
                        },
                        "encode_msg": {
                            "duration": 0.002178668975830078,
                            "details": {}
                        }
                    }
                }
            }
        }
    }
}