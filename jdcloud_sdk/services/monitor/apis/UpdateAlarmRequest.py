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


class UpdateAlarmRequest(JDCloudRequest):
    """
    修改已创建的报警规则
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(UpdateAlarmRequest, self).__init__(
            '/regions/{regionId}/alarms/{alarmId}', 'PATCH', header, version)
        self.parameters = parameters


class UpdateAlarmParameters(object):

    def __init__(self, regionId, alarmId, calculation, metric, operation, period, serviceCode, threshold, times):
        """
        :param regionId: 地域 Id
        :param alarmId: 规则id
        :param calculation: 统计方法：平均值=avg、最大值=max、最小值=min、总和=sum
        :param metric: 根据产品线查询可用监控项列表 接口 返回的Metric字段
        :param operation: >=、>、<、<=、==、!=
        :param period: 统计周期（单位：分钟），可选值：2,5,15,30,60
        :param serviceCode: 产品名称
        :param threshold: 阈值
        :param times: 连续多少次后报警，可选值:1,2,3,5
        """

        self.regionId = regionId
        self.alarmId = alarmId
        self.calculation = calculation
        self.contactGroups = None
        self.contactPersons = None
        self.downSample = None
        self.metric = metric
        self.noticePeriod = None
        self.operation = operation
        self.period = period
        self.serviceCode = serviceCode
        self.threshold = threshold
        self.times = times

    def setContactGroups(self, contactGroups):
        """
        :param contactGroups: (Optional) 通知的联系组，如 [“联系组1”,”联系组2”]
        """
        self.contactGroups = contactGroups

    def setContactPersons(self, contactPersons):
        """
        :param contactPersons: (Optional) 通知的联系人，如 [“联系人1”,”联系人2”]
        """
        self.contactPersons = contactPersons

    def setDownSample(self, downSample):
        """
        :param downSample: (Optional) 取样频次
        """
        self.downSample = downSample

    def setNoticePeriod(self, noticePeriod):
        """
        :param noticePeriod: (Optional) 通知周期 单位：小时
        """
        self.noticePeriod = noticePeriod

