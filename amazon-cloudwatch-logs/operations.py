""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

from connectors.core.connector import get_logger, ConnectorError
from .utils import CloudWatch

logger = get_logger('amazon-cloudwatch-logs')


def create_log_group(config, params):
    try:
        cw = CloudWatch(config)
        cw_client = cw._get_cloudwatch_client()
        params_dict = cw._build_request_payload(params)
        response = cw_client.create_log_group(**params_dict)
        return response
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


def create_log_stream(config, params):
    try:
        cw = CloudWatch(config)
        cw_client = cw._get_cloudwatch_client()
        params_dict = cw._build_request_payload(params)
        response = cw_client.create_log_stream(**params_dict)
        return response
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


def get_list_log_groups(config, params):
    try:
        cw = CloudWatch(config)
        cw_client = cw._get_cloudwatch_client()
        params_dict = cw._build_request_payload(params)
        response = cw_client.describe_log_groups(**params_dict)
        return response
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


def get_list_log_streams(config, params):
    try:
        cw = CloudWatch(config)
        cw_client = cw._get_cloudwatch_client()
        params_dict = cw._build_request_payload(params)
        response = cw_client.describe_log_streams(**params_dict)
        return response
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


def get_log_events(config, params):
    try:
        cw = CloudWatch(config)
        cw_client = cw._get_cloudwatch_client()
        params_dict = cw._build_request_payload(params)
        response = cw_client.get_log_events(**params_dict)
        return response
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


def delete_log_group(config, params):
    try:
        cw = CloudWatch(config)
        cw_client = cw._get_cloudwatch_client()
        params_dict = cw._build_request_payload(params)
        response = cw_client.delete_log_group(**params_dict)
        return response
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


def delete_log_stream(config, params):
    try:
        cw = CloudWatch(config)
        cw_client = cw._get_cloudwatch_client()
        params_dict = cw._build_request_payload(params)
        response = cw_client.delete_log_stream(**params_dict)
        return response
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


def create_log_retention_policy(config, params):
    try:
        cw = CloudWatch(config)
        cw_client = cw._get_cloudwatch_client()
        params_dict = cw._build_request_payload(params)
        response = cw_client.put_retention_policy(**params_dict)
        return response
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


def delete_log_retention_policy(config, params):
    try:
        cw = CloudWatch(config)
        cw_client = cw._get_cloudwatch_client()
        params_dict = cw._build_request_payload(params)
        response = cw_client.delete_retention_policy(**params_dict)
        return response
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


def upload_log_event(config, params):
    try:
        cw = CloudWatch(config)
        cw_client = cw._get_cloudwatch_client()
        params_dict = cw._build_request_payload(params, operation='upload_log_event')
        response = cw_client.put_log_events(**params_dict)
        return response
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


def run_log_insight_query(config, params):
    try:
        cw = CloudWatch(config)
        cw_client = cw._get_cloudwatch_client()
        params_dict = cw._build_request_payload(params)
        response = cw_client.start_query(**params_dict)
        return response
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


def get_log_insight_query_result(config, params):
    try:
        cw = CloudWatch(config)
        cw_client = cw._get_cloudwatch_client()
        params_dict = cw._build_request_payload(params)
        response = cw_client.get_query_results(**params_dict)
        return response
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


def stop_log_insight_query(config, params):
    try:
        cw = CloudWatch(config)
        cw_client = cw._get_cloudwatch_client()
        params_dict = cw._build_request_payload(params)
        response = cw_client.stop_query(**params_dict)
        return response
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


def health_check(config):
    try:
        cw = CloudWatch(config)
        cw_client = cw._get_cloudwatch_client()
        response = cw_client.describe_log_groups()
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return True
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


operations = {
    'create_log_group': create_log_group,
    'create_log_stream': create_log_stream,
    'get_list_log_groups': get_list_log_groups,
    'get_list_log_streams': get_list_log_streams,
    'get_log_events': get_log_events,
    'delete_log_group': delete_log_group,
    'delete_log_stream': delete_log_stream,
    'create_log_retention_policy': create_log_retention_policy,
    'delete_log_retention_policy': delete_log_retention_policy,
    'upload_log_event': upload_log_event,
    'run_log_insight_query': run_log_insight_query,
    'get_log_insight_query_result': get_log_insight_query_result,
    'stop_log_insight_query': stop_log_insight_query
}
