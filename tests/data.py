import time

config = {
    "config_type": "Access Credentials",
    "aws_region": "us-east-2",
    "aws_access_key": "XXXXXXXXXXXXXXXXXXXXXX",
    "aws_secret_access_key": "XXXXXXXXXXXXXXXXXXXXXXXXXX"
}

create_log_group_params = {
    "logGroupName": "test-intg-12345"
}

get_list_log_groups_params = {}

create_log_stream_params = {
    "logGroupName": "test-intg-12345",
    "logStreamName": "test-intg-sream-12345"
}

get_list_log_streams_params = {
    "logGroupName": "test-intg-12345"
}

get_log_events_params = {
    "logGroupName": "test-intg-12345",
    "logStreamName": "test-intg-sream-12345"
}

delete_log_group_params = {
    "logGroupName": "test-intg-12345"
}

delete_log_stream_params = {
    "logGroupName": "test-intg-12345",
    "logStreamName": "test-intg-sream-12345"
}

create_log_retention_policy_params = {
    "logGroupName": "test-intg-12345",
    "retentionInDays": "1 Day"
}

delete_log_retention_policy_params = {
    "logGroupName": "test-intg-12345"
}

upload_log_event_params = {
    "logGroupName": "test-intg-12345",
    "logStreamName": "test-intg-sream-12345",
    "timestamp": 1633890600807,
    "message": "Test-upload"
}

run_log_insight_query_params = {
    "logGroupNames": ["test-intg-12345"],
    "startTime": int(time.time()),
    "endTime": int(time.time()),
    "queryString": "@timestamp"
}

get_log_insight_query_result_params = {
    "queryId": "5f500fe4-cec1-4d65-94f2-442740f02e36"
}

stop_log_insight_query_params = {
    "queryId": "5f500fe4-cec1-4d65-94f2-442740f02e36"
}
