# coding: utf-8

"""
    Contabo API

    # Introduction  Contabo API allows you to manage your resources using HTTP requests. This documentation includes a set of HTTP endpoints that are designed to RESTful principles. Each endpoint includes descriptions, request syntax, and examples.  Contabo provides also a CLI tool which enables you to manage your resources easily from the command line. [CLI Download and  Installation instructions.](https://github.com/contabo/cntb)  ## Getting Started  In order to use the Contabo API you will need the following credentials which are available from the [Customer Control Panel](https://my.contabo.com/api/details): 1. ClientId 2. ClientSecret 3. API User (your email address to login to the [Customer Control Panel](https://my.contabo.com/api/details)) 4. API Password (this is a new password which you'll set or change in the [Customer Control Panel](https://my.contabo.com/api/details))  You can either use the API directly or by using the `cntb` CLI (Command Line Interface) tool.  ### Using the API directly  #### Via `curl` for Linux/Unix like systems  This requires `curl` and `jq` in your shell (e.g. `bash`, `zsh`). Please replace the first four placeholders with actual values.  ```sh CLIENT_ID=<ClientId from Customer Control Panel> CLIENT_SECRET=<ClientSecret from Customer Control Panel> API_USER=<API User from Customer Control Panel> API_PASSWORD=<API Password from Customer Control Panel> ACCESS_TOKEN=$(curl -d \"client_id=$CLIENT_ID\" -d \"client_secret=$CLIENT_SECRET\" --data-urlencode \"username=$API_USER\" --data-urlencode \"password=$API_PASSWORD\" -d 'grant_type=password' 'https://auth.contabo.com/auth/realms/contabo/protocol/openid-connect/token' | jq -r '.access_token') # get list of your instances curl -X GET -H \"Authorization: Bearer $ACCESS_TOKEN\" -H \"x-request-id: 51A87ECD-754E-4104-9C54-D01AD0F83406\" \"https://api.contabo.com/v1/compute/instances\" | jq ```  #### Via `PowerShell` for Windows  Please open `PowerShell` and execute the following code after replacing the first four placeholders with actual values.  ```powershell $client_id='<ClientId from Customer Control Panel>' $client_secret='<ClientSecret from Customer Control Panel>' $api_user='<API User from Customer Control Panel>' $api_password='<API Password from Customer Control Panel>' $body = @{grant_type='password' client_id=$client_id client_secret=$client_secret username=$api_user password=$api_password} $response = Invoke-WebRequest -Uri 'https://auth.contabo.com/auth/realms/contabo/protocol/openid-connect/token' -Method 'POST' -Body $body $access_token = (ConvertFrom-Json $([String]::new($response.Content))).access_token # get list of your instances $headers = @{} $headers.Add(\"Authorization\",\"Bearer $access_token\") $headers.Add(\"x-request-id\",\"51A87ECD-754E-4104-9C54-D01AD0F83406\") Invoke-WebRequest -Uri 'https://api.contabo.com/v1/compute/instances' -Method 'GET' -Headers $headers ```  ### Using the Contabo API via the `cntb` CLI tool  1. Download `cntb` for your operating system (MacOS, Windows and Linux supported) [here](https://github.com/contabo/cntb) 2. Unzip the downloaded file 3. You might move the executable to any location on your disk. You may update your `PATH` environment variable for easier invocation. 4. Configure it once to use your credentials           ```sh    cntb config set-credentials --oauth2-clientid=<ClientId from Customer Control Panel> --oauth2-client-secret=<ClientSecret from Customer Control Panel> --oauth2-user=<API User from Customer Control Panel> --oauth2-password=<API Password from Customer Control Panel>    ```  5. Use the CLI           ```sh    # get list of your instances    cntb get instances    # help    cntb help    ```  ## API Overiew  ### [Compute Mangement](#tag/Instances)  The Compute Management API allows you to manage compute resources (e.g. creation, deletion, starting, stopping) as well as managing snapshots and custom images. It also offers you to take advantage of [cloud-init](https://cloud-init.io/) at least on our default / standard images (for custom images you'll need to provide cloud-init support packages). The API offers provisioning of cloud-init scripts via the `user_data` field.  Custom images must be provided in `.qcow2` or `.iso` format. This gives you even more flexibilty for setting up your environment.  ### [Secrets Mangement](#tag/Secrets)  You can optionally save your passwords or public ssh keys using the Secrets Managemnt API. You are not required to use it there will be no functional disadvantages.  By using that API you can easily reuse you public ssh keys when setting up different servers without the need to look them up every time. It can also be used to allow Contabo Supporters to access your machine without sending the passwords via potentially unsecure emails.  ### [User Management](#tag/Users)  If you need to allow other persons or automation scripts to access specific API endpoints resp. resources the User Mangement API comes into play. With that API you are able to manage users having possibly restricted access. You are free to define those restrictions to fit your needs. So beside an arbitrary number of users you basically define any number of so called `roles`. Roles allows access and must be one of the following types:  * `apiPermission`          This allows you to specify a restriction to certain functions of an API by allowing control over POST (=Create), GET (=Read), PUT/PATCH (=Update) and DELETE (=Delete) methods for each API endpoint (URL) individually. * `resourcePermission`          In order to restrict access to specific resources create a role with `resourcePermission` type by specifying any number of [tags](#tag-management). These tags need to be assigned to resources for them to take effect. E.g. a tag could be assiged to several compute resources. So that a user with that role (and of course access to the API endpoints via `apiPermission` role type) could only access those compute resources.  The `roles` are then assigned to a `user`. You can assign one or several roles regardless of the role's type. Of course you could also assign a user `admin` privileges without specifying any roles.  ### [Tag Management](#tag/Tags)  The Tag Management API allows you to manage your tags in order to organize your resources in a more convenient way. Simply assign a tag to resources like a compute resource to manage them.The assignments of tags to resources will also enable you to control access to these specific resources to users via the [User Management API](#user-management). For convenience reasons you might choose a color for tag. The Customer Control Panel will use that color to display the tags.  ## Requests  The Contabo API supports HTTP requests like mentioned below. Not every endpoint supports all methods. The allowed methods are listed within this documentation.  Method | Description ---    | --- GET    | To retrieve information about a resource, use the GET method.<br>The data is returned as a JSON object. GET methods are read-only and do not affect any resources. POST   | Issue a POST method to create a new object. Include all needed attributes in the request body encoded as JSON. PATCH  | Some resources support partial modification with PATCH,<br>which modifies specific attributes without updating the entire object representation. PUT    | Use the PUT method to update information about a resource.<br>PUT will set new values on the item without regard to their current values. DELETE | Use the DELETE method to destroy a resource in your account.<br>If it is not found, the operation will return a 4xx error and an appropriate message.  ## Responses  Usually the Contabo API should respond to your requests. The data returned is in [JSON](https://www.json.org/) format allowing easy processing in any programming language or tools.  As common for HTTP requests you will get back a so called HTTP status code. This gives you overall information about success or error. The following table lists common HTTP status codes.  Please note that the description of the endpoints and methods are not listing all possibly status codes in detail as they are generic. Only special return codes with their resp. response data are explicitly listed.  Response Code | Description --- | --- 200 | The response contains your requested information. 201 | Your request was accepted. The resource was created. 204 | Your request succeeded, there is no additional information returned. 400 | Your request was malformed. 401 | You did not supply valid authentication credentials. 402 | Request refused as it requires additional payed service. 403 | You are not allowed to perform the request. 404 | No results were found for your request or resource does not exist. 409 | Conflict with resources. For example violation of unique data contraints detected when trying to create or change resources. 429 | Rate-limit reached. Please wait for some time before doing more requests. 500 | We were unable to perform the request due to server-side problems. In such cases please retry or contact the support.  Not every endpoint returns data. For example DELETE requests usually don't return any data. All others do return data. For easy handling the return values consists of metadata denoted with and underscore (\"_\") like `_links` or `_pagination`. The actual data is returned in a field called `data`. For convenience reasons this `data` field is always returned as an array even if it consists of only one single element.  Some general details about Contabo API from [Contabo](https://contabo.com).   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@contabo.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "pfruck_contabo"
VERSION = "1.0.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="This is an UNOFFICIAL Python API client for Contabo",
    author_email="support@contabo.com",
    url="https://github.com/p-fruck/python-contabo",
    keywords=["Swagger", "Contabo API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
# pfruck_contabo

> ⚠️ I am not affiliated in any way with Contabo

This is an UNOFFICIAL Python API client for [contabo.com](https://contabo.com), which is a hosting provider for VPS and dedicated servers.

The goal of this client is to make management of your server instances more easy using a native Python API for the freshly released [Contabo API](https://api.contabo.com/).
This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project.

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

The simplest way to install the Contabo API client is by using the provided [pip package](https://pypi.org/project/pfruck-contabo):

```sh
pip install pfruck-contabo
```

You can also install the package directly from the GitHub Repo using pip:
```sh
pip install git+https://github.com/p-fruck/python-contabo.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/p-fruck/python-contabo.git`)

Then import the package:
```python
import pfruck_contabo
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import pfruck_contabo
```
## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.ImagesApi(pfruck_contabo.ApiClient(configuration))
body = pfruck_contabo.CreateCustomImageRequest() # CreateCustomImageRequest | 
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Provide a custom image
    api_response = api_instance.create_custom_image(body, x_request_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->create_custom_image: %s\\n" % e)


# create an instance of the API class
api_instance = pfruck_contabo.ImagesApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
image_id = 'image_id_example' # str | The identifier of the image
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Delete an uploaded custom image by its id
    api_instance.delete_image(x_request_id, image_id, x_trace_id=x_trace_id)
except ApiException as e:
    print("Exception when calling ImagesApi->delete_image: %s\\n" % e)


# create an instance of the API class
api_instance = pfruck_contabo.ImagesApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # List statistics regarding the customer's custom images
    api_response = api_instance.retrieve_custom_images_stats(x_request_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->retrieve_custom_images_stats: %s\\n" % e)


# create an instance of the API class
api_instance = pfruck_contabo.ImagesApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
image_id = 'image_id_example' # str | The identifier of the image
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Get details about a specific image by its id
    api_response = api_instance.retrieve_image(x_request_id, image_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->retrieve_image: %s\\n" % e)


# create an instance of the API class
api_instance = pfruck_contabo.ImagesApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
page = 789 # int | Number of page to be fetched. (optional)
size = 789 # int | Number of elements per page. (optional)
order_by = ['order_by_example'] # list[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
name = 'name_example' # str | The name of the image (optional)
standard_image = true # bool | Flag indicating that image is either a standard (true) or a custom image (false) (optional)

try:
    # List available standard and custom images
    api_response = api_instance.retrieve_image_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, name=name, standard_image=standard_image)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->retrieve_image_list: %s\\n" % e)


# create an instance of the API class
api_instance = pfruck_contabo.ImagesApi(pfruck_contabo.ApiClient(configuration))
body = pfruck_contabo.UpdateCustomImageRequest() # UpdateCustomImageRequest | 
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
image_id = 'image_id_example' # str | The identifier of the image
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Update custom image name by its id
    api_response = api_instance.update_image(body, x_request_id, image_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->update_image: %s\\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ImagesApi* | [**create_custom_image**](https://github.com/p-fruck/python-contabo/blob/main/docs/ImagesApi.md#create_custom_image) | **POST** /v1/compute/images | Provide a custom image
*ImagesApi* | [**delete_image**](https://github.com/p-fruck/python-contabo/blob/main/docs/ImagesApi.md#delete_image) | **DELETE** /v1/compute/images/{imageId} | Delete an uploaded custom image by its id
*ImagesApi* | [**retrieve_custom_images_stats**](https://github.com/p-fruck/python-contabo/blob/main/docs/ImagesApi.md#retrieve_custom_images_stats) | **GET** /v1/compute/images/stats | List statistics regarding the customer&#x27;s custom images
*ImagesApi* | [**retrieve_image**](https://github.com/p-fruck/python-contabo/blob/main/docs/ImagesApi.md#retrieve_image) | **GET** /v1/compute/images/{imageId} | Get details about a specific image by its id
*ImagesApi* | [**retrieve_image_list**](https://github.com/p-fruck/python-contabo/blob/main/docs/ImagesApi.md#retrieve_image_list) | **GET** /v1/compute/images | List available standard and custom images
*ImagesApi* | [**update_image**](https://github.com/p-fruck/python-contabo/blob/main/docs/ImagesApi.md#update_image) | **PATCH** /v1/compute/images/{imageId} | Update custom image name by its id
*ImagesAuditsApi* | [**retrieve_image_audits_list**](https://github.com/p-fruck/python-contabo/blob/main/docs/ImagesAuditsApi.md#retrieve_image_audits_list) | **GET** /v1/compute/images/audits | List history about your custom images (audit)
*InstanceActionsApi* | [**restart**](https://github.com/p-fruck/python-contabo/blob/main/docs/InstanceActionsApi.md#restart) | **POST** /v1/compute/instances/{instanceId}/actions/restart | Restart a compute instance / resource identified by its id
*InstanceActionsApi* | [**start**](https://github.com/p-fruck/python-contabo/blob/main/docs/InstanceActionsApi.md#start) | **POST** /v1/compute/instances/{instanceId}/actions/start | Start a compute instance / resource identified by its id
*InstanceActionsApi* | [**stop**](https://github.com/p-fruck/python-contabo/blob/main/docs/InstanceActionsApi.md#stop) | **POST** /v1/compute/instances/{instanceId}/actions/stop | Stop compute instance / resource by its id
*InstanceActionsAuditsApi* | [**retrieve_instances_actions_audits_list**](https://github.com/p-fruck/python-contabo/blob/main/docs/InstanceActionsAuditsApi.md#retrieve_instances_actions_audits_list) | **GET** /v1/compute/instances/actions/audits | List history about your actions (audit) triggered via the API
*InstancesApi* | [**cancel_instance**](https://github.com/p-fruck/python-contabo/blob/main/docs/InstancesApi.md#cancel_instance) | **POST** /v1/compute/instances/{instanceId}/cancel | Cancel specific instance by id
*InstancesApi* | [**create_instance**](https://github.com/p-fruck/python-contabo/blob/main/docs/InstancesApi.md#create_instance) | **POST** /v1/compute/instances | Create a new instance
*InstancesApi* | [**reinstall_instance**](https://github.com/p-fruck/python-contabo/blob/main/docs/InstancesApi.md#reinstall_instance) | **PATCH** /v1/compute/instances/{instanceId} | Reinstall specific instance
*InstancesApi* | [**retrieve_instance**](https://github.com/p-fruck/python-contabo/blob/main/docs/InstancesApi.md#retrieve_instance) | **GET** /v1/compute/instances/{instanceId} | Get specific instance by id
*InstancesApi* | [**retrieve_instances_list**](https://github.com/p-fruck/python-contabo/blob/main/docs/InstancesApi.md#retrieve_instances_list) | **GET** /v1/compute/instances | List instances
*InstancesAuditsApi* | [**retrieve_instances_audits_list**](https://github.com/p-fruck/python-contabo/blob/main/docs/InstancesAuditsApi.md#retrieve_instances_audits_list) | **GET** /v1/compute/instances/audits | List history about your instances (audit) triggered via the API
*RolesApi* | [**create_role**](https://github.com/p-fruck/python-contabo/blob/main/docs/RolesApi.md#create_role) | **POST** /v1/roles/{roleType} | Create a new role
*RolesApi* | [**delete_role**](https://github.com/p-fruck/python-contabo/blob/main/docs/RolesApi.md#delete_role) | **DELETE** /v1/roles/{roleType}/{roleId} | Delete existing role by id
*RolesApi* | [**retrieve_api_permissions_list**](https://github.com/p-fruck/python-contabo/blob/main/docs/RolesApi.md#retrieve_api_permissions_list) | **GET** /v1/roles/api-permissions | List of API permissions
*RolesApi* | [**retrieve_role**](https://github.com/p-fruck/python-contabo/blob/main/docs/RolesApi.md#retrieve_role) | **GET** /v1/roles/{roleType}/{roleId} | Get specific role by id
*RolesApi* | [**retrieve_role_list**](https://github.com/p-fruck/python-contabo/blob/main/docs/RolesApi.md#retrieve_role_list) | **GET** /v1/roles/{roleType} | List roles
*RolesApi* | [**update_role**](https://github.com/p-fruck/python-contabo/blob/main/docs/RolesApi.md#update_role) | **PATCH** /v1/roles/{roleType}/{roleId} | Update specific role by id
*RolesAuditsApi* | [**retrieve_role_audits_list**](https://github.com/p-fruck/python-contabo/blob/main/docs/RolesAuditsApi.md#retrieve_role_audits_list) | **GET** /v1/roles/audits | List history about your roles (audit)
*SecretsApi* | [**create_secret**](https://github.com/p-fruck/python-contabo/blob/main/docs/SecretsApi.md#create_secret) | **POST** /v1/secrets | Create a new secret
*SecretsApi* | [**delete_secret**](https://github.com/p-fruck/python-contabo/blob/main/docs/SecretsApi.md#delete_secret) | **DELETE** /v1/secrets/{secretId} | Delete existing secret by id
*SecretsApi* | [**retrieve_secret**](https://github.com/p-fruck/python-contabo/blob/main/docs/SecretsApi.md#retrieve_secret) | **GET** /v1/secrets/{secretId} | Get specific secret by id
*SecretsApi* | [**retrieve_secret_list**](https://github.com/p-fruck/python-contabo/blob/main/docs/SecretsApi.md#retrieve_secret_list) | **GET** /v1/secrets | List secrets
*SecretsApi* | [**update_secret**](https://github.com/p-fruck/python-contabo/blob/main/docs/SecretsApi.md#update_secret) | **PATCH** /v1/secrets/{secretId} | Update specific secret by id
*SecretsAuditsApi* | [**retrieve_secret_audits_list**](https://github.com/p-fruck/python-contabo/blob/main/docs/SecretsAuditsApi.md#retrieve_secret_audits_list) | **GET** /v1/secrets/audits | List history about your secrets (audit)
*SnapshotsApi* | [**create_snapshot**](https://github.com/p-fruck/python-contabo/blob/main/docs/SnapshotsApi.md#create_snapshot) | **POST** /v1/compute/instances/{instanceId}/snapshots | Create a new instance snapshot
*SnapshotsApi* | [**delete_snapshot**](https://github.com/p-fruck/python-contabo/blob/main/docs/SnapshotsApi.md#delete_snapshot) | **DELETE** /v1/compute/instances/{instanceId}/snapshots/{snapshotId} | Delete existing snapshot by id
*SnapshotsApi* | [**retrieve_snapshot**](https://github.com/p-fruck/python-contabo/blob/main/docs/SnapshotsApi.md#retrieve_snapshot) | **GET** /v1/compute/instances/{instanceId}/snapshots/{snapshotId} | Retrieve a specific snapshot by id
*SnapshotsApi* | [**retrieve_snapshot_list**](https://github.com/p-fruck/python-contabo/blob/main/docs/SnapshotsApi.md#retrieve_snapshot_list) | **GET** /v1/compute/instances/{instanceId}/snapshots | List snapshots
*SnapshotsApi* | [**rollback_snapshot**](https://github.com/p-fruck/python-contabo/blob/main/docs/SnapshotsApi.md#rollback_snapshot) | **POST** /v1/compute/instances/{instanceId}/snapshots/{snapshotId}/rollback | Rollback the instance to a specific snapshot by id
*SnapshotsApi* | [**update_snapshot**](https://github.com/p-fruck/python-contabo/blob/main/docs/SnapshotsApi.md#update_snapshot) | **PATCH** /v1/compute/instances/{instanceId}/snapshots/{snapshotId} | Update specific snapshot by id
*SnapshotsAuditsApi* | [**retrieve_snapshots_audits_list**](https://github.com/p-fruck/python-contabo/blob/main/docs/SnapshotsAuditsApi.md#retrieve_snapshots_audits_list) | **GET** /v1/compute/snapshots/audits | List history about your snapshots (audit) triggered via the API
*TagAssignmentsApi* | [**create_assignment**](https://github.com/p-fruck/python-contabo/blob/main/docs/TagAssignmentsApi.md#create_assignment) | **POST** /v1/tags/{tagId}/assignments/{resourceType}/{resourceId} | Create a new assignment for the tag
*TagAssignmentsApi* | [**delete_assignment**](https://github.com/p-fruck/python-contabo/blob/main/docs/TagAssignmentsApi.md#delete_assignment) | **DELETE** /v1/tags/{tagId}/assignments/{resourceType}/{resourceId} | Delete existing tag assignment
*TagAssignmentsApi* | [**retrieve_assignment**](https://github.com/p-fruck/python-contabo/blob/main/docs/TagAssignmentsApi.md#retrieve_assignment) | **GET** /v1/tags/{tagId}/assignments/{resourceType}/{resourceId} | Get specific assignment for the tag
*TagAssignmentsApi* | [**retrieve_assignment_list**](https://github.com/p-fruck/python-contabo/blob/main/docs/TagAssignmentsApi.md#retrieve_assignment_list) | **GET** /v1/tags/{tagId}/assignments | List tag assignments
*TagAssignmentsAuditsApi* | [**retrieve_assignments_audits_list**](https://github.com/p-fruck/python-contabo/blob/main/docs/TagAssignmentsAuditsApi.md#retrieve_assignments_audits_list) | **GET** /v1/tags/assignments/audits | List history about your assignments (audit)
*TagsApi* | [**create_tag**](https://github.com/p-fruck/python-contabo/blob/main/docs/TagsApi.md#create_tag) | **POST** /v1/tags | Create a new tag
*TagsApi* | [**delete_tag**](https://github.com/p-fruck/python-contabo/blob/main/docs/TagsApi.md#delete_tag) | **DELETE** /v1/tags/{tagId} | Delete existing tag by id
*TagsApi* | [**retrieve_tag**](https://github.com/p-fruck/python-contabo/blob/main/docs/TagsApi.md#retrieve_tag) | **GET** /v1/tags/{tagId} | Get specific tag by id
*TagsApi* | [**retrieve_tag_list**](https://github.com/p-fruck/python-contabo/blob/main/docs/TagsApi.md#retrieve_tag_list) | **GET** /v1/tags | List tags
*TagsApi* | [**update_tag**](https://github.com/p-fruck/python-contabo/blob/main/docs/TagsApi.md#update_tag) | **PATCH** /v1/tags/{tagId} | Update specific tag by id
*TagsAuditsApi* | [**retrieve_tag_audits_list**](https://github.com/p-fruck/python-contabo/blob/main/docs/TagsAuditsApi.md#retrieve_tag_audits_list) | **GET** /v1/tags/audits | List history about your tags (audit)
*UsersApi* | [**create_user**](https://github.com/p-fruck/python-contabo/blob/main/docs/UsersApi.md#create_user) | **POST** /v1/users | Create a new user
*UsersApi* | [**delete_user**](https://github.com/p-fruck/python-contabo/blob/main/docs/UsersApi.md#delete_user) | **DELETE** /v1/users/{userId} | Delete existing user by id
*UsersApi* | [**generate_client_secret**](https://github.com/p-fruck/python-contabo/blob/main/docs/UsersApi.md#generate_client_secret) | **PUT** /v1/users/client/secret | Generate new client secret
*UsersApi* | [**resend_email_verification**](https://github.com/p-fruck/python-contabo/blob/main/docs/UsersApi.md#resend_email_verification) | **POST** /v1/users/{userId}/resend-email-verification | Resend email verification
*UsersApi* | [**reset_password**](https://github.com/p-fruck/python-contabo/blob/main/docs/UsersApi.md#reset_password) | **POST** /v1/users/{userId}/reset-password | Send reset password email
*UsersApi* | [**retrieve_user**](https://github.com/p-fruck/python-contabo/blob/main/docs/UsersApi.md#retrieve_user) | **GET** /v1/users/{userId} | Get specific user by id
*UsersApi* | [**retrieve_user_client**](https://github.com/p-fruck/python-contabo/blob/main/docs/UsersApi.md#retrieve_user_client) | **GET** /v1/users/client | Get client
*UsersApi* | [**retrieve_user_is_password_set**](https://github.com/p-fruck/python-contabo/blob/main/docs/UsersApi.md#retrieve_user_is_password_set) | **GET** /v1/users/is-password-set | Get user is password set status
*UsersApi* | [**retrieve_user_list**](https://github.com/p-fruck/python-contabo/blob/main/docs/UsersApi.md#retrieve_user_list) | **GET** /v1/users | List users
*UsersApi* | [**update_user**](https://github.com/p-fruck/python-contabo/blob/main/docs/UsersApi.md#update_user) | **PATCH** /v1/users/{userId} | Update specific user by id
*UsersAuditsApi* | [**retrieve_user_audits_list**](https://github.com/p-fruck/python-contabo/blob/main/docs/UsersAuditsApi.md#retrieve_user_audits_list) | **GET** /v1/users/audits | List history about your users (audit)

## Documentation For Models

 - [AddOnResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/AddOnResponse.md)
 - [AllOfCancelInstanceResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfCancelInstanceResponseLinks.md)
 - [AllOfCreateAssignmentResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfCreateAssignmentResponseLinks.md)
 - [AllOfCreateCustomImageResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfCreateCustomImageResponseLinks.md)
 - [AllOfCreateInstanceResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfCreateInstanceResponseLinks.md)
 - [AllOfCreateRoleResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfCreateRoleResponseLinks.md)
 - [AllOfCreateSecretResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfCreateSecretResponseLinks.md)
 - [AllOfCreateSnapshotResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfCreateSnapshotResponseLinks.md)
 - [AllOfCreateTagResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfCreateTagResponseLinks.md)
 - [AllOfCreateUserResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfCreateUserResponseLinks.md)
 - [AllOfCustomImagesStatsResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfCustomImagesStatsResponseLinks.md)
 - [AllOfFindAssignmentResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfFindAssignmentResponseLinks.md)
 - [AllOfFindClientResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfFindClientResponseLinks.md)
 - [AllOfFindImageResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfFindImageResponseLinks.md)
 - [AllOfFindInstanceResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfFindInstanceResponseLinks.md)
 - [AllOfFindRoleResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfFindRoleResponseLinks.md)
 - [AllOfFindSecretResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfFindSecretResponseLinks.md)
 - [AllOfFindSnapshotResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfFindSnapshotResponseLinks.md)
 - [AllOfFindTagResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfFindTagResponseLinks.md)
 - [AllOfFindUserIsPasswordSetResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfFindUserIsPasswordSetResponseLinks.md)
 - [AllOfFindUserResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfFindUserResponseLinks.md)
 - [AllOfGenerateClientSecretResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfGenerateClientSecretResponseLinks.md)
 - [AllOfImageAuditResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfImageAuditResponseLinks.md)
 - [AllOfImageAuditResponsePagination](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfImageAuditResponsePagination.md)
 - [AllOfInstanceRestartActionResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfInstanceRestartActionResponseLinks.md)
 - [AllOfInstanceStartActionResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfInstanceStartActionResponseLinks.md)
 - [AllOfInstanceStopActionResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfInstanceStopActionResponseLinks.md)
 - [AllOfListApiPermissionResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListApiPermissionResponseLinks.md)
 - [AllOfListAssignmentAuditsResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListAssignmentAuditsResponseLinks.md)
 - [AllOfListAssignmentAuditsResponsePagination](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListAssignmentAuditsResponsePagination.md)
 - [AllOfListAssignmentResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListAssignmentResponseLinks.md)
 - [AllOfListAssignmentResponsePagination](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListAssignmentResponsePagination.md)
 - [AllOfListImageResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListImageResponseLinks.md)
 - [AllOfListImageResponsePagination](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListImageResponsePagination.md)
 - [AllOfListInstancesActionsAuditResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListInstancesActionsAuditResponseLinks.md)
 - [AllOfListInstancesActionsAuditResponsePagination](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListInstancesActionsAuditResponsePagination.md)
 - [AllOfListInstancesAuditResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListInstancesAuditResponseLinks.md)
 - [AllOfListInstancesAuditResponsePagination](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListInstancesAuditResponsePagination.md)
 - [AllOfListInstancesResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListInstancesResponseLinks.md)
 - [AllOfListInstancesResponsePagination](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListInstancesResponsePagination.md)
 - [AllOfListRoleAuditResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListRoleAuditResponseLinks.md)
 - [AllOfListRoleResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListRoleResponseLinks.md)
 - [AllOfListRoleResponsePagination](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListRoleResponsePagination.md)
 - [AllOfListSecretAuditResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListSecretAuditResponseLinks.md)
 - [AllOfListSecretAuditResponsePagination](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListSecretAuditResponsePagination.md)
 - [AllOfListSecretResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListSecretResponseLinks.md)
 - [AllOfListSecretResponsePagination](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListSecretResponsePagination.md)
 - [AllOfListSnapshotResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListSnapshotResponseLinks.md)
 - [AllOfListSnapshotResponsePagination](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListSnapshotResponsePagination.md)
 - [AllOfListSnapshotsAuditResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListSnapshotsAuditResponseLinks.md)
 - [AllOfListSnapshotsAuditResponsePagination](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListSnapshotsAuditResponsePagination.md)
 - [AllOfListTagAuditsResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListTagAuditsResponseLinks.md)
 - [AllOfListTagAuditsResponsePagination](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListTagAuditsResponsePagination.md)
 - [AllOfListTagResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListTagResponseLinks.md)
 - [AllOfListTagResponsePagination](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListTagResponsePagination.md)
 - [AllOfListUserAuditResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListUserAuditResponseLinks.md)
 - [AllOfListUserAuditResponsePagination](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListUserAuditResponsePagination.md)
 - [AllOfListUserResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListUserResponseLinks.md)
 - [AllOfListUserResponsePagination](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfListUserResponsePagination.md)
 - [AllOfReinstallInstanceResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfReinstallInstanceResponseLinks.md)
 - [AllOfRollbackSnapshotResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfRollbackSnapshotResponseLinks.md)
 - [AllOfUpdateCustomImageResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfUpdateCustomImageResponseLinks.md)
 - [AllOfUpdateRoleResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfUpdateRoleResponseLinks.md)
 - [AllOfUpdateSecretResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfUpdateSecretResponseLinks.md)
 - [AllOfUpdateSnapshotResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfUpdateSnapshotResponseLinks.md)
 - [AllOfUpdateTagResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfUpdateTagResponseLinks.md)
 - [AllOfUpdateUserResponseLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/AllOfUpdateUserResponseLinks.md)
 - [ApiPermissionsResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ApiPermissionsResponse.md)
 - [AssignmentAuditResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/AssignmentAuditResponse.md)
 - [AssignmentResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/AssignmentResponse.md)
 - [CancelInstanceResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/CancelInstanceResponse.md)
 - [CancelInstanceResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/CancelInstanceResponseData.md)
 - [ClientResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ClientResponse.md)
 - [ClientSecretResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ClientSecretResponse.md)
 - [CreateAssignmentResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateAssignmentResponse.md)
 - [CreateCustomImageRequest](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateCustomImageRequest.md)
 - [CreateCustomImageResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateCustomImageResponse.md)
 - [CreateCustomImageResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateCustomImageResponseData.md)
 - [CreateInstanceRequest](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateInstanceRequest.md)
 - [CreateInstanceResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateInstanceResponse.md)
 - [CreateInstanceResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateInstanceResponseData.md)
 - [CreateRoleRequest](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateRoleRequest.md)
 - [CreateRoleResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateRoleResponse.md)
 - [CreateRoleResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateRoleResponseData.md)
 - [CreateSecretRequest](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateSecretRequest.md)
 - [CreateSecretResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateSecretResponse.md)
 - [CreateSnapshotRequest](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateSnapshotRequest.md)
 - [CreateSnapshotResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateSnapshotResponse.md)
 - [CreateSnapshotResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateSnapshotResponseData.md)
 - [CreateTagRequest](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateTagRequest.md)
 - [CreateTagResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateTagResponse.md)
 - [CreateTagResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateTagResponseData.md)
 - [CreateUserRequest](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateUserRequest.md)
 - [CreateUserResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateUserResponse.md)
 - [CreateUserResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateUserResponseData.md)
 - [CustomImagesStatsResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/CustomImagesStatsResponse.md)
 - [CustomImagesStatsResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/CustomImagesStatsResponseData.md)
 - [FindAssignmentResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/FindAssignmentResponse.md)
 - [FindClientResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/FindClientResponse.md)
 - [FindImageResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/FindImageResponse.md)
 - [FindInstanceResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/FindInstanceResponse.md)
 - [FindRoleResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/FindRoleResponse.md)
 - [FindSecretResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/FindSecretResponse.md)
 - [FindSnapshotResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/FindSnapshotResponse.md)
 - [FindTagResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/FindTagResponse.md)
 - [FindUserIsPasswordSetResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/FindUserIsPasswordSetResponse.md)
 - [FindUserResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/FindUserResponse.md)
 - [GenerateClientSecretResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/GenerateClientSecretResponse.md)
 - [ImageAuditResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ImageAuditResponse.md)
 - [ImageAuditResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/ImageAuditResponseData.md)
 - [ImageResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ImageResponse.md)
 - [InstanceResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/InstanceResponse.md)
 - [InstanceRestartActionResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/InstanceRestartActionResponse.md)
 - [InstanceRestartActionResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/InstanceRestartActionResponseData.md)
 - [InstanceStartActionResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/InstanceStartActionResponse.md)
 - [InstanceStartActionResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/InstanceStartActionResponseData.md)
 - [InstanceStatus](https://github.com/p-fruck/python-contabo/blob/main/docs/InstanceStatus.md)
 - [InstanceStopActionResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/InstanceStopActionResponse.md)
 - [InstanceStopActionResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/InstanceStopActionResponseData.md)
 - [InstancesActionsAuditResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/InstancesActionsAuditResponse.md)
 - [InstancesAuditResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/InstancesAuditResponse.md)
 - [IpConfig](https://github.com/p-fruck/python-contabo/blob/main/docs/IpConfig.md)
 - [IpV4](https://github.com/p-fruck/python-contabo/blob/main/docs/IpV4.md)
 - [IpV6](https://github.com/p-fruck/python-contabo/blob/main/docs/IpV6.md)
 - [Links](https://github.com/p-fruck/python-contabo/blob/main/docs/Links.md)
 - [ListApiPermissionResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ListApiPermissionResponse.md)
 - [ListAssignmentAuditsResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ListAssignmentAuditsResponse.md)
 - [ListAssignmentResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ListAssignmentResponse.md)
 - [ListImageResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ListImageResponse.md)
 - [ListImageResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/ListImageResponseData.md)
 - [ListInstancesActionsAuditResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ListInstancesActionsAuditResponse.md)
 - [ListInstancesAuditResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ListInstancesAuditResponse.md)
 - [ListInstancesResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ListInstancesResponse.md)
 - [ListInstancesResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/ListInstancesResponseData.md)
 - [ListRoleAuditResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ListRoleAuditResponse.md)
 - [ListRoleResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ListRoleResponse.md)
 - [ListSecretAuditResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ListSecretAuditResponse.md)
 - [ListSecretResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ListSecretResponse.md)
 - [ListSnapshotResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ListSnapshotResponse.md)
 - [ListSnapshotsAuditResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ListSnapshotsAuditResponse.md)
 - [ListTagAuditsResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ListTagAuditsResponse.md)
 - [ListTagResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ListTagResponse.md)
 - [ListUserAuditResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ListUserAuditResponse.md)
 - [ListUserResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ListUserResponse.md)
 - [PaginationMeta](https://github.com/p-fruck/python-contabo/blob/main/docs/PaginationMeta.md)
 - [ReinstallInstanceRequest](https://github.com/p-fruck/python-contabo/blob/main/docs/ReinstallInstanceRequest.md)
 - [ReinstallInstanceResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ReinstallInstanceResponse.md)
 - [ReinstallInstanceResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/ReinstallInstanceResponseData.md)
 - [ResourcePermissionsResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ResourcePermissionsResponse.md)
 - [RoleAuditResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/RoleAuditResponse.md)
 - [RoleResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/RoleResponse.md)
 - [RollbackSnapshotResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/RollbackSnapshotResponse.md)
 - [SecretAuditResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/SecretAuditResponse.md)
 - [SecretResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/SecretResponse.md)
 - [SelfLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/SelfLinks.md)
 - [SnapshotResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/SnapshotResponse.md)
 - [SnapshotsAuditResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/SnapshotsAuditResponse.md)
 - [TagAssignmentSelfLinks](https://github.com/p-fruck/python-contabo/blob/main/docs/TagAssignmentSelfLinks.md)
 - [TagAuditResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/TagAuditResponse.md)
 - [TagResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/TagResponse.md)
 - [TagResponse1](https://github.com/p-fruck/python-contabo/blob/main/docs/TagResponse1.md)
 - [UpdateCustomImageRequest](https://github.com/p-fruck/python-contabo/blob/main/docs/UpdateCustomImageRequest.md)
 - [UpdateCustomImageResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/UpdateCustomImageResponse.md)
 - [UpdateCustomImageResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/UpdateCustomImageResponseData.md)
 - [UpdateRoleRequest](https://github.com/p-fruck/python-contabo/blob/main/docs/UpdateRoleRequest.md)
 - [UpdateRoleResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/UpdateRoleResponse.md)
 - [UpdateSecretRequest](https://github.com/p-fruck/python-contabo/blob/main/docs/UpdateSecretRequest.md)
 - [UpdateSecretResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/UpdateSecretResponse.md)
 - [UpdateSnapshotRequest](https://github.com/p-fruck/python-contabo/blob/main/docs/UpdateSnapshotRequest.md)
 - [UpdateSnapshotResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/UpdateSnapshotResponse.md)
 - [UpdateTagRequest](https://github.com/p-fruck/python-contabo/blob/main/docs/UpdateTagRequest.md)
 - [UpdateTagResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/UpdateTagResponse.md)
 - [UpdateUserRequest](https://github.com/p-fruck/python-contabo/blob/main/docs/UpdateUserRequest.md)
 - [UpdateUserResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/UpdateUserResponse.md)
 - [UserAuditResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/UserAuditResponse.md)
 - [UserIsPasswordSetResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/UserIsPasswordSetResponse.md)
 - [UserResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/UserResponse.md)

## Documentation For Authorization


## bearer



## Author

support@contabo.com
    """,
    long_description_content_type='text/markdown',
    project_urls={
        "Bug Tracker": "https://github.com/p-fruck/python-contabo/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        'Intended Audience :: Developers',
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
