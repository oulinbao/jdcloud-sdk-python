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


class DescribeAlarmHistoryRequest(JDCloudRequest):
    """
    查询报警历史
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeAlarmHistoryRequest, self).__init__(
            '/regions/{regionId}/alarmHistory', 'GET', header, version)
        self.parameters = parameters


class DescribeAlarmHistoryParameters(object):

    def __init__(self, regionId, startTime, endTime, ):
        """
        :param regionId: 地域 Id
        :param startTime: 查询数据开始时间，默认24小时前，可以输入long型时间，也可以输入yyyy-MM-dd'T'HH:mm:ssZ类型时间
        :param endTime: 查询数据结束时间，默认当前时间，可以输入long型时间，也可以输入yyyy-MM-dd'T'HH:mm:ssZ类型时间
        """

        self.regionId = regionId
        self.id = None
        self.serviceCode = None
        self.resourceId = None
        self.startTime = startTime
        self.endTime = endTime
        self.pageNumber = None
        self.pageSize = None

    def setId(self, id):
        """
        :param id: (Optional) 报警规则的Id
        """
        self.id = id

    def setServiceCode(self, serviceCode):
        """
        :param serviceCode: (Optional) 产品名称
        """
        self.serviceCode = serviceCode

    def setResourceId(self, resourceId):
        """
        :param resourceId: (Optional) 资源Id
        """
        self.resourceId = resourceId

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 当前所在页，默认为1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) ，默认为20；取值范围[1, 100]
        """
        self.pageSize = pageSize

