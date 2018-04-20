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


class ContainerSpec(object):

    def __init__(self, instanceType, az, name, rootVolume, primaryNetworkInterface, hostAliases=None, hostname=None, command=None, args=None, envs=None, image=None, secret=None, tty=None, workingDir=None, dataVolumes=None, elasticIp=None, logConfiguration=None, description=None, charge=None):
        """
        :param instanceType:  实例类型；参考[文档](http://git.jd.com/jcloud-product/PRD/blob/master/云主机类型.md)
        :param az:  容器所属可用区
        :param name:  容器名称；命名规范请参考[文档](http://git.jd.com/jcloud-product/open-api-doc/blob/master/公共部分/API规则.md)
        :param hostAliases: (Optional) 域名和IP映射的信息；&lt;/br&gt; 最大10个alias
        :param hostname: (Optional) 主机名，规范请参考说明文档；默认容器ID
        :param command: (Optional) 容器执行命令，如果不指定默认是docker镜像的ENTRYPOINT
        :param args: (Optional) 容器执行命令的参数，如果不指定默认是docker镜像的CMD
        :param envs: (Optional) 容器执行的环境变量；如果和镜像中的环境变量Key相同，会覆盖镜像中的值；&lt;/br&gt; 最大10对
        :param image: (Optional) 镜像名称 &lt;/br&gt; 1. Docker Hub官方镜像通过类似nginx, mysql/mysql-server的名字指定 &lt;/br&gt; ^ 2. 其它私有仓储的镜像名称需要包含server地址：container-registry/image:tag &lt;/br&gt; &lt;/br&gt; repository长度最大256个字符，tag最大128个字符，registry最大255个字符 &lt;/br&gt; 下载镜像超时时间：10分钟
        :param secret: (Optional) secret引用名称；使用Docker Hub和京东云CR的镜像不需要secret
        :param tty: (Optional) 容器是否分配tty。默认不分配
        :param workingDir: (Optional) 容器的工作目录。如果不指定，默认是根目录（/）；必须是绝对路径
        :param rootVolume:  根Volume信息
        :param dataVolumes: (Optional) 挂载的数据Volume信息；最多7个
        :param elasticIp: (Optional) 主网卡主IP关联的弹性IP规格
        :param primaryNetworkInterface:  主网卡配置信息
        :param logConfiguration: (Optional) 容器日志配置信息；默认会在本地分配10MB的存储空间
        :param description: (Optional) 容器描述；命名规范请参考[文档](http://git.jd.com/jcloud-product/open-api-doc/blob/master/公共部分/API规则.md)
        :param charge: (Optional) 计费配置；如不指定，默认计费类型是后付费-按使用时常付费
        """

        self.instanceType = instanceType
        self.az = az
        self.name = name
        self.hostAliases = hostAliases
        self.hostname = hostname
        self.command = command
        self.args = args
        self.envs = envs
        self.image = image
        self.secret = secret
        self.tty = tty
        self.workingDir = workingDir
        self.rootVolume = rootVolume
        self.dataVolumes = dataVolumes
        self.elasticIp = elasticIp
        self.primaryNetworkInterface = primaryNetworkInterface
        self.logConfiguration = logConfiguration
        self.description = description
        self.charge = charge
