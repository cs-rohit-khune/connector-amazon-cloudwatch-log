import importlib
from .data import *
conn_package = importlib.import_module("aws-cloudwatch-logs.operations")


def test_check_health():
    resp = conn_package.check_health(config)
    print(resp)