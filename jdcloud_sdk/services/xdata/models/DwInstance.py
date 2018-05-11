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


class DwInstance(object):

    def __init__(self, instanceName, comments=None, instanceOwnerName=None, area=None, uname=None, createTime=None):
        """
        :param instanceName:  实例名
        :param comments: (Optional) 实例描述
        :param instanceOwnerName: (Optional) 实例属主
        :param area: (Optional) 实例所属区域
        :param uname: (Optional) 实例别名（在页面显示）
        :param createTime: (Optional) 实例创建时间
        """

        self.instanceName = instanceName
        self.comments = comments
        self.instanceOwnerName = instanceOwnerName
        self.area = area
        self.uname = uname
        self.createTime = createTime
