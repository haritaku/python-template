"""ファイルの入出力を行うためのモジュール

対応するデータ形式は以下。

- json
- yaml
- pickle

"""

import json
import pickle
from collections import OrderedDict
from pathlib import Path
from typing import Any

import yaml

ENCODING = "utf-8"


def load_json(fpath: Path, encoding: str = ENCODING) -> dict:
    """json形式のファイルの読み込む。

    Args:
        fpath: 読み込むファイルパス。
        encoding: エンコーディング。デフォルトはutf-8。

    Returns:
        json_dict: 読み込んだdict形式の変数
    """
    with open(fpath, "r", encoding=encoding) as f:
        json_dict = json.load(f)
    return json_dict


def dump_json(data: Any, fpath: Path, encoding: str = ENCODING) -> None:
    """データを指定されたパスにjson形式で保存する。

    Args:
        data: 保存するデータ。
        fpath: 保存するファイルパス。
        encoding: エンコーディング。デフォルトはutf-8。
    """
    with open(fpath, "w", encoding=encoding) as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_yaml(fpath: Path, encoding: str = ENCODING) -> dict:
    """yaml形式のファイルの読み込む。

    Args:
        fpath: 読み込むファイルパス
        encoding: エンコーディング。デフォルトはutf-8。

    Returns:
        yaml_dict: 読み込んだdict形式の変数。
    """
    with open(fpath, "r", encoding=encoding) as f:
        yaml_dict = yaml.load(f, Loader=yaml.SafeLoader)
    return yaml_dict


def dump_yaml(data: Any, fpath: Path, encoding: str = ENCODING) -> None:
    """データを指定されたパスにyaml形式で保存する。

    Args:
        data: 保存するデータ。
        fpath: 保存するファイルパス。
        encoding: エンコーディング。デフォルトはutf-8。
    """

    def _represent_odict(dumper, instance):
        """辞書の順番を保存するための設定"""
        return dumper.represent_mapping("tag:yaml.org,2002:map", instance.items())

    yaml.add_representer(OrderedDict, _represent_odict)
    with open(fpath, "w", encoding=encoding) as f:
        yaml.dump(data, f, allow_unicode=True)


def load_pickle(fpath: Path, encoding: str = ENCODING) -> Any:
    """pickle形式のファイルの読み込む。

    Args:
        fpath: 読み込むファイルパス
        encoding: エンコーディング。デフォルトはutf-8。

    Returns:
        data: 読み込んだ変数。
    """
    with open(fpath, "rb", encoding=encoding) as f:
        data = pickle.load(f)
    return data


def dump_pickle(data: Any, fpath: Path, encoding: str = ENCODING) -> None:
    """データを指定されたパスにpickle形式で保存する。

    Args:
        data: 保存するデータ。
        fpath: 保存するファイルパス。
        encoding: エンコーディング。デフォルトはutf-8。
    """
    with open(fpath, "wb", encoding=encoding) as f:
        pickle.dump(data, f)
