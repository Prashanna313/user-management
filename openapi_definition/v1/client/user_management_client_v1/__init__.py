# coding: utf-8

# flake8: noqa

"""
    User Management Microservice

    User Management Microservice  # noqa: E501

    The version of the OpenAPI document: v1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "0.0.0"

# import apis into sdk package
from user_management_client_v1.api.default_api import DefaultApi

# import ApiClient
from user_management_client_v1.api_client import ApiClient
from user_management_client_v1.configuration import Configuration
from user_management_client_v1.exceptions import OpenApiException
from user_management_client_v1.exceptions import ApiTypeError
from user_management_client_v1.exceptions import ApiValueError
from user_management_client_v1.exceptions import ApiKeyError
from user_management_client_v1.exceptions import ApiException
# import models into sdk package
from user_management_client_v1.models.error import Error
from user_management_client_v1.models.error_response import ErrorResponse
from user_management_client_v1.models.gender import Gender
from user_management_client_v1.models.get_users_response import GetUsersResponse
from user_management_client_v1.models.user import User

