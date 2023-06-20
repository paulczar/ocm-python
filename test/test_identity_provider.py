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
from openapi_client.models.identity_provider import IdentityProvider  # noqa: E501
from openapi_client.rest import ApiException

class TestIdentityProvider(unittest.TestCase):
    """IdentityProvider unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IdentityProvider
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.identity_provider.IdentityProvider()  # noqa: E501
        if include_optional :
            return IdentityProvider(
                kind = '0', 
                id = '0', 
                href = '0', 
                ldap = openapi_client.models.ldap_identity_provider.LDAPIdentityProvider(
                    ca = '0', 
                    url = '0', 
                    attributes = openapi_client.models.ldap_attributes.LDAPAttributes(
                        id = [
                            '0'
                            ], 
                        email = [
                            '0'
                            ], 
                        name = [
                            '0'
                            ], 
                        preferred_username = [
                            '0'
                            ], ), 
                    bind_dn = '0', 
                    bind_password = '0', 
                    insecure = True, ), 
                challenge = True, 
                github = openapi_client.models.github_identity_provider.GithubIdentityProvider(
                    ca = '0', 
                    client_id = '0', 
                    client_secret = '0', 
                    hostname = '0', 
                    organizations = [
                        '0'
                        ], 
                    teams = [
                        '0'
                        ], ), 
                gitlab = openapi_client.models.gitlab_identity_provider.GitlabIdentityProvider(
                    ca = '0', 
                    url = '0', 
                    client_id = '0', 
                    client_secret = '0', ), 
                google = openapi_client.models.google_identity_provider.GoogleIdentityProvider(
                    client_id = '0', 
                    client_secret = '0', 
                    hosted_domain = '0', ), 
                htpasswd = openapi_client.models.ht_passwd_identity_provider.HTPasswdIdentityProvider(
                    password = '0', 
                    username = '0', 
                    users = [
                        openapi_client.models.ht_passwd_user.HTPasswdUser(
                            id = '0', 
                            password = '0', 
                            username = '0', )
                        ], ), 
                login = True, 
                mapping_method = 'add', 
                name = '0', 
                open_id = openapi_client.models.open_id_identity_provider.OpenIDIdentityProvider(
                    ca = '0', 
                    claims = openapi_client.models.open_id_claims.OpenIDClaims(
                        email = [
                            '0'
                            ], 
                        groups = [
                            '0'
                            ], 
                        name = [
                            '0'
                            ], 
                        preferred_username = [
                            '0'
                            ], ), 
                    client_id = '0', 
                    client_secret = '0', 
                    extra_authorize_parameters = {
                        'key' : '0'
                        }, 
                    extra_scopes = [
                        '0'
                        ], 
                    issuer = '0', ), 
                type = 'LDAPIdentityProvider'
            )
        else :
            return IdentityProvider(
        )

    def testIdentityProvider(self):
        """Test IdentityProvider"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()