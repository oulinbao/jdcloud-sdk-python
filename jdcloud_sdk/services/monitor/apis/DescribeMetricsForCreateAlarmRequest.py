# coding=utf8

# Copyright 2018-2025 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class DescribeMetricsForCreateAlarmRequest(JDCloudRequest):
    """
    查询可用创建监控规则的指标列表
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeMetricsForCreateAlarmRequest, self).__init__(
            '/metricsForCreateAlarm', 'GET', header, version)
        self.parameters = parameters


class DescribeMetricsForCreateAlarmParameters(object):

    def __init__(self, ):
        """
        """

        self.serviceCode = None

    def setServiceCode(self, serviceCode):
        """
        :param serviceCode: (Optional) 资源的类型，取值vm, lb, ip, database 等，默认为空，展示所有项目
        """
        self.serviceCode = serviceCode

