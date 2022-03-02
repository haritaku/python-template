"""共通のモジュール."""

import inspect
import logging.config
import subprocess
from pathlib import Path

from src import LOGS_PATH, ROOT_PATH

from .io import load_yaml


def set_log():
    r"""loggingの設定。

    リポジトリのルートに存在するlogging_cfg.ymlからloggingの設定を読み込み反映する。\n
    logファイルはrepository_root/logsに保存され、(呼び出し元のファイル名).logというファイル名で保存される。

    Examples:
        logを使用するスクリプト内に以下を記述する。

        .. code-block:: python

            from logging import getLogger

            from src.utils.common import set_log

            set_log()
            logger = getLogger()  # 個別の設定を使う場合は、getLogger('other config')とする。
            logger.info('test')

    """
    fpath_log_cfg = ROOT_PATH / "logging_cfg.yml"
    caller_stem = Path(inspect.stack()[1].filename).stem
    log_dpath = LOGS_PATH / caller_stem
    log_dpath.mkdir(exist_ok=True)
    git_hash = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).decode().strip()

    log_cfgs = load_yaml(fpath_log_cfg)
    log_cfgs["handlers"]["TimedRotatingFileHandler"]["filename"] = log_dpath / (caller_stem + ".log")
    log_cfgs["formatters"]["default_formatter"]["format"] = log_cfgs["formatters"]["default_formatter"][
        "format"
    ].format(git_hash)

    logging.config.dictConfig(log_cfgs)
