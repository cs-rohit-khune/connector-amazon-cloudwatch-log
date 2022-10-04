import time

config = {
    "config_type": "Access Credentials",
    "aws_region": "us-east-2",
    "aws_access_key": "XXXXXXXXXXXXXXXXXXXXXX",
    "aws_secret_access_key": "XXXXXXXXXXXXXXXXXXXXXXXXXX"
}

create_log_group_params = {
    "logGroupName": "test-intg-1234"
}

get_list_log_groups_params = {}

create_log_stream_params = {
    "logGroupName": "test-intg-1234",
    "logStreamName": "test-intg-sream-1234"
}

get_list_log_streams_params = {
    "logGroupName": "test-intg-1234"
}

get_log_events_params = {
    "logGroupName": "test-intg-1234",
    "logStreamName": "test-intg-sream-1234"
}

delete_log_group_params = {
    "logGroupName": "test-intg-1234"
}

delete_log_stream_params = {
    "logGroupName": "test-intg-1234",
    "logStreamName": "test-intg-sream-1234"
}

create_log_retention_policy_params = {
    "logGroupName": "test-intg-1234",
    "retentionInDays": "1 Day"
}

delete_log_retention_policy_params = {
    "logGroupName": "test-intg-1234"
}

upload_log_event_params = {
    "logGroupName": "test-intg-1234",
    "logStreamName": "test-intg-sream-1234",
    "timestamp": 1633890600807,
    "message": "Test-upload"
}

run_log_insight_query_params = {
    "logGroupNames": ["test-intg-1234"],
    "startTime": time.time(),
    "endTime": time.time(),
    "queryString": "@timestamp"
}

get_log_insight_query_result_params = {
    "queryId": "254b388d-d2c9-4cfa-85e6-dd212437a050"
}

stop_log_insight_query_params = {
    "queryId": "254b388d-d2c9-4cfa-85e6-dd212437a050"
}




