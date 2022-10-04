import importlib
import json

from .data import *
conn_package = importlib.import_module("aws-cloudwatch-logs.operations")


def test_get_list_log_streams():
    resp = conn_package.get_list_log_streams(config, get_list_log_streams_params)
    print(json.dumps(resp, indent=2))