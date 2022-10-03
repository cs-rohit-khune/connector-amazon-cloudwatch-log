import importlib
from .data import *
conn_package = importlib.import_module("aws-cloudwatch-logs.operations")


def test_delete_log_group():
    resp = conn_package.delete_log_group(config, delete_log_group_params)
    print(resp)