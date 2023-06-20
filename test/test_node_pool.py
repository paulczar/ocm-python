# coding: utf-8

"""
    clusters_mgmt

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: ocm-feedback@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.node_pool import NodePool  # noqa: E501
from openapi_client.rest import ApiException

class TestNodePool(unittest.TestCase):
    """NodePool unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NodePool
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.node_pool.NodePool()  # noqa: E501
        if include_optional :
            return NodePool(
                kind = '0', 
                id = '0', 
                href = '0', 
                aws_node_pool = openapi_client.models.aws_node_pool.AWSNodePool(
                    kind = '0', 
                    id = '0', 
                    href = '0', 
                    instance_profile = '0', 
                    instance_type = '0', 
                    tags = {
                        'key' : '0'
                        }, ), 
                auto_repair = True, 
                autoscaling = openapi_client.models.node_pool_autoscaling.NodePoolAutoscaling(
                    kind = '0', 
                    id = '0', 
                    href = '0', 
                    max_replica = 56, 
                    min_replica = 56, ), 
                availability_zone = '0', 
                labels = {
                    'key' : '0'
                    }, 
                replicas = 56, 
                status = openapi_client.models.node_pool_status.NodePoolStatus(
                    kind = '0', 
                    id = '0', 
                    href = '0', 
                    current_replicas = 56, 
                    message = '0', ), 
                subnet = '0', 
                taints = [
                    openapi_client.models.taint.Taint(
                        effect = '0', 
                        key = '0', 
                        value = '0', )
                    ], 
                tuning_configs = [
                    '0'
                    ], 
                version = openapi_client.models.version.Version(
                    kind = '0', 
                    id = '0', 
                    href = '0', 
                    rosa_enabled = True, 
                    available_upgrades = [
                        '0'
                        ], 
                    channel_group = '0', 
                    default = True, 
                    enabled = True, 
                    end_of_life_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    hosted_control_plane_enabled = True, 
                    raw_id = '0', 
                    release_image = '0', )
            )
        else :
            return NodePool(
        )

    def testNodePool(self):
        """Test NodePool"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()