# coding: utf-8

"""
    User Management Microservice

    User Management Microservice  # noqa: E501

    The version of the OpenAPI document: v1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import user_management_client_v1
from user_management_client_v1.api.default_api import DefaultApi  # noqa: E501
from user_management_client_v1.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = user_management_client_v1.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_users(self):
        """Test case for get_users

        get users  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
