import os
import logging

log_file_creater = lambda otype: "{}_time_log.txt".format(otype)

def get_time_log_folder_path():
    script_running_path = os.path.abspath(os.getcwd())
    time_log_folder_path = os.path.join(script_running_path, "time_log")
    if not os.path.exists(time_log_folder_path):
        os.makedirs(time_log_folder_path)
    return time_log_folder_path

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
time_log_path = os.path.join(get_time_log_folder_path(), log_file_creater(otype))
flwrsim_logger = create_logger(otype, time_log_path)
