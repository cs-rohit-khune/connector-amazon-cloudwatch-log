""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

from connectors.core.connector import get_logger, ConnectorError
from .utils import _get_aws_client, _build_request_payload, _get_temp_credentials
from .constants import *
import boto3

logger = get_logger('aws-cloudwatch-log')


def create_log_group(config, params):
    try:
        cw_client = _get_aws_client(config, params, CLOUDWATCH_SERVICE)
        params_dict = _build_request_payload(params)
        response = cw_client.create_log_group(**params_dict)
        return response
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


def create_log_stream(config, params):
    try:
        cw_client = _get_aws_client(config, params, CLOUDWATCH_SERVICE)
        params_dict = _build_request_payload(params)
        response = cw_client.create_log_stream(**params_dict)
        return response
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


def get_list_log_groups(config, params):
    try:
        cw_client = _get_aws_client(config, params, CLOUDWATCH_SERVICE)
        params_dict = _build_request_payload(params)
        response = cw_client.describe_log_groups(**params_dict)
        return response
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


def get_list_log_streams(config, params):
    try:
        cw_client = _get_aws_client(config, params, CLOUDWATCH_SERVICE)
        params_dict = _build_request_payload(params)
        response = cw_client.describe_log_streams(**params_dict)
        return response
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


def get_log_events(config, params):
    try:
        cw_client = _get_aws_client(config, params, CLOUDWATCH_SERVICE)
        params_dict = _build_request_payload(params)
        response = cw_client.get_log_events(**params_dict)
        return response
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


def delete_log_group(config, params):
    try:
        cw_client = _get_aws_client(config, params, CLOUDWATCH_SERVICE)
        params_dict = _build_request_payload(params)
        response = cw_client.delete_log_group(**params_dict)
        return response
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


def delete_log_stream(config, params):
    try:
        cw_client = _get_aws_client(config, params, CLOUDWATCH_SERVICE)
        params_dict = _build_request_payload(params)
        response = cw_client.delete_log_stream(**params_dict)
        return response
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


def create_log_retention_policy(config, params):
    try:
        cw_client = _get_aws_client(config, params, CLOUDWATCH_SERVICE)
        params_dict = _build_request_payload(params)
        response = cw_client.put_retention_policy(**params_dict)
        return response
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


def delete_log_retention_policy(config, params):
    try:
        cw_client = _get_aws_client(config, params, CLOUDWATCH_SERVICE)
        params_dict = _build_request_payload(params)
        response = cw_client.delete_retention_policy(**params_dict)
        return response
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


def upload_log_event(config, params):
    try:
        cw_client = _get_aws_client(config, params, CLOUDWATCH_SERVICE)
        params_dict = _build_request_payload(params, operation='upload_log_event')
        response = cw_client.put_log_events(**params_dict)
        return response
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


def run_log_insight_query(config, params):
    try:
        cw_client = _get_aws_client(config, params, CLOUDWATCH_SERVICE)
        log_group_names = params.get("logGroupNames")
        if isinstance(log_group_names, list) and len(log_group_names) == 1:
            params["logGroupName"] = log_group_names[0]
            params.pop("logGroupNames")
        params_dict = _build_request_payload(params)
        response = cw_client.start_query(**params_dict)
        return response
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


def get_log_insight_query_result(config, params):
    try:
        cw_client = _get_aws_client(config, params, CLOUDWATCH_SERVICE)
        params_dict = _build_request_payload(params)
        response = cw_client.get_query_results(**params_dict)
        return response
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


def stop_log_insight_query(config, params):
    try:
        cw_client = _get_aws_client(config, params, CLOUDWATCH_SERVICE)
        params_dict = _build_request_payload(params)
        response = cw_client.stop_query(**params_dict)
        return response
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


def check_health(config):
    try:
        config_type = config.get('config_type')
        if config_type == "AWS Instance IAM Role":
            if _get_temp_credentials(config):
                return True
            else:
                logger.error('Invalid Role. Please verify is the role is associated to your instance.')
                raise ConnectorError('Invalid Role. Please verify is the role is associated to your instance.')
        else:
            aws_access_key = config.get('aws_access_key')
            aws_region = config.get('aws_region')
            aws_secret_access_key = config.get('aws_secret_access_key')
            client = boto3.client(CLOUDWATCH_SERVICE, region_name=aws_region, aws_access_key_id=aws_access_key,
                                  aws_secret_access_key=aws_secret_access_key)
            client.describe_log_groups(limit=1)
            return True

    except Exception as Err:
        logger.exception(Err)
        raise ConnectorError(Err)


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
