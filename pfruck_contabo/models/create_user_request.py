# coding: utf-8

"""
    Contabo API


    OpenAPI spec version: 1.0.0
    Contact: support@contabo.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreateUserRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'enabled': 'bool',
        'totp': 'bool',
        'locale': 'str',
        'roles': 'list[int]'
    }

    attribute_map = {
        'first_name': 'firstName',
        'last_name': 'lastName',
        'email': 'email',
        'enabled': 'enabled',
        'totp': 'totp',
        'locale': 'locale',
        'roles': 'roles'
    }

    def __init__(self, first_name=None, last_name=None, email=None, enabled=None, totp=None, locale=None, roles=None):  # noqa: E501
        """CreateUserRequest - a model defined in Swagger"""  # noqa: E501
        self._first_name = None
        self._last_name = None
        self._email = None
        self._enabled = None
        self._totp = None
        self._locale = None
        self._roles = None
        self.discriminator = None
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        self.email = email
        self.enabled = enabled
        self.totp = totp
        self.locale = locale
        if roles is not None:
            self.roles = roles

    @property
    def first_name(self):
        """Gets the first_name of this CreateUserRequest.  # noqa: E501

        The name of the user. Names may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per user.  # noqa: E501

        :return: The first_name of this CreateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this CreateUserRequest.

        The name of the user. Names may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per user.  # noqa: E501

        :param first_name: The first_name of this CreateUserRequest.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this CreateUserRequest.  # noqa: E501

        The last name of the user. Users may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per user.  # noqa: E501

        :return: The last_name of this CreateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this CreateUserRequest.

        The last name of the user. Users may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per user.  # noqa: E501

        :param last_name: The last_name of this CreateUserRequest.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this CreateUserRequest.  # noqa: E501

        The email of the user to which activation and forgot password links are being sent to. There is a limit of 255 characters per email.  # noqa: E501

        :return: The email of this CreateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CreateUserRequest.

        The email of the user to which activation and forgot password links are being sent to. There is a limit of 255 characters per email.  # noqa: E501

        :param email: The email of this CreateUserRequest.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def enabled(self):
        """Gets the enabled of this CreateUserRequest.  # noqa: E501

        If user is not enabled, he can't login and thus use services any longer.  # noqa: E501

        :return: The enabled of this CreateUserRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CreateUserRequest.

        If user is not enabled, he can't login and thus use services any longer.  # noqa: E501

        :param enabled: The enabled of this CreateUserRequest.  # noqa: E501
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def totp(self):
        """Gets the totp of this CreateUserRequest.  # noqa: E501

        Enable or disable two-factor authentication (2FA) via time based OTP.  # noqa: E501

        :return: The totp of this CreateUserRequest.  # noqa: E501
        :rtype: bool
        """
        return self._totp

    @totp.setter
    def totp(self, totp):
        """Sets the totp of this CreateUserRequest.

        Enable or disable two-factor authentication (2FA) via time based OTP.  # noqa: E501

        :param totp: The totp of this CreateUserRequest.  # noqa: E501
        :type: bool
        """
        if totp is None:
            raise ValueError("Invalid value for `totp`, must not be `None`")  # noqa: E501

        self._totp = totp

    @property
    def locale(self):
        """Gets the locale of this CreateUserRequest.  # noqa: E501

        The locale of the user. This can be `de-DE`, `de`, `en-US`, `en`  # noqa: E501

        :return: The locale of this CreateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this CreateUserRequest.

        The locale of the user. This can be `de-DE`, `de`, `en-US`, `en`  # noqa: E501

        :param locale: The locale of this CreateUserRequest.  # noqa: E501
        :type: str
        """
        if locale is None:
            raise ValueError("Invalid value for `locale`, must not be `None`")  # noqa: E501
        allowed_values = ["de-DE", "de", "en-US", "en"]  # noqa: E501
        if locale not in allowed_values:
            raise ValueError(
                "Invalid value for `locale` ({0}), must be one of {1}"  # noqa: E501
                .format(locale, allowed_values)
            )

        self._locale = locale

    @property
    def roles(self):
        """Gets the roles of this CreateUserRequest.  # noqa: E501

        The roles as list of `roleId`s of the user.  # noqa: E501

        :return: The roles of this CreateUserRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this CreateUserRequest.

        The roles as list of `roleId`s of the user.  # noqa: E501

        :param roles: The roles of this CreateUserRequest.  # noqa: E501
        :type: list[int]
        """

        self._roles = roles

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(CreateUserRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateUserRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
