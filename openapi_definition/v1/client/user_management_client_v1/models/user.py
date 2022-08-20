# coding: utf-8

"""
    User Management Microservice

    User Management Microservice  # noqa: E501

    The version of the OpenAPI document: v1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from user_management_client_v1.configuration import Configuration


class User(object):
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
        'date_of_birth': 'date',
        'gender': 'Gender',
        'is_active': 'bool',
        'email': 'str',
        'first_name': 'str',
        'id': 'str',
        'last_name': 'str'
    }

    attribute_map = {
        'date_of_birth': 'dateOfBirth',
        'gender': 'gender',
        'is_active': 'isActive',
        'email': 'email',
        'first_name': 'firstName',
        'id': 'id',
        'last_name': 'lastName'
    }

    def __init__(self, date_of_birth=None, gender=None, is_active=None, email=None, first_name=None, id=None, last_name=None, local_vars_configuration=None):  # noqa: E501
        """User - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._date_of_birth = None
        self._gender = None
        self._is_active = None
        self._email = None
        self._first_name = None
        self._id = None
        self._last_name = None
        self.discriminator = None

        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        self.gender = gender
        self.is_active = is_active
        self.email = email
        self.first_name = first_name
        self.id = id
        self.last_name = last_name

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this User.  # noqa: E501

        Date of birth of the user in format: yyyy-MM-dd  # noqa: E501

        :return: The date_of_birth of this User.  # noqa: E501
        :rtype: date
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this User.

        Date of birth of the user in format: yyyy-MM-dd  # noqa: E501

        :param date_of_birth: The date_of_birth of this User.  # noqa: E501
        :type: date
        """

        self._date_of_birth = date_of_birth

    @property
    def gender(self):
        """Gets the gender of this User.  # noqa: E501


        :return: The gender of this User.  # noqa: E501
        :rtype: Gender
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this User.


        :param gender: The gender of this User.  # noqa: E501
        :type: Gender
        """
        if self.local_vars_configuration.client_side_validation and gender is None:  # noqa: E501
            raise ValueError("Invalid value for `gender`, must not be `None`")  # noqa: E501

        self._gender = gender

    @property
    def is_active(self):
        """Gets the is_active of this User.  # noqa: E501

        Flag that represents the current state of the user  # noqa: E501

        :return: The is_active of this User.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this User.

        Flag that represents the current state of the user  # noqa: E501

        :param is_active: The is_active of this User.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_active is None:  # noqa: E501
            raise ValueError("Invalid value for `is_active`, must not be `None`")  # noqa: E501

        self._is_active = is_active

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501

        Email address of the user  # noqa: E501

        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.

        Email address of the user  # noqa: E501

        :param email: The email of this User.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) > 256):
            raise ValueError("Invalid value for `email`, length must be less than or equal to `256`")  # noqa: E501

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this User.  # noqa: E501

        First Name of the user  # noqa: E501

        :return: The first_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this User.

        First Name of the user  # noqa: E501

        :param first_name: The first_name of this User.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and first_name is None:  # noqa: E501
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                first_name is not None and len(first_name) > 100):
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `100`")  # noqa: E501

        self._first_name = first_name

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501


        :return: The id of this User.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.


        :param id: The id of this User.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and not re.search(r'^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$', id)):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$/`")  # noqa: E501

        self._id = id

    @property
    def last_name(self):
        """Gets the last_name of this User.  # noqa: E501

        Last Name of the user  # noqa: E501

        :return: The last_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this User.

        Last Name of the user  # noqa: E501

        :param last_name: The last_name of this User.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and last_name is None:  # noqa: E501
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                last_name is not None and len(last_name) > 100):
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `100`")  # noqa: E501

        self._last_name = last_name

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
        if not isinstance(other, User):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, User):
            return True

        return self.to_dict() != other.to_dict()
