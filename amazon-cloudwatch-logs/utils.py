""" Copyright start
  Copyright (C) 2008 - 2021 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

from connectors.core.connector import get_logger, ConnectorError
from datetime import datetime
import boto3
from .constants import *

logger = get_logger('amazon-cloudwatch-logs')


class CloudWatch(object):

    def __init__(self, config):
        self.config_type = config.get('config_type')
        self.aws_access_key_id = config.get('aws_access_key_id')
        self.aws_secret_access_key = config.get('aws_secret_access_key')
        self.region_name = config.get('region_name')
        self.aws_iam_role = config.get('aws_iam_role')

    def _get_cloudwatch_client(self):
        try:
            if self.config_type == 'Assume Role':
                sts_client = boto3.client('sts', aws_access_key_id=self.aws_access_key_id,
                                          aws_secret_access_key=self.aws_secret_access_key)
                sts_response = sts_client.assume_role(RoleArn=self.aws_iam_role, RoleSessionName='CloudWatchLogs')
                client = boto3.client(
                    'logs',
                    aws_access_key_id=sts_response.get('Credentials').get('AccessKeyId'),
                    aws_secret_access_key=sts_response.get('Credentials').get('SecretAccessKey'),
                    aws_session_token=sts_response.get('Credentials').get('SessionToken'),
                    region_name=self.region_name
                )
            else:
                client = boto3.client(
                    'logs',
                    aws_access_key_id=self.aws_access_key_id,
                    aws_secret_access_key=self.aws_secret_access_key,
                    region_name=self.region_name
                )
            return client
        except Exception as err:
            logger.error('{}'.format(str(err)))
            raise ConnectorError(str(err))

    def _convert_to_epoch(self, date_time):
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

    def _convert_csv_str_to_list(self, list_param):
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

    def _build_request_payload(self, params, operation=None):
        try:
            params_dict = {}
            for k, v in params.items():
                if v or isinstance(v, bool):
                    if k in DATE_PARAMS:
                        params_dict[k] = self._convert_to_epoch(v)
                    elif k in LIST_PARAMS:
                        params_dict[k] = self._convert_csv_str_to_list(v)
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
