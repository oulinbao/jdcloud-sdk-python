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


class DescribeDisksRequest(JDCloudRequest):
    """
    查询云硬盘列表
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeDisksRequest, self).__init__(
            '/regions/{regionId}/disks', 'GET', header, version)
        self.parameters = parameters


class DescribeDisksParameters(object):

    def __init__(self, regionId, ):
        """
        :param regionId: 地域ID
        """

        self.regionId = regionId
        self.pageNumber = None
        self.pageSize = None
        self.filters = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码, 默认为1, 取值范围：[1,∞)
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小，默认为20，取值范围：[10,100]
        """
        self.pageSize = pageSize

    def setFilters(self, filters):
        """
        :param filters: (Optional) diskId - 云硬盘ID，精确匹配，支持多个
diskType - 云硬盘类型，精确匹配，支持多个，取值为 ssd 或 premium-hdd
instanceId - 云硬盘所挂载主机的ID，精确匹配，支持多个
instanceType - 云硬盘所挂载主机的类型，精确匹配，支持多个
status - 可用区，精确匹配，支持多个
az - 云硬盘状态，精确匹配，支持多个
name - 云硬盘名称，模糊匹配，支持单个

        """
        self.filters = filters

