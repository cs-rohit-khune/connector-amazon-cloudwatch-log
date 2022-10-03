import importlib
from .data import *
conn_package = importlib.import_module("aws-cloudwatch-logs.operations")


def test_get_list_log_groups():
    resp = conn_package.get_list_log_groups(config, get_list_log_groups_params)
    print(resp)