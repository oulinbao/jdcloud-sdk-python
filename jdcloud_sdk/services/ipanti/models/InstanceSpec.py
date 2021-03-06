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


class InstanceSpec(object):

    def __init__(self, name=None, buyType=None, timeUnit=None, timeSpan=None, carrier=None, bp=None, ep=None, bw=None):
        """
        :param name: (Optional) 实例名称
        :param buyType: (Optional) 购买类型：1新购 3升级
        :param timeUnit: (Optional) 购买时长单位：3月 4年
        :param timeSpan: (Optional) 购买时长跨度
        :param carrier: (Optional) 线路：UNICOM、TELECOM
        :param bp: (Optional) 保底带宽：单位Gbps
        :param ep: (Optional) 弹性带宽：单位Gbps
        :param bw: (Optional) 业务带宽：单位Mbps
        """

        self.name = name
        self.buyType = buyType
        self.timeUnit = timeUnit
        self.timeSpan = timeSpan
        self.carrier = carrier
        self.bp = bp
        self.ep = ep
        self.bw = bw
