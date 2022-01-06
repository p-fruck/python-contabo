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

class InstanceResponse(object):
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
        'name': 'str',
        'instance_id': 'int',
        'region': 'str',
        'product_id': 'str',
        'image_id': 'str',
        'ip_config': 'IpConfig',
        'mac_address': 'str',
        'ram_mb': 'float',
        'cpu_cores': 'int',
        'os_type': 'str',
        'disk_mb': 'float',
        'ssh_keys': 'list[str]',
        'created_date': 'datetime',
        'cancel_date': 'date',
        'status': 'InstanceStatus',
        'v_host_id': 'int',
        'add_ons': 'list[AddOnResponse]',
        'error_message': 'str',
        'product_type': 'str'
    }

    attribute_map = {
        'tenant_id': 'tenantId',
        'customer_id': 'customerId',
        'name': 'name',
        'instance_id': 'instanceId',
        'region': 'region',
        'product_id': 'productId',
        'image_id': 'imageId',
        'ip_config': 'ipConfig',
        'mac_address': 'macAddress',
        'ram_mb': 'ramMb',
        'cpu_cores': 'cpuCores',
        'os_type': 'osType',
        'disk_mb': 'diskMb',
        'ssh_keys': 'sshKeys',
        'created_date': 'createdDate',
        'cancel_date': 'cancelDate',
        'status': 'status',
        'v_host_id': 'vHostId',
        'add_ons': 'addOns',
        'error_message': 'errorMessage',
        'product_type': 'productType'
    }

    def __init__(self, tenant_id=None, customer_id=None, name=None, instance_id=None, region=None, product_id=None, image_id=None, ip_config=None, mac_address=None, ram_mb=None, cpu_cores=None, os_type=None, disk_mb=None, ssh_keys=None, created_date=None, cancel_date=None, status=None, v_host_id=None, add_ons=None, error_message=None, product_type=None):  # noqa: E501
        """InstanceResponse - a model defined in Swagger"""  # noqa: E501
        self._tenant_id = None
        self._customer_id = None
        self._name = None
        self._instance_id = None
        self._region = None
        self._product_id = None
        self._image_id = None
        self._ip_config = None
        self._mac_address = None
        self._ram_mb = None
        self._cpu_cores = None
        self._os_type = None
        self._disk_mb = None
        self._ssh_keys = None
        self._created_date = None
        self._cancel_date = None
        self._status = None
        self._v_host_id = None
        self._add_ons = None
        self._error_message = None
        self._product_type = None
        self.discriminator = None
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if customer_id is not None:
            self.customer_id = customer_id
        if name is not None:
            self.name = name
        if instance_id is not None:
            self.instance_id = instance_id
        if region is not None:
            self.region = region
        if product_id is not None:
            self.product_id = product_id
        if image_id is not None:
            self.image_id = image_id
        if ip_config is not None:
            self.ip_config = ip_config
        if mac_address is not None:
            self.mac_address = mac_address
        if ram_mb is not None:
            self.ram_mb = ram_mb
        if cpu_cores is not None:
            self.cpu_cores = cpu_cores
        if os_type is not None:
            self.os_type = os_type
        if disk_mb is not None:
            self.disk_mb = disk_mb
        if ssh_keys is not None:
            self.ssh_keys = ssh_keys
        if created_date is not None:
            self.created_date = created_date
        if cancel_date is not None:
            self.cancel_date = cancel_date
        if status is not None:
            self.status = status
        if v_host_id is not None:
            self.v_host_id = v_host_id
        if add_ons is not None:
            self.add_ons = add_ons
        if error_message is not None:
            if error_message is not None:
                self.error_message = error_message
        if product_type is not None:
            self.product_type = product_type

    @property
    def tenant_id(self):
        """Gets the tenant_id of this InstanceResponse.  # noqa: E501

        Your customer tenant id  # noqa: E501

        :return: The tenant_id of this InstanceResponse.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this InstanceResponse.

        Your customer tenant id  # noqa: E501

        :param tenant_id: The tenant_id of this InstanceResponse.  # noqa: E501
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
        """Gets the customer_id of this InstanceResponse.  # noqa: E501

        Customer ID  # noqa: E501

        :return: The customer_id of this InstanceResponse.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this InstanceResponse.

        Customer ID  # noqa: E501

        :param customer_id: The customer_id of this InstanceResponse.  # noqa: E501
        :type: str
        """
        if customer_id is None:
            raise ValueError("Invalid value for `customer_id`, must not be `None`")  # noqa: E501

        self._customer_id = customer_id

    @property
    def name(self):
        """Gets the name of this InstanceResponse.  # noqa: E501

        Instance Name  # noqa: E501

        :return: The name of this InstanceResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InstanceResponse.

        Instance Name  # noqa: E501

        :param name: The name of this InstanceResponse.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def instance_id(self):
        """Gets the instance_id of this InstanceResponse.  # noqa: E501

        Instance ID  # noqa: E501

        :return: The instance_id of this InstanceResponse.  # noqa: E501
        :rtype: int
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this InstanceResponse.

        Instance ID  # noqa: E501

        :param instance_id: The instance_id of this InstanceResponse.  # noqa: E501
        :type: int
        """
        if instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def region(self):
        """Gets the region of this InstanceResponse.  # noqa: E501

        Instance Region where the compute instance should be located.  # noqa: E501

        :return: The region of this InstanceResponse.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this InstanceResponse.

        Instance Region where the compute instance should be located.  # noqa: E501

        :param region: The region of this InstanceResponse.  # noqa: E501
        :type: str
        """
        if region is None:
            raise ValueError("Invalid value for `region`, must not be `None`")  # noqa: E501

        self._region = region

    @property
    def product_id(self):
        """Gets the product_id of this InstanceResponse.  # noqa: E501

        Product ID  # noqa: E501

        :return: The product_id of this InstanceResponse.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this InstanceResponse.

        Product ID  # noqa: E501

        :param product_id: The product_id of this InstanceResponse.  # noqa: E501
        :type: str
        """
        if product_id is None:
            raise ValueError("Invalid value for `product_id`, must not be `None`")  # noqa: E501

        self._product_id = product_id

    @property
    def image_id(self):
        """Gets the image_id of this InstanceResponse.  # noqa: E501

        Image's id  # noqa: E501

        :return: The image_id of this InstanceResponse.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this InstanceResponse.

        Image's id  # noqa: E501

        :param image_id: The image_id of this InstanceResponse.  # noqa: E501
        :type: str
        """
        if image_id is None:
            raise ValueError("Invalid value for `image_id`, must not be `None`")  # noqa: E501

        self._image_id = image_id

    @property
    def ip_config(self):
        """Gets the ip_config of this InstanceResponse.  # noqa: E501


        :return: The ip_config of this InstanceResponse.  # noqa: E501
        :rtype: IpConfig
        """
        return self._ip_config

    @ip_config.setter
    def ip_config(self, ip_config):
        """Sets the ip_config of this InstanceResponse.


        :param ip_config: The ip_config of this InstanceResponse.  # noqa: E501
        :type: IpConfig
        """
        if ip_config is None:
            raise ValueError("Invalid value for `ip_config`, must not be `None`")  # noqa: E501

        self._ip_config = ip_config

    @property
    def mac_address(self):
        """Gets the mac_address of this InstanceResponse.  # noqa: E501

        MAC Address  # noqa: E501

        :return: The mac_address of this InstanceResponse.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this InstanceResponse.

        MAC Address  # noqa: E501

        :param mac_address: The mac_address of this InstanceResponse.  # noqa: E501
        :type: str
        """
        if mac_address is None:
            raise ValueError("Invalid value for `mac_address`, must not be `None`")  # noqa: E501

        self._mac_address = mac_address

    @property
    def ram_mb(self):
        """Gets the ram_mb of this InstanceResponse.  # noqa: E501

        Image RAM size in MB  # noqa: E501

        :return: The ram_mb of this InstanceResponse.  # noqa: E501
        :rtype: float
        """
        return self._ram_mb

    @ram_mb.setter
    def ram_mb(self, ram_mb):
        """Sets the ram_mb of this InstanceResponse.

        Image RAM size in MB  # noqa: E501

        :param ram_mb: The ram_mb of this InstanceResponse.  # noqa: E501
        :type: float
        """
        if ram_mb is None:
            raise ValueError("Invalid value for `ram_mb`, must not be `None`")  # noqa: E501

        self._ram_mb = ram_mb

    @property
    def cpu_cores(self):
        """Gets the cpu_cores of this InstanceResponse.  # noqa: E501

        CPU core count  # noqa: E501

        :return: The cpu_cores of this InstanceResponse.  # noqa: E501
        :rtype: int
        """
        return self._cpu_cores

    @cpu_cores.setter
    def cpu_cores(self, cpu_cores):
        """Sets the cpu_cores of this InstanceResponse.

        CPU core count  # noqa: E501

        :param cpu_cores: The cpu_cores of this InstanceResponse.  # noqa: E501
        :type: int
        """
        if cpu_cores is None:
            raise ValueError("Invalid value for `cpu_cores`, must not be `None`")  # noqa: E501

        self._cpu_cores = cpu_cores

    @property
    def os_type(self):
        """Gets the os_type of this InstanceResponse.  # noqa: E501

        Type of operating system (OS)  # noqa: E501

        :return: The os_type of this InstanceResponse.  # noqa: E501
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this InstanceResponse.

        Type of operating system (OS)  # noqa: E501

        :param os_type: The os_type of this InstanceResponse.  # noqa: E501
        :type: str
        """
        if os_type is None:
            raise ValueError("Invalid value for `os_type`, must not be `None`")  # noqa: E501

        self._os_type = os_type

    @property
    def disk_mb(self):
        """Gets the disk_mb of this InstanceResponse.  # noqa: E501

        Image Disk size in MB  # noqa: E501

        :return: The disk_mb of this InstanceResponse.  # noqa: E501
        :rtype: float
        """
        return self._disk_mb

    @disk_mb.setter
    def disk_mb(self, disk_mb):
        """Sets the disk_mb of this InstanceResponse.

        Image Disk size in MB  # noqa: E501

        :param disk_mb: The disk_mb of this InstanceResponse.  # noqa: E501
        :type: float
        """
        if disk_mb is None:
            raise ValueError("Invalid value for `disk_mb`, must not be `None`")  # noqa: E501

        self._disk_mb = disk_mb

    @property
    def ssh_keys(self):
        """Gets the ssh_keys of this InstanceResponse.  # noqa: E501

        Array of ids of public SSH Keys in order to access as admin user with root privileges (via sudo). Applies to Linux/BSD systems. Please refer to Secrets Management API.  # noqa: E501

        :return: The ssh_keys of this InstanceResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._ssh_keys

    @ssh_keys.setter
    def ssh_keys(self, ssh_keys):
        """Sets the ssh_keys of this InstanceResponse.

        Array of ids of public SSH Keys in order to access as admin user with root privileges (via sudo). Applies to Linux/BSD systems. Please refer to Secrets Management API.  # noqa: E501

        :param ssh_keys: The ssh_keys of this InstanceResponse.  # noqa: E501
        :type: list[str]
        """
        if ssh_keys is None:
            raise ValueError("Invalid value for `ssh_keys`, must not be `None`")  # noqa: E501

        self._ssh_keys = ssh_keys

    @property
    def created_date(self):
        """Gets the created_date of this InstanceResponse.  # noqa: E501

        The creation date for the instance  # noqa: E501

        :return: The created_date of this InstanceResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this InstanceResponse.

        The creation date for the instance  # noqa: E501

        :param created_date: The created_date of this InstanceResponse.  # noqa: E501
        :type: datetime
        """
        if created_date is None:
            raise ValueError("Invalid value for `created_date`, must not be `None`")  # noqa: E501

        self._created_date = created_date

    @property
    def cancel_date(self):
        """Gets the cancel_date of this InstanceResponse.  # noqa: E501

        The date on which the instance will be cancelled  # noqa: E501

        :return: The cancel_date of this InstanceResponse.  # noqa: E501
        :rtype: date
        """
        return self._cancel_date

    @cancel_date.setter
    def cancel_date(self, cancel_date):
        """Sets the cancel_date of this InstanceResponse.

        The date on which the instance will be cancelled  # noqa: E501

        :param cancel_date: The cancel_date of this InstanceResponse.  # noqa: E501
        :type: date
        """
        if cancel_date is None:
            raise ValueError("Invalid value for `cancel_date`, must not be `None`")  # noqa: E501

        self._cancel_date = cancel_date

    @property
    def status(self):
        """Gets the status of this InstanceResponse.  # noqa: E501


        :return: The status of this InstanceResponse.  # noqa: E501
        :rtype: InstanceStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InstanceResponse.


        :param status: The status of this InstanceResponse.  # noqa: E501
        :type: InstanceStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def v_host_id(self):
        """Gets the v_host_id of this InstanceResponse.  # noqa: E501

        ID of host system  # noqa: E501

        :return: The v_host_id of this InstanceResponse.  # noqa: E501
        :rtype: int
        """
        return self._v_host_id

    @v_host_id.setter
    def v_host_id(self, v_host_id):
        """Sets the v_host_id of this InstanceResponse.

        ID of host system  # noqa: E501

        :param v_host_id: The v_host_id of this InstanceResponse.  # noqa: E501
        :type: int
        """
        if v_host_id is None:
            raise ValueError("Invalid value for `v_host_id`, must not be `None`")  # noqa: E501

        self._v_host_id = v_host_id

    @property
    def add_ons(self):
        """Gets the add_ons of this InstanceResponse.  # noqa: E501


        :return: The add_ons of this InstanceResponse.  # noqa: E501
        :rtype: list[AddOnResponse]
        """
        return self._add_ons

    @add_ons.setter
    def add_ons(self, add_ons):
        """Sets the add_ons of this InstanceResponse.


        :param add_ons: The add_ons of this InstanceResponse.  # noqa: E501
        :type: list[AddOnResponse]
        """
        if add_ons is None:
            raise ValueError("Invalid value for `add_ons`, must not be `None`")  # noqa: E501

        self._add_ons = add_ons

    @property
    def error_message(self):
        """Gets the error_message of this InstanceResponse.  # noqa: E501

        Message in case of an error.  # noqa: E501

        :return: The error_message of this InstanceResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this InstanceResponse.

        Message in case of an error.  # noqa: E501

        :param error_message: The error_message of this InstanceResponse.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def product_type(self):
        """Gets the product_type of this InstanceResponse.  # noqa: E501

        Instance's category depending on Product Id  # noqa: E501

        :return: The product_type of this InstanceResponse.  # noqa: E501
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this InstanceResponse.

        Instance's category depending on Product Id  # noqa: E501

        :param product_type: The product_type of this InstanceResponse.  # noqa: E501
        :type: str
        """
        if product_type is None:
            raise ValueError("Invalid value for `product_type`, must not be `None`")  # noqa: E501
        allowed_values = ["hdd", "ssd", "vds", "nvme"]  # noqa: E501
        if product_type not in allowed_values:
            raise ValueError(
                "Invalid value for `product_type` ({0}), must be one of {1}"  # noqa: E501
                .format(product_type, allowed_values)
            )

        self._product_type = product_type

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
        if issubclass(InstanceResponse, dict):
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
        if not isinstance(other, InstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
