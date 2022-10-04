import importlib
import json

from .data import *
conn_package = importlib.import_module("aws-cloudwatch-logs.operations")


def test_stop_log_insight_query():
    resp = conn_package.stop_log_insight_query(config, stop_log_insight_query_params)
    print(json.dumps(resp, indent=2))