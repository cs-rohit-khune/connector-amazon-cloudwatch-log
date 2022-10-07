import importlib
from .data import *

conn_package = importlib.import_module("aws-cloudwatch-log.operations")


def test_delete_log_stream():
    resp = conn_package.delete_log_stream(config, delete_log_stream_params)
    print(resp)
