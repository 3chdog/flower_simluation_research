from os.path import join as os_path_join
import logging

time_log_folder = "/home/jack/jacklab/flowerHome/flowerTest_flwr17/simulation-pytorch-resnet50/time_log"
log_file_creater = lambda otype: "{}_time_log.txt".format(otype)

def create_logger(otype: str, time_log_path: str):
    logger = logging.getLogger(otype)
    logger.setLevel(logging.DEBUG)

    ch = logging.FileHandler(time_log_path)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('{} | %(levelname)s | %(module)s:%(lineno)d | %(message)s '.format(otype.upper()))
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

otype = "flwrsim"
time_log_path = os_path_join(time_log_folder, log_file_creater(otype))
flwrsim_logger = create_logger(otype, time_log_path)
