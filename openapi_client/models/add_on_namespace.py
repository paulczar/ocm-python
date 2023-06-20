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


class AddOnNamespace(object):
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
        'kind': 'str',
        'id': 'str',
        'href': 'str',
        'annotations': 'dict(str, str)',
        'labels': 'dict(str, str)',
        'name': 'str'
    }

    attribute_map = {
        'kind': 'kind',
        'id': 'id',
        'href': 'href',
        'annotations': 'annotations',
        'labels': 'labels',
        'name': 'name'
    }

    def __init__(self, kind=None, id=None, href=None, annotations=None, labels=None, name=None, local_vars_configuration=None):  # noqa: E501
        """AddOnNamespace - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._kind = None
        self._id = None
        self._href = None
        self._annotations = None
        self._labels = None
        self._name = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if annotations is not None:
            self.annotations = annotations
        if labels is not None:
            self.labels = labels
        if name is not None:
            self.name = name

    @property
    def kind(self):
        """Gets the kind of this AddOnNamespace.  # noqa: E501

        Indicates the type of this object. Will be 'AddOnNamespace' if this is a complete object or 'AddOnNamespaceLink' if it is just a link.  # noqa: E501

        :return: The kind of this AddOnNamespace.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this AddOnNamespace.

        Indicates the type of this object. Will be 'AddOnNamespace' if this is a complete object or 'AddOnNamespaceLink' if it is just a link.  # noqa: E501

        :param kind: The kind of this AddOnNamespace.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def id(self):
        """Gets the id of this AddOnNamespace.  # noqa: E501

        Unique identifier of the object.  # noqa: E501

        :return: The id of this AddOnNamespace.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AddOnNamespace.

        Unique identifier of the object.  # noqa: E501

        :param id: The id of this AddOnNamespace.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this AddOnNamespace.  # noqa: E501

        Self link.  # noqa: E501

        :return: The href of this AddOnNamespace.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this AddOnNamespace.

        Self link.  # noqa: E501

        :param href: The href of this AddOnNamespace.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def annotations(self):
        """Gets the annotations of this AddOnNamespace.  # noqa: E501

        Annotations to be applied to this namespace.  # noqa: E501

        :return: The annotations of this AddOnNamespace.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this AddOnNamespace.

        Annotations to be applied to this namespace.  # noqa: E501

        :param annotations: The annotations of this AddOnNamespace.  # noqa: E501
        :type: dict(str, str)
        """

        self._annotations = annotations

    @property
    def labels(self):
        """Gets the labels of this AddOnNamespace.  # noqa: E501

        Labels to be applied to this namespace.  # noqa: E501

        :return: The labels of this AddOnNamespace.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this AddOnNamespace.

        Labels to be applied to this namespace.  # noqa: E501

        :param labels: The labels of this AddOnNamespace.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def name(self):
        """Gets the name of this AddOnNamespace.  # noqa: E501

        Name of the namespace.  # noqa: E501

        :return: The name of this AddOnNamespace.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddOnNamespace.

        Name of the namespace.  # noqa: E501

        :param name: The name of this AddOnNamespace.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, AddOnNamespace):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddOnNamespace):
            return True

        return self.to_dict() != other.to_dict()