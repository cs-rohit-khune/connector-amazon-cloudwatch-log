import importlib
import json

from .data import *

conn_package = importlib.import_module("aws-cloudwatch-log.operations")


def test_get_list_log_groups():
    resp = conn_package.get_list_log_groups(config, get_list_log_groups_params)
    print(json.dumps(resp, indent=2))
