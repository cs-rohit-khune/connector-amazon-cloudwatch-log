import importlib
import json

from .data import *

conn_package = importlib.import_module("aws-cloudwatch-log.operations")


def test_delete_log_group():
    resp = conn_package.delete_log_group(config, delete_log_group_params)
    print(json.dumps(resp, indent=2))
