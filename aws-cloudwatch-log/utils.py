""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

import json
import requests

import boto3
from connectors.core.connector import get_logger, ConnectorError
from .constants import *
from datetime import datetime

logger = get_logger('aws-cloudwatch-log')
TEMP_CRED_ENDPOINT = 'http://169.254.169.254/latest/meta-data/iam/security-credentials/{}'


def _get_temp_credentials(config):
    try:
        aws_iam_role = config.get('aws_iam_role')
        url = TEMP_CRED_ENDPOINT.format(aws_iam_role)
        resp = requests.get(url=url, verify=config.get('verify_ssl'))
        if resp.ok:
            data = json.loads(resp.text)
            return data
        else:
            logger.error(str(resp.text))
            raise ConnectorError("Unable to validate the credentials")
    except Exception as Err:
        logger.exception(Err)
        raise ConnectorError(Err)


def _assume_a_role(data, params, aws_region):
    try:
        client = boto3.client(CLOUDWATCH_SERVICE, region_name=aws_region, aws_access_key_id=data.get('AccessKeyId'),
                              aws_secret_access_key=data.get('SecretAccessKey'),
                              aws_session_token=data.get('Token'))
        role_arn = params.get('role_arn')
        session_name = params.get('session_name')
        response = client.assume_role(RoleArn=role_arn, RoleSessionName=session_name)
        aws_region2 = params.get('aws_region')
        aws_session = boto3.session.Session(region_name=aws_region2,
                                            aws_access_key_id=response['Credentials']['AccessKeyId'],
                                            aws_secret_access_key=response['Credentials']['SecretAccessKey'],
                                            aws_session_token=response['Credentials']['SessionToken'])
        return aws_session
    except Exception as Err:
        logger.exception(Err)
        raise ConnectorError(Err)


def _get_session(config, params):
    try:
        config_type = config.get('config_type')
        assume_role = params.get("assume_role", False)
        if config_type == "AWS Instance IAM Role":
            if not assume_role:
                raise ConnectorError("Please Assume a Role to execute actions")

            aws_region = params.get('aws_region')
            data = _get_temp_credentials(config)
            aws_session = _assume_a_role(data, params, aws_region)
            return aws_session

        else:
            aws_access_key = config.get('aws_access_key')
            aws_region = config.get('aws_region')
            aws_secret_access_key = config.get('aws_secret_access_key')
            if assume_role:
                data = {
                    "AccessKeyId": aws_access_key,
                    "SecretAccessKey": aws_secret_access_key,
                    "Token": None
                }
                aws_session = _assume_a_role(data, params, aws_region)
            else:
                aws_session = boto3.session.Session(region_name=aws_region, aws_access_key_id=aws_access_key,
                                                    aws_secret_access_key=aws_secret_access_key)
            return aws_session
    except Exception as Err:
        raise ConnectorError(Err)


def _get_aws_client(config, params, service):
    try:
        aws_session = _get_session(config, params)
        aws_client = aws_session.client(service, verify=config.get('verify_ssl'))
        return aws_client
    except Exception as Err:
        logger.exception(Err)
        raise ConnectorError(Err)


def _convert_to_epoch(date_time):
    try:
        if isinstance(date_time, int):
            try:
                datetime.fromtimestamp(date_time)
                return int(date_time * 1000)
            except (OSError, ValueError):
                datetime.fromtimestamp(date_time / 1e3)
                return date_time
        else:
            time_stamp = datetime.strptime(date_time, "%Y-%m-%dT%H:%M:%S.%fZ")
            epoch_time = (time_stamp - datetime(1970, 1, 1)).total_seconds()
            return int(epoch_time * 1000)
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(
            "[{}] Invalid date format. Provide date in '%Y-%m-%dT%H:%M:%S.%fZ' e.g ‘2020-10-11T04:30:00.000Z’".format(
                str(err), str(date_time)))


def _convert_csv_str_to_list(list_param):
    try:
        if isinstance(list_param, str):
            return list_param.split(',')
        elif isinstance(list_param, list):
            return list_param
        else:
            raise ConnectorError("{} is not in a valid list or csv format".format(list_param))
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))


def _build_request_payload(params, operation=None):
    if "assume_role" in params:
        params.pop("assume_role")
    try:
        params_dict = {}
        for k, v in params.items():
            if v or isinstance(v, bool):
                if k in DATE_PARAMS:
                    params_dict[k] = _convert_to_epoch(v)
                elif k in LIST_PARAMS:
                    params_dict[k] = _convert_csv_str_to_list(v)
                elif v in RETENTION_PERIOD.keys():
                    params_dict[k] = RETENTION_PERIOD.get(v)
                elif k in TOKEN_PARAMS:
                    params_dict[k] = str(v)
                else:
                    params_dict[k] = v
        if operation == 'upload_log_event':
            params_dict['logEvents'] = [{k: v for k, v in params_dict.items() if k in LOG_EVENT_MESSAGE_PARAMS}]
            [params_dict.pop(k) for k in LOG_EVENT_MESSAGE_PARAMS]
        return params_dict
    except Exception as err:
        logger.error('{}'.format(str(err)))
        raise ConnectorError(str(err))
