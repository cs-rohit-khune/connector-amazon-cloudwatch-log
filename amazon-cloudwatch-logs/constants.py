""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

# Consolidated list of date-time parameters used by several operations
DATE_PARAMS = ['startTime', 'endTime', 'fromTime', 'creationTime', 'completionTime', 'lastEventTimestamp',
               'lastIngestionTime', 'lastUpdatedTime', 'ingestionTime', 'timestamp']

# Time range for log retention policy of log group, used in 'Create Log Retention Policy' operation
RETENTION_PERIOD = {'1 Day': 1,
                    '3 Days': 3,
                    '5 Days': 5,
                    '1 Week': 7,
                    '2 Weeks': 14,
                    '1 Month': 30,
                    '2 Months': 60,
                    '3 Months': 90,
                    '4 Months': 120,
                    '5 Months': 150,
                    '6 Months': 180,
                    '12 Months': 365,
                    '13 Months': 400,
                    '18 Months': 545,
                    '24 Months': 731,
                    '60 Months': 1827,
                    '120 Months': 3653}

# Mandatory params for log event record in log stream, used in 'Upload Log Event' operation
LOG_EVENT_MESSAGE_PARAMS = ['timestamp', 'message']

# Parameters that must be in list format used by several operations. If values provide in csv, then it get converted to list
LIST_PARAMS = ['logGroupNames']

# Token params that can be an integer, but should always sent as string.
TOKEN_PARAMS = ['sequenceToken', 'nextToken']
