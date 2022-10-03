import importlib
import json

from .data import *
conn_package = importlib.import_module("aws-cloudwatch-logs.operations")


def test_delete_log_retention_policy():
    resp = conn_package.delete_log_retention_policy(config, delete_log_retention_policy_params)
    print(json.dumps(resp, indent=2))