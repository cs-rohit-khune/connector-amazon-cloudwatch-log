import importlib
from .data import *
conn_package = importlib.import_module("aws-cloudwatch-logs.operations")


def test_create_log_group():
    resp = conn_package.create_log_group(config, create_log_group_params)
    print(resp)