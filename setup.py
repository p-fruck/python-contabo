"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "pfruck_contabo"
VERSION = "1.7.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="This is an UNOFFICIAL Python API client for Contabo",
    author="OpenAPI Generator community",
    author_email="support@contabo.com",
    url="https://github.com/p-fruck/python-contabo",
    keywords=["OpenAPI", "OpenAPI-Generator", "Contabo API"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
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

import time
import pfruck_contabo
from pprint import pprint
from pfruck_contabo.api import images_api
from pfruck_contabo.model.create_custom_image_fail_response import CreateCustomImageFailResponse
from pfruck_contabo.model.create_custom_image_request import CreateCustomImageRequest
from pfruck_contabo.model.create_custom_image_response import CreateCustomImageResponse
from pfruck_contabo.model.custom_images_stats_response import CustomImagesStatsResponse
from pfruck_contabo.model.find_image_response import FindImageResponse
from pfruck_contabo.model.list_image_response import ListImageResponse
from pfruck_contabo.model.update_custom_image_request import UpdateCustomImageRequest
from pfruck_contabo.model.update_custom_image_response import UpdateCustomImageResponse
# Defining the host is optional and defaults to https://api.contabo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pfruck_contabo.Configuration(
    host = "https://api.contabo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = pfruck_contabo.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)


# Enter a context with an instance of the API client
with pfruck_contabo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = images_api.ImagesApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
create_custom_image_request = CreateCustomImageRequest(
        name="Ubuntu Custom Image",
        description="This is an UNOFFICIAL Python API client for Contabo",
        url="https://example.com/image.qcow2",
        os_type="Linux",
        version="20.04.2",
    ) # CreateCustomImageRequest | 
x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    try:
        # Provide a custom image
        api_response = api_instance.create_custom_image(x_request_id, create_custom_image_request, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling ImagesApi->create_custom_image: %s\\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.contabo.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ImagesApi* | [**create_custom_image**](https://github.com/p-fruck/python-contabo/blob/main/docs/ImagesApi.md#create_custom_image) | **POST** /v1/compute/images | Provide a custom image
*ImagesApi* | [**delete_image**](https://github.com/p-fruck/python-contabo/blob/main/docs/ImagesApi.md#delete_image) | **DELETE** /v1/compute/images/{imageId} | Delete an uploaded custom image by its id
*ImagesApi* | [**retrieve_custom_images_stats**](https://github.com/p-fruck/python-contabo/blob/main/docs/ImagesApi.md#retrieve_custom_images_stats) | **GET** /v1/compute/images/stats | List statistics regarding the customer&#39;s custom images
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
*InstancesApi* | [**reinstall_instance**](https://github.com/p-fruck/python-contabo/blob/main/docs/InstancesApi.md#reinstall_instance) | **PUT** /v1/compute/instances/{instanceId} | Reinstall specific instance
*InstancesApi* | [**retrieve_instance**](https://github.com/p-fruck/python-contabo/blob/main/docs/InstancesApi.md#retrieve_instance) | **GET** /v1/compute/instances/{instanceId} | Get specific instance by id
*InstancesApi* | [**retrieve_instances_list**](https://github.com/p-fruck/python-contabo/blob/main/docs/InstancesApi.md#retrieve_instances_list) | **GET** /v1/compute/instances | List instances
*InstancesAuditsApi* | [**retrieve_instances_audits_list**](https://github.com/p-fruck/python-contabo/blob/main/docs/InstancesAuditsApi.md#retrieve_instances_audits_list) | **GET** /v1/compute/instances/audits | List history about your instances (audit) triggered via the API
*InternalApi* | [**create_ticket**](https://github.com/p-fruck/python-contabo/blob/main/docs/InternalApi.md#create_ticket) | **POST** /v1/create-ticket | Create a new support ticket
*InternalApi* | [**retrieve_user_is_password_set**](https://github.com/p-fruck/python-contabo/blob/main/docs/InternalApi.md#retrieve_user_is_password_set) | **GET** /v1/users/is-password-set | Get user is password set status
*ObjectStoragesApi* | [**cancel_object_storage**](https://github.com/p-fruck/python-contabo/blob/main/docs/ObjectStoragesApi.md#cancel_object_storage) | **PATCH** /v1/object-storages/{objectStorageId}/cancel | Cancels the specified object storage at the next possible date
*ObjectStoragesApi* | [**create_object_storage**](https://github.com/p-fruck/python-contabo/blob/main/docs/ObjectStoragesApi.md#create_object_storage) | **POST** /v1/object-storages | Create a new object storage
*ObjectStoragesApi* | [**retrieve_data_center_list**](https://github.com/p-fruck/python-contabo/blob/main/docs/ObjectStoragesApi.md#retrieve_data_center_list) | **GET** /v1/data-centers | List data centers
*ObjectStoragesApi* | [**retrieve_object_storage**](https://github.com/p-fruck/python-contabo/blob/main/docs/ObjectStoragesApi.md#retrieve_object_storage) | **GET** /v1/object-storages/{objectStorageId} | Get specific object storage by its id
*ObjectStoragesApi* | [**retrieve_object_storage_list**](https://github.com/p-fruck/python-contabo/blob/main/docs/ObjectStoragesApi.md#retrieve_object_storage_list) | **GET** /v1/object-storages | List all your Object Storages
*ObjectStoragesApi* | [**retrieve_object_storages_stats**](https://github.com/p-fruck/python-contabo/blob/main/docs/ObjectStoragesApi.md#retrieve_object_storages_stats) | **GET** /v1/object-storages/{objectStorageId}/stats | List usage statistics about the specified object storage
*ObjectStoragesApi* | [**upgrade_object_storage**](https://github.com/p-fruck/python-contabo/blob/main/docs/ObjectStoragesApi.md#upgrade_object_storage) | **POST** /v1/object-storages/{objectStorageId}/resize | Upgrade object storage size resp. update autoscaling settings.
*ObjectStoragesAuditsApi* | [**retrieve_object_storage_audits_list**](https://github.com/p-fruck/python-contabo/blob/main/docs/ObjectStoragesAuditsApi.md#retrieve_object_storage_audits_list) | **GET** /v1/object-storages/audits | List history about your object storages (audit)
*RolesApi* | [**create_role**](https://github.com/p-fruck/python-contabo/blob/main/docs/RolesApi.md#create_role) | **POST** /v1/roles | Create a new role
*RolesApi* | [**delete_role**](https://github.com/p-fruck/python-contabo/blob/main/docs/RolesApi.md#delete_role) | **DELETE** /v1/roles/{roleId} | Delete existing role by id
*RolesApi* | [**retrieve_api_permissions_list**](https://github.com/p-fruck/python-contabo/blob/main/docs/RolesApi.md#retrieve_api_permissions_list) | **GET** /v1/roles/api-permissions | List of API permissions
*RolesApi* | [**retrieve_role**](https://github.com/p-fruck/python-contabo/blob/main/docs/RolesApi.md#retrieve_role) | **GET** /v1/roles/{roleId} | Get specific role by id
*RolesApi* | [**retrieve_role_list**](https://github.com/p-fruck/python-contabo/blob/main/docs/RolesApi.md#retrieve_role_list) | **GET** /v1/roles | List roles
*RolesApi* | [**update_role**](https://github.com/p-fruck/python-contabo/blob/main/docs/RolesApi.md#update_role) | **PUT** /v1/roles/{roleId} | Update specific role by id
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
*UsersApi* | [**get_object_storage_credentials**](https://github.com/p-fruck/python-contabo/blob/main/docs/UsersApi.md#get_object_storage_credentials) | **GET** /v1/users/{userId}/object-storages/credentials | Get S3 compatible object storage credentials
*UsersApi* | [**regenerate_credentials**](https://github.com/p-fruck/python-contabo/blob/main/docs/UsersApi.md#regenerate_credentials) | **PATCH** /v1/users/{userId}/object-storages/credentials | Regenerates secret key of specified user for the S3 compatible object storages
*UsersApi* | [**resend_email_verification**](https://github.com/p-fruck/python-contabo/blob/main/docs/UsersApi.md#resend_email_verification) | **POST** /v1/users/{userId}/resend-email-verification | Resend email verification
*UsersApi* | [**reset_password**](https://github.com/p-fruck/python-contabo/blob/main/docs/UsersApi.md#reset_password) | **POST** /v1/users/{userId}/reset-password | Send reset password email
*UsersApi* | [**retrieve_user**](https://github.com/p-fruck/python-contabo/blob/main/docs/UsersApi.md#retrieve_user) | **GET** /v1/users/{userId} | Get specific user by id
*UsersApi* | [**retrieve_user_client**](https://github.com/p-fruck/python-contabo/blob/main/docs/UsersApi.md#retrieve_user_client) | **GET** /v1/users/client | Get client
*UsersApi* | [**retrieve_user_list**](https://github.com/p-fruck/python-contabo/blob/main/docs/UsersApi.md#retrieve_user_list) | **GET** /v1/users | List users
*UsersApi* | [**update_user**](https://github.com/p-fruck/python-contabo/blob/main/docs/UsersApi.md#update_user) | **PATCH** /v1/users/{userId} | Update specific user by id
*UsersAuditsApi* | [**retrieve_user_audits_list**](https://github.com/p-fruck/python-contabo/blob/main/docs/UsersAuditsApi.md#retrieve_user_audits_list) | **GET** /v1/users/audits | List history about your users (audit)


## Documentation For Models

 - [AddOnResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/AddOnResponse.md)
 - [ApiPermissionsResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ApiPermissionsResponse.md)
 - [AssignmentAuditResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/AssignmentAuditResponse.md)
 - [AssignmentResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/AssignmentResponse.md)
 - [AutoScalingTypeRequest](https://github.com/p-fruck/python-contabo/blob/main/docs/AutoScalingTypeRequest.md)
 - [AutoScalingTypeResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/AutoScalingTypeResponse.md)
 - [CancelInstanceResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/CancelInstanceResponse.md)
 - [CancelInstanceResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/CancelInstanceResponseData.md)
 - [CancelObjectStorageResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/CancelObjectStorageResponse.md)
 - [CancelObjectStorageResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/CancelObjectStorageResponseData.md)
 - [ClientResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ClientResponse.md)
 - [ClientSecretResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ClientSecretResponse.md)
 - [CreateAssignmentResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateAssignmentResponse.md)
 - [CreateCustomImageFailResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateCustomImageFailResponse.md)
 - [CreateCustomImageRequest](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateCustomImageRequest.md)
 - [CreateCustomImageResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateCustomImageResponse.md)
 - [CreateCustomImageResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateCustomImageResponseData.md)
 - [CreateInstanceRequest](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateInstanceRequest.md)
 - [CreateInstanceResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateInstanceResponse.md)
 - [CreateInstanceResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateInstanceResponseData.md)
 - [CreateObjectStorageRequest](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateObjectStorageRequest.md)
 - [CreateObjectStorageResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateObjectStorageResponse.md)
 - [CreateObjectStorageResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateObjectStorageResponseData.md)
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
 - [CreateTicketRequest](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateTicketRequest.md)
 - [CreateTicketResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateTicketResponse.md)
 - [CreateTicketResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateTicketResponseData.md)
 - [CreateUserRequest](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateUserRequest.md)
 - [CreateUserResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateUserResponse.md)
 - [CreateUserResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/CreateUserResponseData.md)
 - [CredentialData](https://github.com/p-fruck/python-contabo/blob/main/docs/CredentialData.md)
 - [CredentialResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/CredentialResponse.md)
 - [CustomImagesStatsResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/CustomImagesStatsResponse.md)
 - [CustomImagesStatsResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/CustomImagesStatsResponseData.md)
 - [DataCenterResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/DataCenterResponse.md)
 - [FindAssignmentResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/FindAssignmentResponse.md)
 - [FindClientResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/FindClientResponse.md)
 - [FindImageResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/FindImageResponse.md)
 - [FindInstanceResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/FindInstanceResponse.md)
 - [FindObjectStorageResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/FindObjectStorageResponse.md)
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
 - [ListDataCenterResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ListDataCenterResponse.md)
 - [ListImageResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ListImageResponse.md)
 - [ListImageResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/ListImageResponseData.md)
 - [ListInstancesActionsAuditResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ListInstancesActionsAuditResponse.md)
 - [ListInstancesAuditResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ListInstancesAuditResponse.md)
 - [ListInstancesResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ListInstancesResponse.md)
 - [ListInstancesResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/ListInstancesResponseData.md)
 - [ListObjectStorageAuditResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ListObjectStorageAuditResponse.md)
 - [ListObjectStorageResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ListObjectStorageResponse.md)
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
 - [ObjectStorageAuditResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ObjectStorageAuditResponse.md)
 - [ObjectStorageResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ObjectStorageResponse.md)
 - [ObjectStoragesStatsResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/ObjectStoragesStatsResponse.md)
 - [ObjectStoragesStatsResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/ObjectStoragesStatsResponseData.md)
 - [PaginationMeta](https://github.com/p-fruck/python-contabo/blob/main/docs/PaginationMeta.md)
 - [PermissionRequest](https://github.com/p-fruck/python-contabo/blob/main/docs/PermissionRequest.md)
 - [PermissionResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/PermissionResponse.md)
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
 - [UpdateObjectStorageResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/UpdateObjectStorageResponse.md)
 - [UpdateObjectStorageResponseData](https://github.com/p-fruck/python-contabo/blob/main/docs/UpdateObjectStorageResponseData.md)
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
 - [UpgradeAutoScalingType](https://github.com/p-fruck/python-contabo/blob/main/docs/UpgradeAutoScalingType.md)
 - [UpgradeObjectStorageRequest](https://github.com/p-fruck/python-contabo/blob/main/docs/UpgradeObjectStorageRequest.md)
 - [UserAuditResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/UserAuditResponse.md)
 - [UserIsPasswordSetResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/UserIsPasswordSetResponse.md)
 - [UserResponse](https://github.com/p-fruck/python-contabo/blob/main/docs/UserResponse.md)


## Documentation For Authorization


## bearer

- **Type**: Bearer authentication (JWT)


## Author

support@contabo.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in pfruck_contabo.apis and pfruck_contabo.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from pfruck_contabo.api.default_api import DefaultApi`
- `from pfruck_contabo.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import pfruck_contabo
from pfruck_contabo.apis import *
from pfruck_contabo.models import *
```

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
