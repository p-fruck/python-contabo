# coding: utf-8

"""
    Contabo API

    # Introduction  Contabo API allows you to manage your resources using HTTP requests. This documentation includes a set of HTTP endpoints that are designed to RESTful principles. Each endpoint includes descriptions, request syntax, and examples.  Contabo provides also a CLI tool which enables you to manage your resources easily from the command line. [CLI Download and  Installation instructions.](https://github.com/contabo/cntb)  ## Getting Started  In order to use the Contabo API you will need the following credentials which are available from the [Customer Control Panel](https://my.contabo.com/api/details): 1. ClientId 2. ClientSecret 3. API User (your email address to login to the [Customer Control Panel](https://my.contabo.com/api/details)) 4. API Password (this is a new password which you'll set or change in the [Customer Control Panel](https://my.contabo.com/api/details))  You can either use the API directly or by using the `cntb` CLI (Command Line Interface) tool.  ### Using the API directly  #### Via `curl` for Linux/Unix like systems  This requires `curl` and `jq` in your shell (e.g. `bash`, `zsh`). Please replace the first four placeholders with actual values.  ```sh CLIENT_ID=<ClientId from Customer Control Panel> CLIENT_SECRET=<ClientSecret from Customer Control Panel> API_USER=<API User from Customer Control Panel> API_PASSWORD=<API Password from Customer Control Panel> ACCESS_TOKEN=$(curl -d \"client_id=$CLIENT_ID\" -d \"client_secret=$CLIENT_SECRET\" --data-urlencode \"username=$API_USER\" --data-urlencode \"password=$API_PASSWORD\" -d 'grant_type=password' 'https://auth.contabo.com/auth/realms/contabo/protocol/openid-connect/token' | jq -r '.access_token') # get list of your instances curl -X GET -H \"Authorization: Bearer $ACCESS_TOKEN\" -H \"x-request-id: 51A87ECD-754E-4104-9C54-D01AD0F83406\" \"https://api.contabo.com/v1/compute/instances\" | jq ```  #### Via `PowerShell` for Windows  Please open `PowerShell` and execute the following code after replacing the first four placeholders with actual values.  ```powershell $client_id='<ClientId from Customer Control Panel>' $client_secret='<ClientSecret from Customer Control Panel>' $api_user='<API User from Customer Control Panel>' $api_password='<API Password from Customer Control Panel>' $body = @{grant_type='password' client_id=$client_id client_secret=$client_secret username=$api_user password=$api_password} $response = Invoke-WebRequest -Uri 'https://auth.contabo.com/auth/realms/contabo/protocol/openid-connect/token' -Method 'POST' -Body $body $access_token = (ConvertFrom-Json $([String]::new($response.Content))).access_token # get list of your instances $headers = @{} $headers.Add(\"Authorization\",\"Bearer $access_token\") $headers.Add(\"x-request-id\",\"51A87ECD-754E-4104-9C54-D01AD0F83406\") Invoke-WebRequest -Uri 'https://api.contabo.com/v1/compute/instances' -Method 'GET' -Headers $headers ```  ### Using the Contabo API via the `cntb` CLI tool  1. Download `cntb` for your operating system (MacOS, Windows and Linux supported) [here](https://github.com/contabo/cntb) 2. Unzip the downloaded file 3. You might move the executable to any location on your disk. You may update your `PATH` environment variable for easier invocation. 4. Configure it once to use your credentials           ```sh    cntb config set-credentials --oauth2-clientid=<ClientId from Customer Control Panel> --oauth2-client-secret=<ClientSecret from Customer Control Panel> --oauth2-user=<API User from Customer Control Panel> --oauth2-password=<API Password from Customer Control Panel>    ```  5. Use the CLI           ```sh    # get list of your instances    cntb get instances    # help    cntb help    ```  ## API Overiew  ### [Compute Mangement](#tag/Instances)  The Compute Management API allows you to manage compute resources (e.g. creation, deletion, starting, stopping) as well as managing snapshots and custom images. It also offers you to take advantage of [cloud-init](https://cloud-init.io/) at least on our default / standard images (for custom images you'll need to provide cloud-init support packages). The API offers provisioning of cloud-init scripts via the `user_data` field.  Custom images must be provided in `.qcow2` or `.iso` format. This gives you even more flexibilty for setting up your environment.  ### [Secrets Mangement](#tag/Secrets)  You can optionally save your passwords or public ssh keys using the Secrets Managemnt API. You are not required to use it there will be no functional disadvantages.  By using that API you can easily reuse you public ssh keys when setting up different servers without the need to look them up every time. It can also be used to allow Contabo Supporters to access your machine without sending the passwords via potentially unsecure emails.  ### [User Management](#tag/Users)  If you need to allow other persons or automation scripts to access specific API endpoints resp. resources the User Mangement API comes into play. With that API you are able to manage users having possibly restricted access. You are free to define those restrictions to fit your needs. So beside an arbitrary number of users you basically define any number of so called `roles`. Roles allows access and must be one of the following types:  * `apiPermission`          This allows you to specify a restriction to certain functions of an API by allowing control over POST (=Create), GET (=Read), PUT/PATCH (=Update) and DELETE (=Delete) methods for each API endpoint (URL) individually. * `resourcePermission`          In order to restrict access to specific resources create a role with `resourcePermission` type by specifying any number of [tags](#tag-management). These tags need to be assigned to resources for them to take effect. E.g. a tag could be assiged to several compute resources. So that a user with that role (and of course access to the API endpoints via `apiPermission` role type) could only access those compute resources.  The `roles` are then assigned to a `user`. You can assign one or several roles regardless of the role's type. Of course you could also assign a user `admin` privileges without specifying any roles.  ### [Tag Management](#tag/Tags)  The Tag Management API allows you to manage your tags in order to organize your resources in a more convenient way. Simply assign a tag to resources like a compute resource to manage them.The assignments of tags to resources will also enable you to control access to these specific resources to users via the [User Management API](#user-management). For convenience reasons you might choose a color for tag. The Customer Control Panel will use that color to display the tags.  ## Requests  The Contabo API supports HTTP requests like mentioned below. Not every endpoint supports all methods. The allowed methods are listed within this documentation.  Method | Description ---    | --- GET    | To retrieve information about a resource, use the GET method.<br>The data is returned as a JSON object. GET methods are read-only and do not affect any resources. POST   | Issue a POST method to create a new object. Include all needed attributes in the request body encoded as JSON. PATCH  | Some resources support partial modification with PATCH,<br>which modifies specific attributes without updating the entire object representation. PUT    | Use the PUT method to update information about a resource.<br>PUT will set new values on the item without regard to their current values. DELETE | Use the DELETE method to destroy a resource in your account.<br>If it is not found, the operation will return a 4xx error and an appropriate message.  ## Responses  Usually the Contabo API should respond to your requests. The data returned is in [JSON](https://www.json.org/) format allowing easy processing in any programming language or tools.  As common for HTTP requests you will get back a so called HTTP status code. This gives you overall information about success or error. The following table lists common HTTP status codes.  Please note that the description of the endpoints and methods are not listing all possibly status codes in detail as they are generic. Only special return codes with their resp. response data are explicitly listed.  Response Code | Description --- | --- 200 | The response contains your requested information. 201 | Your request was accepted. The resource was created. 204 | Your request succeeded, there is no additional information returned. 400 | Your request was malformed. 401 | You did not supply valid authentication credentials. 402 | Request refused as it requires additional payed service. 403 | You are not allowed to perform the request. 404 | No results were found for your request or resource does not exist. 409 | Conflict with resources. For example violation of unique data contraints detected when trying to create or change resources. 429 | Rate-limit reached. Please wait for some time before doing more requests. 500 | We were unable to perform the request due to server-side problems. In such cases please retry or contact the support.  Not every endpoint returns data. For example DELETE requests usually don't return any data. All others do return data. For easy handling the return values consists of metadata denoted with and underscore (\"_\") like `_links` or `_pagination`. The actual data is returned in a field called `data`. For convenience reasons this `data` field is always returned as an array even if it consists of only one single element.  Some general details about Contabo API from [Contabo](https://contabo.com).   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@contabo.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UserResponse(object):
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
        'tenant_id': 'str',
        'customer_id': 'str',
        'user_id': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'email_verified': 'bool',
        'enabled': 'bool',
        'totp': 'bool',
        'admin': 'bool',
        'access_all_resources': 'bool',
        'locale': 'str',
        'roles': 'list[RoleResponse]'
    }

    attribute_map = {
        'tenant_id': 'tenantId',
        'customer_id': 'customerId',
        'user_id': 'userId',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'email': 'email',
        'email_verified': 'emailVerified',
        'enabled': 'enabled',
        'totp': 'totp',
        'admin': 'admin',
        'access_all_resources': 'accessAllResources',
        'locale': 'locale',
        'roles': 'roles'
    }

    def __init__(self, tenant_id=None, customer_id=None, user_id=None, first_name=None, last_name=None, email=None, email_verified=None, enabled=None, totp=None, admin=None, access_all_resources=None, locale=None, roles=None):  # noqa: E501
        """UserResponse - a model defined in Swagger"""  # noqa: E501
        self._tenant_id = None
        self._customer_id = None
        self._user_id = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._email_verified = None
        self._enabled = None
        self._totp = None
        self._admin = None
        self._access_all_resources = None
        self._locale = None
        self._roles = None
        self.discriminator = None
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if customer_id is not None:
            self.customer_id = customer_id
        if user_id is not None:
            self.user_id = user_id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if email is not None:
            self.email = email
        if email_verified is not None:
            self.email_verified = email_verified
        if enabled is not None:
            self.enabled = enabled
        if totp is not None:
            self.totp = totp
        if admin is not None:
            self.admin = admin
        if access_all_resources is not None:
            self.access_all_resources = access_all_resources
        if locale is not None:
            self.locale = locale
        if roles is not None:
            self.roles = roles

    @property
    def tenant_id(self):
        """Gets the tenant_id of this UserResponse.  # noqa: E501

        Your customer tenant id  # noqa: E501

        :return: The tenant_id of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this UserResponse.

        Your customer tenant id  # noqa: E501

        :param tenant_id: The tenant_id of this UserResponse.  # noqa: E501
        :type: str
        """
        if tenant_id is None:
            raise ValueError("Invalid value for `tenant_id`, must not be `None`")  # noqa: E501

        self._tenant_id = tenant_id

    @property
    def customer_id(self):
        """Gets the customer_id of this UserResponse.  # noqa: E501

        Your customer number  # noqa: E501

        :return: The customer_id of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this UserResponse.

        Your customer number  # noqa: E501

        :param customer_id: The customer_id of this UserResponse.  # noqa: E501
        :type: str
        """
        if customer_id is None:
            raise ValueError("Invalid value for `customer_id`, must not be `None`")  # noqa: E501

        self._customer_id = customer_id

    @property
    def user_id(self):
        """Gets the user_id of this UserResponse.  # noqa: E501

        User's id  # noqa: E501

        :return: The user_id of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserResponse.

        User's id  # noqa: E501

        :param user_id: The user_id of this UserResponse.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def first_name(self):
        """Gets the first_name of this UserResponse.  # noqa: E501

        The first name of the user. Users may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per user.  # noqa: E501

        :return: The first_name of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserResponse.

        The first name of the user. Users may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per user.  # noqa: E501

        :param first_name: The first_name of this UserResponse.  # noqa: E501
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UserResponse.  # noqa: E501

        The last name of the user. Users may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per user.  # noqa: E501

        :return: The last_name of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserResponse.

        The last name of the user. Users may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per user.  # noqa: E501

        :param last_name: The last_name of this UserResponse.  # noqa: E501
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this UserResponse.  # noqa: E501

        The email of the user to which activation and forgot password links are being sent to. There is a limit of 255 characters per email.  # noqa: E501

        :return: The email of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserResponse.

        The email of the user to which activation and forgot password links are being sent to. There is a limit of 255 characters per email.  # noqa: E501

        :param email: The email of this UserResponse.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def email_verified(self):
        """Gets the email_verified of this UserResponse.  # noqa: E501

        User email verification status.  # noqa: E501

        :return: The email_verified of this UserResponse.  # noqa: E501
        :rtype: bool
        """
        return self._email_verified

    @email_verified.setter
    def email_verified(self, email_verified):
        """Sets the email_verified of this UserResponse.

        User email verification status.  # noqa: E501

        :param email_verified: The email_verified of this UserResponse.  # noqa: E501
        :type: bool
        """
        if email_verified is None:
            raise ValueError("Invalid value for `email_verified`, must not be `None`")  # noqa: E501

        self._email_verified = email_verified

    @property
    def enabled(self):
        """Gets the enabled of this UserResponse.  # noqa: E501

        If uses is not enabled, he can't login and thus use services any longer.  # noqa: E501

        :return: The enabled of this UserResponse.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UserResponse.

        If uses is not enabled, he can't login and thus use services any longer.  # noqa: E501

        :param enabled: The enabled of this UserResponse.  # noqa: E501
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def totp(self):
        """Gets the totp of this UserResponse.  # noqa: E501

        Enable or disable two-factor authentication (2FA) via time based OTP.  # noqa: E501

        :return: The totp of this UserResponse.  # noqa: E501
        :rtype: bool
        """
        return self._totp

    @totp.setter
    def totp(self, totp):
        """Sets the totp of this UserResponse.

        Enable or disable two-factor authentication (2FA) via time based OTP.  # noqa: E501

        :param totp: The totp of this UserResponse.  # noqa: E501
        :type: bool
        """
        if totp is None:
            raise ValueError("Invalid value for `totp`, must not be `None`")  # noqa: E501

        self._totp = totp

    @property
    def admin(self):
        """Gets the admin of this UserResponse.  # noqa: E501

        If user is admin he will have permissions to all API endpoints and resources. Enabling this will superseed all role definitions and `accessAllResources`.  # noqa: E501

        :return: The admin of this UserResponse.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this UserResponse.

        If user is admin he will have permissions to all API endpoints and resources. Enabling this will superseed all role definitions and `accessAllResources`.  # noqa: E501

        :param admin: The admin of this UserResponse.  # noqa: E501
        :type: bool
        """
        if admin is None:
            raise ValueError("Invalid value for `admin`, must not be `None`")  # noqa: E501

        self._admin = admin

    @property
    def access_all_resources(self):
        """Gets the access_all_resources of this UserResponse.  # noqa: E501

        Allow access to all resources. This will superseed all assigned roles of type `resourcePermission`. You'll need to set it to `true` in case you are not assigning roles of type `resourcePermission` explicitly.  # noqa: E501

        :return: The access_all_resources of this UserResponse.  # noqa: E501
        :rtype: bool
        """
        return self._access_all_resources

    @access_all_resources.setter
    def access_all_resources(self, access_all_resources):
        """Sets the access_all_resources of this UserResponse.

        Allow access to all resources. This will superseed all assigned roles of type `resourcePermission`. You'll need to set it to `true` in case you are not assigning roles of type `resourcePermission` explicitly.  # noqa: E501

        :param access_all_resources: The access_all_resources of this UserResponse.  # noqa: E501
        :type: bool
        """
        if access_all_resources is None:
            raise ValueError("Invalid value for `access_all_resources`, must not be `None`")  # noqa: E501

        self._access_all_resources = access_all_resources

    @property
    def locale(self):
        """Gets the locale of this UserResponse.  # noqa: E501

        The locale of the user. This can be `de-DE`, `de`, `en-US`, `en`  # noqa: E501

        :return: The locale of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this UserResponse.

        The locale of the user. This can be `de-DE`, `de`, `en-US`, `en`  # noqa: E501

        :param locale: The locale of this UserResponse.  # noqa: E501
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
        """Gets the roles of this UserResponse.  # noqa: E501

        The roles as list of `roleId`s of the user.  # noqa: E501

        :return: The roles of this UserResponse.  # noqa: E501
        :rtype: list[RoleResponse]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this UserResponse.

        The roles as list of `roleId`s of the user.  # noqa: E501

        :param roles: The roles of this UserResponse.  # noqa: E501
        :type: list[RoleResponse]
        """
        if roles is None:
            raise ValueError("Invalid value for `roles`, must not be `None`")  # noqa: E501

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
        if issubclass(UserResponse, dict):
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
        if not isinstance(other, UserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
