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

from openapi_client.configuration import Configuration


class GCPEncryptionKey(object):
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
        'kms_key_service_account': 'str',
        'key_location': 'str',
        'key_name': 'str',
        'key_ring': 'str'
    }

    attribute_map = {
        'kms_key_service_account': 'kms_key_service_account',
        'key_location': 'key_location',
        'key_name': 'key_name',
        'key_ring': 'key_ring'
    }

    def __init__(self, kms_key_service_account=None, key_location=None, key_name=None, key_ring=None, local_vars_configuration=None):  # noqa: E501
        """GCPEncryptionKey - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._kms_key_service_account = None
        self._key_location = None
        self._key_name = None
        self._key_ring = None
        self.discriminator = None

        if kms_key_service_account is not None:
            self.kms_key_service_account = kms_key_service_account
        if key_location is not None:
            self.key_location = key_location
        if key_name is not None:
            self.key_name = key_name
        if key_ring is not None:
            self.key_ring = key_ring

    @property
    def kms_key_service_account(self):
        """Gets the kms_key_service_account of this GCPEncryptionKey.  # noqa: E501

        Service account used to access the KMS key  # noqa: E501

        :return: The kms_key_service_account of this GCPEncryptionKey.  # noqa: E501
        :rtype: str
        """
        return self._kms_key_service_account

    @kms_key_service_account.setter
    def kms_key_service_account(self, kms_key_service_account):
        """Sets the kms_key_service_account of this GCPEncryptionKey.

        Service account used to access the KMS key  # noqa: E501

        :param kms_key_service_account: The kms_key_service_account of this GCPEncryptionKey.  # noqa: E501
        :type: str
        """

        self._kms_key_service_account = kms_key_service_account

    @property
    def key_location(self):
        """Gets the key_location of this GCPEncryptionKey.  # noqa: E501

        Location of the encryption key ring  # noqa: E501

        :return: The key_location of this GCPEncryptionKey.  # noqa: E501
        :rtype: str
        """
        return self._key_location

    @key_location.setter
    def key_location(self, key_location):
        """Sets the key_location of this GCPEncryptionKey.

        Location of the encryption key ring  # noqa: E501

        :param key_location: The key_location of this GCPEncryptionKey.  # noqa: E501
        :type: str
        """

        self._key_location = key_location

    @property
    def key_name(self):
        """Gets the key_name of this GCPEncryptionKey.  # noqa: E501

        Name of the encryption key  # noqa: E501

        :return: The key_name of this GCPEncryptionKey.  # noqa: E501
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this GCPEncryptionKey.

        Name of the encryption key  # noqa: E501

        :param key_name: The key_name of this GCPEncryptionKey.  # noqa: E501
        :type: str
        """

        self._key_name = key_name

    @property
    def key_ring(self):
        """Gets the key_ring of this GCPEncryptionKey.  # noqa: E501

        Name of the key ring the encryption key is located on  # noqa: E501

        :return: The key_ring of this GCPEncryptionKey.  # noqa: E501
        :rtype: str
        """
        return self._key_ring

    @key_ring.setter
    def key_ring(self, key_ring):
        """Sets the key_ring of this GCPEncryptionKey.

        Name of the key ring the encryption key is located on  # noqa: E501

        :param key_ring: The key_ring of this GCPEncryptionKey.  # noqa: E501
        :type: str
        """

        self._key_ring = key_ring

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
        if not isinstance(other, GCPEncryptionKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GCPEncryptionKey):
            return True

        return self.to_dict() != other.to_dict()