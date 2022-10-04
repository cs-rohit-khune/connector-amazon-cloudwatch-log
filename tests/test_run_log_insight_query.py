import importlib
import json

from .data import *
conn_package = importlib.import_module("aws-cloudwatch-logs.operations")


def test_run_log_insight_query():
    resp = conn_package.run_log_insight_query(config, run_log_insight_query_params)
    print(json.dumps(resp, indent=2))