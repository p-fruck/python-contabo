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

class ImageResponse(object):
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
        'image_id': 'str',
        'tenant_id': 'str',
        'customer_id': 'str',
        'name': 'str',
        'description': 'str',
        'url': 'str',
        'size_mb': 'float',
        'os_type': 'str',
        'version': 'str',
        'format': 'str',
        'status': 'str',
        'error_message': 'str',
        'standard_image': 'bool',
        'last_modified_date': 'datetime'
    }

    attribute_map = {
        'image_id': 'imageId',
        'tenant_id': 'tenantId',
        'customer_id': 'customerId',
        'name': 'name',
        'description': 'description',
        'url': 'url',
        'size_mb': 'sizeMb',
        'os_type': 'osType',
        'version': 'version',
        'format': 'format',
        'status': 'status',
        'error_message': 'errorMessage',
        'standard_image': 'standardImage',
        'last_modified_date': 'lastModifiedDate'
    }

    def __init__(self, image_id=None, tenant_id=None, customer_id=None, name=None, description=None, url=None, size_mb=None, os_type=None, version=None, format=None, status=None, error_message=None, standard_image=None, last_modified_date=None):  # noqa: E501
        """ImageResponse - a model defined in Swagger"""  # noqa: E501
        self._image_id = None
        self._tenant_id = None
        self._customer_id = None
        self._name = None
        self._description = None
        self._url = None
        self._size_mb = None
        self._os_type = None
        self._version = None
        self._format = None
        self._status = None
        self._error_message = None
        self._standard_image = None
        self._last_modified_date = None
        self.discriminator = None
        self.image_id = image_id
        self.tenant_id = tenant_id
        self.customer_id = customer_id
        self.name = name
        self.description = description
        self.url = url
        self.size_mb = size_mb
        self.os_type = os_type
        self.version = version
        self.format = format
        self.status = status
        self.error_message = error_message
        self.standard_image = standard_image
        self.last_modified_date = last_modified_date

    @property
    def image_id(self):
        """Gets the image_id of this ImageResponse.  # noqa: E501

        Image's id  # noqa: E501

        :return: The image_id of this ImageResponse.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ImageResponse.

        Image's id  # noqa: E501

        :param image_id: The image_id of this ImageResponse.  # noqa: E501
        :type: str
        """
        if image_id is None:
            raise ValueError("Invalid value for `image_id`, must not be `None`")  # noqa: E501

        self._image_id = image_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ImageResponse.  # noqa: E501

        Your customer tenant id  # noqa: E501

        :return: The tenant_id of this ImageResponse.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ImageResponse.

        Your customer tenant id  # noqa: E501

        :param tenant_id: The tenant_id of this ImageResponse.  # noqa: E501
        :type: str
        """
        if tenant_id is None:
            raise ValueError("Invalid value for `tenant_id`, must not be `None`")  # noqa: E501
        allowed_values = ["DE", "INT"]  # noqa: E501
        if tenant_id not in allowed_values:
            raise ValueError(
                "Invalid value for `tenant_id` ({0}), must be one of {1}"  # noqa: E501
                .format(tenant_id, allowed_values)
            )

        self._tenant_id = tenant_id

    @property
    def customer_id(self):
        """Gets the customer_id of this ImageResponse.  # noqa: E501

        Customer ID  # noqa: E501

        :return: The customer_id of this ImageResponse.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ImageResponse.

        Customer ID  # noqa: E501

        :param customer_id: The customer_id of this ImageResponse.  # noqa: E501
        :type: str
        """
        if customer_id is None:
            raise ValueError("Invalid value for `customer_id`, must not be `None`")  # noqa: E501

        self._customer_id = customer_id

    @property
    def name(self):
        """Gets the name of this ImageResponse.  # noqa: E501

        Image Name  # noqa: E501

        :return: The name of this ImageResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImageResponse.

        Image Name  # noqa: E501

        :param name: The name of this ImageResponse.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this ImageResponse.  # noqa: E501

        Image Description  # noqa: E501

        :return: The description of this ImageResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ImageResponse.

        Image Description  # noqa: E501

        :param description: The description of this ImageResponse.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def url(self):
        """Gets the url of this ImageResponse.  # noqa: E501

        URL from where the image has been downloaded / provided.  # noqa: E501

        :return: The url of this ImageResponse.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ImageResponse.

        URL from where the image has been downloaded / provided.  # noqa: E501

        :param url: The url of this ImageResponse.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def size_mb(self):
        """Gets the size_mb of this ImageResponse.  # noqa: E501

        Image Size in MB  # noqa: E501

        :return: The size_mb of this ImageResponse.  # noqa: E501
        :rtype: float
        """
        return self._size_mb

    @size_mb.setter
    def size_mb(self, size_mb):
        """Sets the size_mb of this ImageResponse.

        Image Size in MB  # noqa: E501

        :param size_mb: The size_mb of this ImageResponse.  # noqa: E501
        :type: float
        """
        if size_mb is None:
            raise ValueError("Invalid value for `size_mb`, must not be `None`")  # noqa: E501

        self._size_mb = size_mb

    @property
    def os_type(self):
        """Gets the os_type of this ImageResponse.  # noqa: E501

        Type of operating system (OS)  # noqa: E501

        :return: The os_type of this ImageResponse.  # noqa: E501
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this ImageResponse.

        Type of operating system (OS)  # noqa: E501

        :param os_type: The os_type of this ImageResponse.  # noqa: E501
        :type: str
        """
        if os_type is None:
            raise ValueError("Invalid value for `os_type`, must not be `None`")  # noqa: E501

        self._os_type = os_type

    @property
    def version(self):
        """Gets the version of this ImageResponse.  # noqa: E501

        Version number to distinguish the contents of an image. Could be the version of the operating system for example.  # noqa: E501

        :return: The version of this ImageResponse.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ImageResponse.

        Version number to distinguish the contents of an image. Could be the version of the operating system for example.  # noqa: E501

        :param version: The version of this ImageResponse.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def format(self):
        """Gets the format of this ImageResponse.  # noqa: E501

        Image format  # noqa: E501

        :return: The format of this ImageResponse.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ImageResponse.

        Image format  # noqa: E501

        :param format: The format of this ImageResponse.  # noqa: E501
        :type: str
        """
        if format is None:
            raise ValueError("Invalid value for `format`, must not be `None`")  # noqa: E501
        allowed_values = ["iso", "qcow2"]  # noqa: E501
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def status(self):
        """Gets the status of this ImageResponse.  # noqa: E501

        Image status (e.g. if image is still downloading)  # noqa: E501

        :return: The status of this ImageResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ImageResponse.

        Image status (e.g. if image is still downloading)  # noqa: E501

        :param status: The status of this ImageResponse.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def error_message(self):
        """Gets the error_message of this ImageResponse.  # noqa: E501

        Image download error message  # noqa: E501

        :return: The error_message of this ImageResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this ImageResponse.

        Image download error message  # noqa: E501

        :param error_message: The error_message of this ImageResponse.  # noqa: E501
        :type: str
        """
        if error_message is None:
            raise ValueError("Invalid value for `error_message`, must not be `None`")  # noqa: E501

        self._error_message = error_message

    @property
    def standard_image(self):
        """Gets the standard_image of this ImageResponse.  # noqa: E501

        Flag indicating that image is either a standard (true) or a custom image (false)  # noqa: E501

        :return: The standard_image of this ImageResponse.  # noqa: E501
        :rtype: bool
        """
        return self._standard_image

    @standard_image.setter
    def standard_image(self, standard_image):
        """Sets the standard_image of this ImageResponse.

        Flag indicating that image is either a standard (true) or a custom image (false)  # noqa: E501

        :param standard_image: The standard_image of this ImageResponse.  # noqa: E501
        :type: bool
        """
        if standard_image is None:
            raise ValueError("Invalid value for `standard_image`, must not be `None`")  # noqa: E501

        self._standard_image = standard_image

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this ImageResponse.  # noqa: E501

        The last modified date time for the image  # noqa: E501

        :return: The last_modified_date of this ImageResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this ImageResponse.

        The last modified date time for the image  # noqa: E501

        :param last_modified_date: The last_modified_date of this ImageResponse.  # noqa: E501
        :type: datetime
        """
        if last_modified_date is None:
            raise ValueError("Invalid value for `last_modified_date`, must not be `None`")  # noqa: E501

        self._last_modified_date = last_modified_date

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
        if issubclass(ImageResponse, dict):
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
        if not isinstance(other, ImageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
