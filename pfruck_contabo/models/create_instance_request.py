# coding: utf-8

"""
    Contabo API

    # Introduction  Contabo API allows you to manage your resources using HTTP requests. This documentation includes a set of HTTP endpoints that are designed to RESTful principles. Each endpoint includes descriptions, request syntax, and examples.  Contabo provides also a CLI tool which enables you to manage your resources easily from the command line. [CLI Download and  Installation instructions.](https://github.com/contabo/cntb)  ## Getting Started  In order to use the Contabo API you will need the following credentials which are available from the [Customer Control Panel](https://my.contabo.com/api/details): 1. ClientId 2. ClientSecret 3. API User (your email address to login to the [Customer Control Panel](https://my.contabo.com/api/details)) 4. API Password (this is a new password which you'll set or change in the [Customer Control Panel](https://my.contabo.com/api/details))  You can either use the API directly or by using the `cntb` CLI (Command Line Interface) tool.  ### Using the API directly  #### Via `curl` for Linux/Unix like systems  This requires `curl` and `jq` in your shell (e.g. `bash`, `zsh`). Please replace the first four placeholders with actual values.  ```sh CLIENT_ID=<ClientId from Customer Control Panel> CLIENT_SECRET=<ClientSecret from Customer Control Panel> API_USER=<API User from Customer Control Panel> API_PASSWORD='<API Password from Customer Control Panel>' ACCESS_TOKEN=$(curl -d \"client_id=$CLIENT_ID\" -d \"client_secret=$CLIENT_SECRET\" --data-urlencode \"username=$API_USER\" --data-urlencode \"password=$API_PASSWORD\" -d 'grant_type=password' 'https://auth.contabo.com/auth/realms/contabo/protocol/openid-connect/token' | jq -r '.access_token') # get list of your instances curl -X GET -H \"Authorization: Bearer $ACCESS_TOKEN\" -H \"x-request-id: 51A87ECD-754E-4104-9C54-D01AD0F83406\" \"https://api.contabo.com/v1/compute/instances\" | jq ```  #### Via `PowerShell` for Windows  Please open `PowerShell` and execute the following code after replacing the first four placeholders with actual values.  ```powershell $client_id='<ClientId from Customer Control Panel>' $client_secret='<ClientSecret from Customer Control Panel>' $api_user='<API User from Customer Control Panel>' $api_password='<API Password from Customer Control Panel>' $body = @{grant_type='password' client_id=$client_id client_secret=$client_secret username=$api_user password=$api_password} $response = Invoke-WebRequest -Uri 'https://auth.contabo.com/auth/realms/contabo/protocol/openid-connect/token' -Method 'POST' -Body $body $access_token = (ConvertFrom-Json $([String]::new($response.Content))).access_token # get list of your instances $headers = @{} $headers.Add(\"Authorization\",\"Bearer $access_token\") $headers.Add(\"x-request-id\",\"51A87ECD-754E-4104-9C54-D01AD0F83406\") Invoke-WebRequest -Uri 'https://api.contabo.com/v1/compute/instances' -Method 'GET' -Headers $headers ```  ### Using the Contabo API via the `cntb` CLI tool  1. Download `cntb` for your operating system (MacOS, Windows and Linux supported) [here](https://github.com/contabo/cntb) 2. Unzip the downloaded file 3. You might move the executable to any location on your disk. You may update your `PATH` environment variable for easier invocation. 4. Configure it once to use your credentials           ```sh    cntb config set-credentials --oauth2-clientid=<ClientId from Customer Control Panel> --oauth2-client-secret=<ClientSecret from Customer Control Panel> --oauth2-user=<API User from Customer Control Panel> --oauth2-password=<API Password from Customer Control Panel>    ```  5. Use the CLI           ```sh    # get list of your instances    cntb get instances    # help    cntb help    ```  ## API Overiew  ### [Compute Mangement](#tag/Instances)  The Compute Management API allows you to manage compute resources (e.g. creation, deletion, starting, stopping) of VPS and VDS (please note that Storage VPS are not supported via API or CLI) as well as managing snapshots and custom images. It also offers you to take advantage of [cloud-init](https://cloud-init.io/) at least on our default / standard images (for custom images you'll need to provide cloud-init support packages). The API offers provisioning of cloud-init scripts via the `user_data` field.  Custom images must be provided in `.qcow2` or `.iso` format. This gives you even more flexibilty for setting up your environment.  ### [Secrets Mangement](#tag/Secrets)  You can optionally save your passwords or public ssh keys using the Secrets Managemnt API. You are not required to use it there will be no functional disadvantages.  By using that API you can easily reuse you public ssh keys when setting up different servers without the need to look them up every time. It can also be used to allow Contabo Supporters to access your machine without sending the passwords via potentially unsecure emails.  ### [User Management](#tag/Users)  If you need to allow other persons or automation scripts to access specific API endpoints resp. resources the User Mangement API comes into play. With that API you are able to manage users having possibly restricted access. You are free to define those restrictions to fit your needs. So beside an arbitrary number of users you basically define any number of so called `roles`. Roles allows access and must be one of the following types:  * `apiPermission`          This allows you to specify a restriction to certain functions of an API by allowing control over POST (=Create), GET (=Read), PUT/PATCH (=Update) and DELETE (=Delete) methods for each API endpoint (URL) individually. * `resourcePermission`          In order to restrict access to specific resources create a role with `resourcePermission` type by specifying any number of [tags](#tag-management). These tags need to be assigned to resources for them to take effect. E.g. a tag could be assiged to several compute resources. So that a user with that role (and of course access to the API endpoints via `apiPermission` role type) could only access those compute resources.  The `roles` are then assigned to a `user`. You can assign one or several roles regardless of the role's type. Of course you could also assign a user `admin` privileges without specifying any roles.  ### [Tag Management](#tag/Tags)  The Tag Management API allows you to manage your tags in order to organize your resources in a more convenient way. Simply assign a tag to resources like a compute resource to manage them.The assignments of tags to resources will also enable you to control access to these specific resources to users via the [User Management API](#user-management). For convenience reasons you might choose a color for tag. The Customer Control Panel will use that color to display the tags.  ## Requests  The Contabo API supports HTTP requests like mentioned below. Not every endpoint supports all methods. The allowed methods are listed within this documentation.  Method | Description ---    | --- GET    | To retrieve information about a resource, use the GET method.<br>The data is returned as a JSON object. GET methods are read-only and do not affect any resources. POST   | Issue a POST method to create a new object. Include all needed attributes in the request body encoded as JSON. PATCH  | Some resources support partial modification with PATCH,<br>which modifies specific attributes without updating the entire object representation. PUT    | Use the PUT method to update information about a resource.<br>PUT will set new values on the item without regard to their current values. DELETE | Use the DELETE method to destroy a resource in your account.<br>If it is not found, the operation will return a 4xx error and an appropriate message.  ## Responses  Usually the Contabo API should respond to your requests. The data returned is in [JSON](https://www.json.org/) format allowing easy processing in any programming language or tools.  As common for HTTP requests you will get back a so called HTTP status code. This gives you overall information about success or error. The following table lists common HTTP status codes.  Please note that the description of the endpoints and methods are not listing all possibly status codes in detail as they are generic. Only special return codes with their resp. response data are explicitly listed.  Response Code | Description --- | --- 200 | The response contains your requested information. 201 | Your request was accepted. The resource was created. 204 | Your request succeeded, there is no additional information returned. 400 | Your request was malformed. 401 | You did not supply valid authentication credentials. 402 | Request refused as it requires additional payed service. 403 | You are not allowed to perform the request. 404 | No results were found for your request or resource does not exist. 409 | Conflict with resources. For example violation of unique data contraints detected when trying to create or change resources. 429 | Rate-limit reached. Please wait for some time before doing more requests. 500 | We were unable to perform the request due to server-side problems. In such cases please retry or contact the support.  Not every endpoint returns data. For example DELETE requests usually don't return any data. All others do return data. For easy handling the return values consists of metadata denoted with and underscore (\"_\") like `_links` or `_pagination`. The actual data is returned in a field called `data`. For convenience reasons this `data` field is always returned as an array even if it consists of only one single element.  Some general details about Contabo API from [Contabo](https://contabo.com).   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@contabo.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreateInstanceRequest(object):
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
        'product_id': 'str',
        'region': 'str',
        'ssh_keys': 'list[int]',
        'root_password': 'int',
        'user_data': 'str',
        'license': 'str',
        'period': 'int'
    }

    attribute_map = {
        'image_id': 'imageId',
        'product_id': 'productId',
        'region': 'region',
        'ssh_keys': 'sshKeys',
        'root_password': 'rootPassword',
        'user_data': 'userData',
        'license': 'license',
        'period': 'period'
    }

    def __init__(self, image_id='db1409d2-ed92-4f2f-978e-7b2fa4a1ec90', product_id='V1', region='EU', ssh_keys=None, root_password=None, user_data=None, license=None, period=1):  # noqa: E501
        """CreateInstanceRequest - a model defined in Swagger"""  # noqa: E501
        self._image_id = None
        self._product_id = None
        self._region = None
        self._ssh_keys = None
        self._root_password = None
        self._user_data = None
        self._license = None
        self._period = None
        self.discriminator = None
        self.image_id = image_id
        self.product_id = product_id
        self.region = region
        if ssh_keys is not None:
            self.ssh_keys = ssh_keys
        if root_password is not None:
            self.root_password = root_password
        if user_data is not None:
            self.user_data = user_data
        if license is not None:
            self.license = license
        self.period = period

    @property
    def image_id(self):
        """Gets the image_id of this CreateInstanceRequest.  # noqa: E501

        ImageId to be used to setup the compute instance. Default is Ubuntu 20.04  # noqa: E501

        :return: The image_id of this CreateInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this CreateInstanceRequest.

        ImageId to be used to setup the compute instance. Default is Ubuntu 20.04  # noqa: E501

        :param image_id: The image_id of this CreateInstanceRequest.  # noqa: E501
        :type: str
        """
        if image_id is None:
            raise ValueError("Invalid value for `image_id`, must not be `None`")  # noqa: E501

        self._image_id = image_id

    @property
    def product_id(self):
        """Gets the product_id of this CreateInstanceRequest.  # noqa: E501

        You can find `productId`s [here](https://contabo.com/en/product-list/?show_ids=true). Default is V1  # noqa: E501

        :return: The product_id of this CreateInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this CreateInstanceRequest.

        You can find `productId`s [here](https://contabo.com/en/product-list/?show_ids=true). Default is V1  # noqa: E501

        :param product_id: The product_id of this CreateInstanceRequest.  # noqa: E501
        :type: str
        """
        if product_id is None:
            raise ValueError("Invalid value for `product_id`, must not be `None`")  # noqa: E501

        self._product_id = product_id

    @property
    def region(self):
        """Gets the region of this CreateInstanceRequest.  # noqa: E501

        Instance Region where the compute instance should be located. Default is EU  # noqa: E501

        :return: The region of this CreateInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CreateInstanceRequest.

        Instance Region where the compute instance should be located. Default is EU  # noqa: E501

        :param region: The region of this CreateInstanceRequest.  # noqa: E501
        :type: str
        """
        if region is None:
            raise ValueError("Invalid value for `region`, must not be `None`")  # noqa: E501
        allowed_values = ["EU", "US-central", "US-east", "US-west", "SIN"]  # noqa: E501
        if region not in allowed_values:
            raise ValueError(
                "Invalid value for `region` ({0}), must be one of {1}"  # noqa: E501
                .format(region, allowed_values)
            )

        self._region = region

    @property
    def ssh_keys(self):
        """Gets the ssh_keys of this CreateInstanceRequest.  # noqa: E501

        Array of ids of public SSH Keys in order to access as admin user with root privileges (via sudo). Applies to Linux/BSD systems. Please refer to Secrets Management API.  # noqa: E501

        :return: The ssh_keys of this CreateInstanceRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._ssh_keys

    @ssh_keys.setter
    def ssh_keys(self, ssh_keys):
        """Sets the ssh_keys of this CreateInstanceRequest.

        Array of ids of public SSH Keys in order to access as admin user with root privileges (via sudo). Applies to Linux/BSD systems. Please refer to Secrets Management API.  # noqa: E501

        :param ssh_keys: The ssh_keys of this CreateInstanceRequest.  # noqa: E501
        :type: list[int]
        """

        self._ssh_keys = ssh_keys

    @property
    def root_password(self):
        """Gets the root_password of this CreateInstanceRequest.  # noqa: E501

        Password id for admin user with administrator/root privileges. For Linux/BSD please use SSH, for Windows RDP. Please refer to Secrets Management API.  # noqa: E501

        :return: The root_password of this CreateInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._root_password

    @root_password.setter
    def root_password(self, root_password):
        """Sets the root_password of this CreateInstanceRequest.

        Password id for admin user with administrator/root privileges. For Linux/BSD please use SSH, for Windows RDP. Please refer to Secrets Management API.  # noqa: E501

        :param root_password: The root_password of this CreateInstanceRequest.  # noqa: E501
        :type: int
        """

        self._root_password = root_password

    @property
    def user_data(self):
        """Gets the user_data of this CreateInstanceRequest.  # noqa: E501

        [Cloud-Init](https://cloud-init.io/) Config in order to customize during start of compute instance.  # noqa: E501

        :return: The user_data of this CreateInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this CreateInstanceRequest.

        [Cloud-Init](https://cloud-init.io/) Config in order to customize during start of compute instance.  # noqa: E501

        :param user_data: The user_data of this CreateInstanceRequest.  # noqa: E501
        :type: str
        """

        self._user_data = user_data

    @property
    def license(self):
        """Gets the license of this CreateInstanceRequest.  # noqa: E501

        Additional licence in order to enhance your chosen product, mainly needed for software licenses on your product (not needed for windows).  # noqa: E501

        :return: The license of this CreateInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this CreateInstanceRequest.

        Additional licence in order to enhance your chosen product, mainly needed for software licenses on your product (not needed for windows).  # noqa: E501

        :param license: The license of this CreateInstanceRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["PleskHost", "PleskPro", "PleskAdmin", "cPanel5", "cPanel30", "cPanel50", "cPanel100", "cPanel150", "cPanel200", "cPanel250", "cPanel300", "cPanel350", "cPanel400", "cPanel450", "cPanel500", "cPanel550", "cPanel600", "cPanel650", "cPanel700", "cPanel750", "cPanel800", "cPanel850", "cPanel900", "cPanel950", "cPanel1000"]  # noqa: E501
        if license not in allowed_values:
            raise ValueError(
                "Invalid value for `license` ({0}), must be one of {1}"  # noqa: E501
                .format(license, allowed_values)
            )

        self._license = license

    @property
    def period(self):
        """Gets the period of this CreateInstanceRequest.  # noqa: E501

        Initial contract period in months. Available periods are: 1, 3, 6 and 12 months. Default to 1 month  # noqa: E501

        :return: The period of this CreateInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this CreateInstanceRequest.

        Initial contract period in months. Available periods are: 1, 3, 6 and 12 months. Default to 1 month  # noqa: E501

        :param period: The period of this CreateInstanceRequest.  # noqa: E501
        :type: int
        """
        if period is None:
            raise ValueError("Invalid value for `period`, must not be `None`")  # noqa: E501

        self._period = period

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
        if issubclass(CreateInstanceRequest, dict):
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
        if not isinstance(other, CreateInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
