# coding: utf-8

"""
    clusters_mgmt

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: ocm-feedback@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ocm_client.configuration import Configuration


class AutoscalerResourceLimits(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'gpus': 'list[AutoscalerResourceLimitsGPULimit]',
        'cores': 'ResourceRange',
        'max_nodes_total': 'int',
        'memory': 'ResourceRange'
    }

    attribute_map = {
        'gpus': 'gpus',
        'cores': 'cores',
        'max_nodes_total': 'max_nodes_total',
        'memory': 'memory'
    }

    def __init__(self, gpus=None, cores=None, max_nodes_total=None, memory=None, local_vars_configuration=None):  # noqa: E501
        """AutoscalerResourceLimits - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._gpus = None
        self._cores = None
        self._max_nodes_total = None
        self._memory = None
        self.discriminator = None

        if gpus is not None:
            self.gpus = gpus
        if cores is not None:
            self.cores = cores
        if max_nodes_total is not None:
            self.max_nodes_total = max_nodes_total
        if memory is not None:
            self.memory = memory

    @property
    def gpus(self):
        """Gets the gpus of this AutoscalerResourceLimits.  # noqa: E501

        Minimum and maximum number of different GPUs in cluster, in the format <gpu_type>:<min>:<max>. Cluster autoscaler will not scale the cluster beyond these numbers. Can be passed multiple times.  # noqa: E501

        :return: The gpus of this AutoscalerResourceLimits.  # noqa: E501
        :rtype: list[AutoscalerResourceLimitsGPULimit]
        """
        return self._gpus

    @gpus.setter
    def gpus(self, gpus):
        """Sets the gpus of this AutoscalerResourceLimits.

        Minimum and maximum number of different GPUs in cluster, in the format <gpu_type>:<min>:<max>. Cluster autoscaler will not scale the cluster beyond these numbers. Can be passed multiple times.  # noqa: E501

        :param gpus: The gpus of this AutoscalerResourceLimits.  # noqa: E501
        :type: list[AutoscalerResourceLimitsGPULimit]
        """

        self._gpus = gpus

    @property
    def cores(self):
        """Gets the cores of this AutoscalerResourceLimits.  # noqa: E501


        :return: The cores of this AutoscalerResourceLimits.  # noqa: E501
        :rtype: ResourceRange
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        """Sets the cores of this AutoscalerResourceLimits.


        :param cores: The cores of this AutoscalerResourceLimits.  # noqa: E501
        :type: ResourceRange
        """

        self._cores = cores

    @property
    def max_nodes_total(self):
        """Gets the max_nodes_total of this AutoscalerResourceLimits.  # noqa: E501

        Maximum number of nodes in all node groups. Cluster autoscaler will not grow the cluster beyond this number.  # noqa: E501

        :return: The max_nodes_total of this AutoscalerResourceLimits.  # noqa: E501
        :rtype: int
        """
        return self._max_nodes_total

    @max_nodes_total.setter
    def max_nodes_total(self, max_nodes_total):
        """Sets the max_nodes_total of this AutoscalerResourceLimits.

        Maximum number of nodes in all node groups. Cluster autoscaler will not grow the cluster beyond this number.  # noqa: E501

        :param max_nodes_total: The max_nodes_total of this AutoscalerResourceLimits.  # noqa: E501
        :type: int
        """

        self._max_nodes_total = max_nodes_total

    @property
    def memory(self):
        """Gets the memory of this AutoscalerResourceLimits.  # noqa: E501


        :return: The memory of this AutoscalerResourceLimits.  # noqa: E501
        :rtype: ResourceRange
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this AutoscalerResourceLimits.


        :param memory: The memory of this AutoscalerResourceLimits.  # noqa: E501
        :type: ResourceRange
        """

        self._memory = memory

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AutoscalerResourceLimits):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AutoscalerResourceLimits):
            return True

        return self.to_dict() != other.to_dict()