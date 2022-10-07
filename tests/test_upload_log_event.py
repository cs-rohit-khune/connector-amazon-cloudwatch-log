import importlib
import json

from .data import *

conn_package = importlib.import_module("aws-cloudwatch-log.operations")


def test_upload_log_event():
    resp = conn_package.upload_log_event(config, upload_log_event_params)
    print(json.dumps(resp, indent=2))
