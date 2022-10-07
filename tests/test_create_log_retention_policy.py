import importlib
import json

from .data import *

conn_package = importlib.import_module("aws-cloudwatch-log.operations")


def test_create_log_retention_policy():
    resp = conn_package.create_log_retention_policy(config, create_log_retention_policy_params)
    print(json.dumps(resp, indent=2))
