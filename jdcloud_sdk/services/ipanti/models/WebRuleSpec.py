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


class WebRuleSpec(object):

    def __init__(self, domain=None, protocol=None, port=None, originType=None, originAddr=None, httpsCertContent=None, httpsRsaKey=None):
        """
        :param domain: (Optional) 子域名
        :param protocol: (Optional) 协议：HTTP、HTTPS、HTTP_HTTPS
        :param port: (Optional) 端口号，80,443
        :param originType: (Optional) 回源类型：ip或者domain
        :param originAddr: (Optional) 回源地址：originType为ip时为多个填多个ip，originType为domain时填一个域名
        :param httpsCertContent: (Optional) 证书内容
        :param httpsRsaKey: (Optional) 证书私钥
        """

        self.domain = domain
        self.protocol = protocol
        self.port = port
        self.originType = originType
        self.originAddr = originAddr
        self.httpsCertContent = httpsCertContent
        self.httpsRsaKey = httpsRsaKey
