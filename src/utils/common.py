import inspect
import logging.config
from pathlib import Path

from src import LOGS_PATH, ROOT_PATH

from .io import load_yaml


def set_log_cfg():
    fpath_log_cfg = ROOT_PATH / "logging_cfg.yml"
    caller_stem = Path(inspect.stack()[1].filename).stem
    log_cfgs = load_yaml(fpath_log_cfg)
    log_cfgs["handlers"]["TimedRotatingFileHandler"]["filename"] = LOGS_PATH / (
        caller_stem + ".log"
    )
    logging.config.dictConfig(log_cfgs)
