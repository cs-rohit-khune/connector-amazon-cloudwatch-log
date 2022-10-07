import importlib
import json

from .data import *

conn_package = importlib.import_module("aws-cloudwatch-log.operations")


def test_get_log_events():
    resp = conn_package.get_log_events(config, get_log_events_params)
    print(json.dumps(resp, indent=2))
