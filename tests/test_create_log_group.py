import importlib
import json

from .data import *

conn_package = importlib.import_module("aws-cloudwatch-log.operations")


def test_create_log_group():
    resp = conn_package.create_log_group(config, create_log_group_params)
    print()
    print(json.dumps(resp, indent=2))
