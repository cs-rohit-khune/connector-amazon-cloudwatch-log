import importlib
import json

from .data import *
conn_package = importlib.import_module("aws-cloudwatch-logs.operations")


def test_get_log_insight_query_result():
    resp = conn_package.get_log_insight_query_result(config, get_log_insight_query_result_params)
    print(json.dumps(resp, indent=2))
