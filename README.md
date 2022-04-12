# pfruck_contabo

> ⚠️ I am not affiliated in any way with Contabo

This is an UNOFFICIAL Python API client for [contabo.com](https://contabo.com), which is a hosting provider for VPS and dedicated servers.

The goal of this client is to make management of your server instances more easy using a native Python API for the [Contabo API](https://api.contabo.com/).
This Python package is automatically generated by the [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) project.

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
        description="Ubuntu Server 20.04.2 LTS",
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
        print("Exception when calling ImagesApi->create_custom_image: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.contabo.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ImagesApi* | [**create_custom_image**](docs/ImagesApi.md#create_custom_image) | **POST** /v1/compute/images | Provide a custom image
*ImagesApi* | [**delete_image**](docs/ImagesApi.md#delete_image) | **DELETE** /v1/compute/images/{imageId} | Delete an uploaded custom image by its id
*ImagesApi* | [**retrieve_custom_images_stats**](docs/ImagesApi.md#retrieve_custom_images_stats) | **GET** /v1/compute/images/stats | List statistics regarding the customer&#39;s custom images
*ImagesApi* | [**retrieve_image**](docs/ImagesApi.md#retrieve_image) | **GET** /v1/compute/images/{imageId} | Get details about a specific image by its id
*ImagesApi* | [**retrieve_image_list**](docs/ImagesApi.md#retrieve_image_list) | **GET** /v1/compute/images | List available standard and custom images
*ImagesApi* | [**update_image**](docs/ImagesApi.md#update_image) | **PATCH** /v1/compute/images/{imageId} | Update custom image name by its id
*ImagesAuditsApi* | [**retrieve_image_audits_list**](docs/ImagesAuditsApi.md#retrieve_image_audits_list) | **GET** /v1/compute/images/audits | List history about your custom images (audit)
*InstanceActionsApi* | [**restart**](docs/InstanceActionsApi.md#restart) | **POST** /v1/compute/instances/{instanceId}/actions/restart | Restart a compute instance / resource identified by its id
*InstanceActionsApi* | [**shutdown**](docs/InstanceActionsApi.md#shutdown) | **POST** /v1/compute/instances/{instanceId}/actions/shutdown | Shutdown compute instance / resource by its id
*InstanceActionsApi* | [**start**](docs/InstanceActionsApi.md#start) | **POST** /v1/compute/instances/{instanceId}/actions/start | Start a compute instance / resource identified by its id
*InstanceActionsApi* | [**stop**](docs/InstanceActionsApi.md#stop) | **POST** /v1/compute/instances/{instanceId}/actions/stop | Stop compute instance / resource by its id
*InstanceActionsAuditsApi* | [**retrieve_instances_actions_audits_list**](docs/InstanceActionsAuditsApi.md#retrieve_instances_actions_audits_list) | **GET** /v1/compute/instances/actions/audits | List history about your actions (audit) triggered via the API
*InstancesApi* | [**cancel_instance**](docs/InstancesApi.md#cancel_instance) | **POST** /v1/compute/instances/{instanceId}/cancel | Cancel specific instance by id
*InstancesApi* | [**create_instance**](docs/InstancesApi.md#create_instance) | **POST** /v1/compute/instances | Create a new instance
*InstancesApi* | [**patch_instance**](docs/InstancesApi.md#patch_instance) | **PATCH** /v1/compute/instances/{instanceId} | Update specific instance
*InstancesApi* | [**reinstall_instance**](docs/InstancesApi.md#reinstall_instance) | **PUT** /v1/compute/instances/{instanceId} | Reinstall specific instance
*InstancesApi* | [**retrieve_instance**](docs/InstancesApi.md#retrieve_instance) | **GET** /v1/compute/instances/{instanceId} | Get specific instance by id
*InstancesApi* | [**retrieve_instances_list**](docs/InstancesApi.md#retrieve_instances_list) | **GET** /v1/compute/instances | List instances
*InstancesApi* | [**upgrade_instance**](docs/InstancesApi.md#upgrade_instance) | **POST** /v1/compute/instances/{instanceId}/upgrade | Upgrade instance with the given list of addons
*InstancesAuditsApi* | [**retrieve_instances_audits_list**](docs/InstancesAuditsApi.md#retrieve_instances_audits_list) | **GET** /v1/compute/instances/audits | List history about your instances (audit) triggered via the API
*InternalApi* | [**create_ticket**](docs/InternalApi.md#create_ticket) | **POST** /v1/create-ticket | Create a new support ticket
*InternalApi* | [**retrieve_user_is_password_set**](docs/InternalApi.md#retrieve_user_is_password_set) | **GET** /v1/users/is-password-set | Get user is password set status
*ObjectStoragesApi* | [**cancel_object_storage**](docs/ObjectStoragesApi.md#cancel_object_storage) | **PATCH** /v1/object-storages/{objectStorageId}/cancel | Cancels the specified object storage at the next possible date
*ObjectStoragesApi* | [**create_object_storage**](docs/ObjectStoragesApi.md#create_object_storage) | **POST** /v1/object-storages | Create a new object storage
*ObjectStoragesApi* | [**retrieve_data_center_list**](docs/ObjectStoragesApi.md#retrieve_data_center_list) | **GET** /v1/data-centers | List data centers
*ObjectStoragesApi* | [**retrieve_object_storage**](docs/ObjectStoragesApi.md#retrieve_object_storage) | **GET** /v1/object-storages/{objectStorageId} | Get specific object storage by its id
*ObjectStoragesApi* | [**retrieve_object_storage_list**](docs/ObjectStoragesApi.md#retrieve_object_storage_list) | **GET** /v1/object-storages | List all your Object Storages
*ObjectStoragesApi* | [**retrieve_object_storages_stats**](docs/ObjectStoragesApi.md#retrieve_object_storages_stats) | **GET** /v1/object-storages/{objectStorageId}/stats | List usage statistics about the specified object storage
*ObjectStoragesApi* | [**upgrade_object_storage**](docs/ObjectStoragesApi.md#upgrade_object_storage) | **POST** /v1/object-storages/{objectStorageId}/resize | Upgrade object storage size resp. update autoscaling settings.
*ObjectStoragesAuditsApi* | [**retrieve_object_storage_audits_list**](docs/ObjectStoragesAuditsApi.md#retrieve_object_storage_audits_list) | **GET** /v1/object-storages/audits | List history about your object storages (audit)
*PrivateNetworksApi* | [**assign_instance_private_network**](docs/PrivateNetworksApi.md#assign_instance_private_network) | **POST** /v1/private-networks/{privateNetworkId}/instances/{instanceId} | Add instance to a private network
*PrivateNetworksApi* | [**create_private_network**](docs/PrivateNetworksApi.md#create_private_network) | **POST** /v1/private-networks | Create a new private network
*PrivateNetworksApi* | [**delete_private_network**](docs/PrivateNetworksApi.md#delete_private_network) | **DELETE** /v1/private-networks/{privateNetworkId} | Delete existing private network by id
*PrivateNetworksApi* | [**patch_private_network**](docs/PrivateNetworksApi.md#patch_private_network) | **PATCH** /v1/private-networks/{privateNetworkId} | Update a private network by id
*PrivateNetworksApi* | [**retrieve_private_network**](docs/PrivateNetworksApi.md#retrieve_private_network) | **GET** /v1/private-networks/{privateNetworkId} | Get specific private network by id
*PrivateNetworksApi* | [**retrieve_private_network_list**](docs/PrivateNetworksApi.md#retrieve_private_network_list) | **GET** /v1/private-networks | List private networks
*PrivateNetworksApi* | [**unassign_instance_private_network**](docs/PrivateNetworksApi.md#unassign_instance_private_network) | **DELETE** /v1/private-networks/{privateNetworkId}/instances/{instanceId} | Remove instance from a private network
*PrivateNetworksAuditsApi* | [**retrieve_private_network_audits_list**](docs/PrivateNetworksAuditsApi.md#retrieve_private_network_audits_list) | **GET** /v1/private-networks/audits | List history about your private networks (audit)
*RolesApi* | [**create_role**](docs/RolesApi.md#create_role) | **POST** /v1/roles | Create a new role
*RolesApi* | [**delete_role**](docs/RolesApi.md#delete_role) | **DELETE** /v1/roles/{roleId} | Delete existing role by id
*RolesApi* | [**retrieve_api_permissions_list**](docs/RolesApi.md#retrieve_api_permissions_list) | **GET** /v1/roles/api-permissions | List of API permissions
*RolesApi* | [**retrieve_role**](docs/RolesApi.md#retrieve_role) | **GET** /v1/roles/{roleId} | Get specific role by id
*RolesApi* | [**retrieve_role_list**](docs/RolesApi.md#retrieve_role_list) | **GET** /v1/roles | List roles
*RolesApi* | [**update_role**](docs/RolesApi.md#update_role) | **PUT** /v1/roles/{roleId} | Update specific role by id
*RolesAuditsApi* | [**retrieve_role_audits_list**](docs/RolesAuditsApi.md#retrieve_role_audits_list) | **GET** /v1/roles/audits | List history about your roles (audit)
*SecretsApi* | [**create_secret**](docs/SecretsApi.md#create_secret) | **POST** /v1/secrets | Create a new secret
*SecretsApi* | [**delete_secret**](docs/SecretsApi.md#delete_secret) | **DELETE** /v1/secrets/{secretId} | Delete existing secret by id
*SecretsApi* | [**retrieve_secret**](docs/SecretsApi.md#retrieve_secret) | **GET** /v1/secrets/{secretId} | Get specific secret by id
*SecretsApi* | [**retrieve_secret_list**](docs/SecretsApi.md#retrieve_secret_list) | **GET** /v1/secrets | List secrets
*SecretsApi* | [**update_secret**](docs/SecretsApi.md#update_secret) | **PATCH** /v1/secrets/{secretId} | Update specific secret by id
*SecretsAuditsApi* | [**retrieve_secret_audits_list**](docs/SecretsAuditsApi.md#retrieve_secret_audits_list) | **GET** /v1/secrets/audits | List history about your secrets (audit)
*SnapshotsApi* | [**create_snapshot**](docs/SnapshotsApi.md#create_snapshot) | **POST** /v1/compute/instances/{instanceId}/snapshots | Create a new instance snapshot
*SnapshotsApi* | [**delete_snapshot**](docs/SnapshotsApi.md#delete_snapshot) | **DELETE** /v1/compute/instances/{instanceId}/snapshots/{snapshotId} | Delete existing snapshot by id
*SnapshotsApi* | [**retrieve_snapshot**](docs/SnapshotsApi.md#retrieve_snapshot) | **GET** /v1/compute/instances/{instanceId}/snapshots/{snapshotId} | Retrieve a specific snapshot by id
*SnapshotsApi* | [**retrieve_snapshot_list**](docs/SnapshotsApi.md#retrieve_snapshot_list) | **GET** /v1/compute/instances/{instanceId}/snapshots | List snapshots
*SnapshotsApi* | [**rollback_snapshot**](docs/SnapshotsApi.md#rollback_snapshot) | **POST** /v1/compute/instances/{instanceId}/snapshots/{snapshotId}/rollback | Rollback the instance to a specific snapshot by id
*SnapshotsApi* | [**update_snapshot**](docs/SnapshotsApi.md#update_snapshot) | **PATCH** /v1/compute/instances/{instanceId}/snapshots/{snapshotId} | Update specific snapshot by id
*SnapshotsAuditsApi* | [**retrieve_snapshots_audits_list**](docs/SnapshotsAuditsApi.md#retrieve_snapshots_audits_list) | **GET** /v1/compute/snapshots/audits | List history about your snapshots (audit) triggered via the API
*TagAssignmentsApi* | [**create_assignment**](docs/TagAssignmentsApi.md#create_assignment) | **POST** /v1/tags/{tagId}/assignments/{resourceType}/{resourceId} | Create a new assignment for the tag
*TagAssignmentsApi* | [**delete_assignment**](docs/TagAssignmentsApi.md#delete_assignment) | **DELETE** /v1/tags/{tagId}/assignments/{resourceType}/{resourceId} | Delete existing tag assignment
*TagAssignmentsApi* | [**retrieve_assignment**](docs/TagAssignmentsApi.md#retrieve_assignment) | **GET** /v1/tags/{tagId}/assignments/{resourceType}/{resourceId} | Get specific assignment for the tag
*TagAssignmentsApi* | [**retrieve_assignment_list**](docs/TagAssignmentsApi.md#retrieve_assignment_list) | **GET** /v1/tags/{tagId}/assignments | List tag assignments
*TagAssignmentsAuditsApi* | [**retrieve_assignments_audits_list**](docs/TagAssignmentsAuditsApi.md#retrieve_assignments_audits_list) | **GET** /v1/tags/assignments/audits | List history about your assignments (audit)
*TagsApi* | [**create_tag**](docs/TagsApi.md#create_tag) | **POST** /v1/tags | Create a new tag
*TagsApi* | [**delete_tag**](docs/TagsApi.md#delete_tag) | **DELETE** /v1/tags/{tagId} | Delete existing tag by id
*TagsApi* | [**retrieve_tag**](docs/TagsApi.md#retrieve_tag) | **GET** /v1/tags/{tagId} | Get specific tag by id
*TagsApi* | [**retrieve_tag_list**](docs/TagsApi.md#retrieve_tag_list) | **GET** /v1/tags | List tags
*TagsApi* | [**update_tag**](docs/TagsApi.md#update_tag) | **PATCH** /v1/tags/{tagId} | Update specific tag by id
*TagsAuditsApi* | [**retrieve_tag_audits_list**](docs/TagsAuditsApi.md#retrieve_tag_audits_list) | **GET** /v1/tags/audits | List history about your tags (audit)
*UsersApi* | [**create_user**](docs/UsersApi.md#create_user) | **POST** /v1/users | Create a new user
*UsersApi* | [**delete_user**](docs/UsersApi.md#delete_user) | **DELETE** /v1/users/{userId} | Delete existing user by id
*UsersApi* | [**generate_client_secret**](docs/UsersApi.md#generate_client_secret) | **PUT** /v1/users/client/secret | Generate new client secret
*UsersApi* | [**get_object_storage_credentials**](docs/UsersApi.md#get_object_storage_credentials) | **GET** /v1/users/{userId}/object-storages/credentials | Get S3 compatible object storage credentials
*UsersApi* | [**regenerate_credentials**](docs/UsersApi.md#regenerate_credentials) | **PATCH** /v1/users/{userId}/object-storages/credentials | Regenerates secret key of specified user for the S3 compatible object storages
*UsersApi* | [**resend_email_verification**](docs/UsersApi.md#resend_email_verification) | **POST** /v1/users/{userId}/resend-email-verification | Resend email verification
*UsersApi* | [**reset_password**](docs/UsersApi.md#reset_password) | **POST** /v1/users/{userId}/reset-password | Send reset password email
*UsersApi* | [**retrieve_user**](docs/UsersApi.md#retrieve_user) | **GET** /v1/users/{userId} | Get specific user by id
*UsersApi* | [**retrieve_user_client**](docs/UsersApi.md#retrieve_user_client) | **GET** /v1/users/client | Get client
*UsersApi* | [**retrieve_user_list**](docs/UsersApi.md#retrieve_user_list) | **GET** /v1/users | List users
*UsersApi* | [**update_user**](docs/UsersApi.md#update_user) | **PATCH** /v1/users/{userId} | Update specific user by id
*UsersAuditsApi* | [**retrieve_user_audits_list**](docs/UsersAuditsApi.md#retrieve_user_audits_list) | **GET** /v1/users/audits | List history about your users (audit)


## Documentation For Models

 - [AddOnResponse](docs/AddOnResponse.md)
 - [ApiPermissionsResponse](docs/ApiPermissionsResponse.md)
 - [AssignInstancePrivateNetworkResponse](docs/AssignInstancePrivateNetworkResponse.md)
 - [AssignmentAuditResponse](docs/AssignmentAuditResponse.md)
 - [AssignmentResponse](docs/AssignmentResponse.md)
 - [AutoScalingTypeRequest](docs/AutoScalingTypeRequest.md)
 - [AutoScalingTypeResponse](docs/AutoScalingTypeResponse.md)
 - [CancelInstanceResponse](docs/CancelInstanceResponse.md)
 - [CancelInstanceResponseData](docs/CancelInstanceResponseData.md)
 - [CancelObjectStorageResponse](docs/CancelObjectStorageResponse.md)
 - [CancelObjectStorageResponseData](docs/CancelObjectStorageResponseData.md)
 - [ClientResponse](docs/ClientResponse.md)
 - [ClientSecretResponse](docs/ClientSecretResponse.md)
 - [CreateAssignmentResponse](docs/CreateAssignmentResponse.md)
 - [CreateCustomImageFailResponse](docs/CreateCustomImageFailResponse.md)
 - [CreateCustomImageRequest](docs/CreateCustomImageRequest.md)
 - [CreateCustomImageResponse](docs/CreateCustomImageResponse.md)
 - [CreateCustomImageResponseData](docs/CreateCustomImageResponseData.md)
 - [CreateInstanceRequest](docs/CreateInstanceRequest.md)
 - [CreateInstanceResponse](docs/CreateInstanceResponse.md)
 - [CreateInstanceResponseData](docs/CreateInstanceResponseData.md)
 - [CreateObjectStorageRequest](docs/CreateObjectStorageRequest.md)
 - [CreateObjectStorageResponse](docs/CreateObjectStorageResponse.md)
 - [CreateObjectStorageResponseData](docs/CreateObjectStorageResponseData.md)
 - [CreatePrivateNetworkRequest](docs/CreatePrivateNetworkRequest.md)
 - [CreatePrivateNetworkResponse](docs/CreatePrivateNetworkResponse.md)
 - [CreateRoleRequest](docs/CreateRoleRequest.md)
 - [CreateRoleResponse](docs/CreateRoleResponse.md)
 - [CreateRoleResponseData](docs/CreateRoleResponseData.md)
 - [CreateSecretRequest](docs/CreateSecretRequest.md)
 - [CreateSecretResponse](docs/CreateSecretResponse.md)
 - [CreateSnapshotRequest](docs/CreateSnapshotRequest.md)
 - [CreateSnapshotResponse](docs/CreateSnapshotResponse.md)
 - [CreateSnapshotResponseData](docs/CreateSnapshotResponseData.md)
 - [CreateTagRequest](docs/CreateTagRequest.md)
 - [CreateTagResponse](docs/CreateTagResponse.md)
 - [CreateTagResponseData](docs/CreateTagResponseData.md)
 - [CreateTicketRequest](docs/CreateTicketRequest.md)
 - [CreateTicketResponse](docs/CreateTicketResponse.md)
 - [CreateTicketResponseData](docs/CreateTicketResponseData.md)
 - [CreateUserRequest](docs/CreateUserRequest.md)
 - [CreateUserResponse](docs/CreateUserResponse.md)
 - [CreateUserResponseData](docs/CreateUserResponseData.md)
 - [CredentialData](docs/CredentialData.md)
 - [CredentialResponse](docs/CredentialResponse.md)
 - [CustomImagesStatsResponse](docs/CustomImagesStatsResponse.md)
 - [CustomImagesStatsResponseData](docs/CustomImagesStatsResponseData.md)
 - [DataCenterResponse](docs/DataCenterResponse.md)
 - [FindAssignmentResponse](docs/FindAssignmentResponse.md)
 - [FindClientResponse](docs/FindClientResponse.md)
 - [FindImageResponse](docs/FindImageResponse.md)
 - [FindInstanceResponse](docs/FindInstanceResponse.md)
 - [FindObjectStorageResponse](docs/FindObjectStorageResponse.md)
 - [FindPrivateNetworkResponse](docs/FindPrivateNetworkResponse.md)
 - [FindRoleResponse](docs/FindRoleResponse.md)
 - [FindSecretResponse](docs/FindSecretResponse.md)
 - [FindSnapshotResponse](docs/FindSnapshotResponse.md)
 - [FindTagResponse](docs/FindTagResponse.md)
 - [FindUserIsPasswordSetResponse](docs/FindUserIsPasswordSetResponse.md)
 - [FindUserResponse](docs/FindUserResponse.md)
 - [GenerateClientSecretResponse](docs/GenerateClientSecretResponse.md)
 - [ImageAuditResponse](docs/ImageAuditResponse.md)
 - [ImageAuditResponseData](docs/ImageAuditResponseData.md)
 - [ImageResponse](docs/ImageResponse.md)
 - [InstanceAssignmentSelfLinks](docs/InstanceAssignmentSelfLinks.md)
 - [InstanceResponse](docs/InstanceResponse.md)
 - [InstanceRestartActionResponse](docs/InstanceRestartActionResponse.md)
 - [InstanceRestartActionResponseData](docs/InstanceRestartActionResponseData.md)
 - [InstanceShutdownActionResponse](docs/InstanceShutdownActionResponse.md)
 - [InstanceShutdownActionResponseData](docs/InstanceShutdownActionResponseData.md)
 - [InstanceStartActionResponse](docs/InstanceStartActionResponse.md)
 - [InstanceStartActionResponseData](docs/InstanceStartActionResponseData.md)
 - [InstanceStatus](docs/InstanceStatus.md)
 - [InstanceStopActionResponse](docs/InstanceStopActionResponse.md)
 - [InstanceStopActionResponseData](docs/InstanceStopActionResponseData.md)
 - [Instances](docs/Instances.md)
 - [InstancesActionsAuditResponse](docs/InstancesActionsAuditResponse.md)
 - [InstancesAuditResponse](docs/InstancesAuditResponse.md)
 - [IpConfig](docs/IpConfig.md)
 - [IpV4](docs/IpV4.md)
 - [IpV6](docs/IpV6.md)
 - [Links](docs/Links.md)
 - [ListApiPermissionResponse](docs/ListApiPermissionResponse.md)
 - [ListAssignmentAuditsResponse](docs/ListAssignmentAuditsResponse.md)
 - [ListAssignmentResponse](docs/ListAssignmentResponse.md)
 - [ListDataCenterResponse](docs/ListDataCenterResponse.md)
 - [ListImageResponse](docs/ListImageResponse.md)
 - [ListImageResponseData](docs/ListImageResponseData.md)
 - [ListInstancesActionsAuditResponse](docs/ListInstancesActionsAuditResponse.md)
 - [ListInstancesAuditResponse](docs/ListInstancesAuditResponse.md)
 - [ListInstancesResponse](docs/ListInstancesResponse.md)
 - [ListInstancesResponseData](docs/ListInstancesResponseData.md)
 - [ListObjectStorageAuditResponse](docs/ListObjectStorageAuditResponse.md)
 - [ListObjectStorageResponse](docs/ListObjectStorageResponse.md)
 - [ListPrivateNetworkAuditResponse](docs/ListPrivateNetworkAuditResponse.md)
 - [ListPrivateNetworkResponse](docs/ListPrivateNetworkResponse.md)
 - [ListPrivateNetworkResponseData](docs/ListPrivateNetworkResponseData.md)
 - [ListRoleAuditResponse](docs/ListRoleAuditResponse.md)
 - [ListRoleResponse](docs/ListRoleResponse.md)
 - [ListSecretAuditResponse](docs/ListSecretAuditResponse.md)
 - [ListSecretResponse](docs/ListSecretResponse.md)
 - [ListSnapshotResponse](docs/ListSnapshotResponse.md)
 - [ListSnapshotsAuditResponse](docs/ListSnapshotsAuditResponse.md)
 - [ListTagAuditsResponse](docs/ListTagAuditsResponse.md)
 - [ListTagResponse](docs/ListTagResponse.md)
 - [ListUserAuditResponse](docs/ListUserAuditResponse.md)
 - [ListUserResponse](docs/ListUserResponse.md)
 - [ObjectStorageAuditResponse](docs/ObjectStorageAuditResponse.md)
 - [ObjectStorageResponse](docs/ObjectStorageResponse.md)
 - [ObjectStoragesStatsResponse](docs/ObjectStoragesStatsResponse.md)
 - [ObjectStoragesStatsResponseData](docs/ObjectStoragesStatsResponseData.md)
 - [PaginationMeta](docs/PaginationMeta.md)
 - [PatchInstanceRequest](docs/PatchInstanceRequest.md)
 - [PatchInstanceResponse](docs/PatchInstanceResponse.md)
 - [PatchInstanceResponseData](docs/PatchInstanceResponseData.md)
 - [PatchPrivateNetworkRequest](docs/PatchPrivateNetworkRequest.md)
 - [PatchPrivateNetworkResponse](docs/PatchPrivateNetworkResponse.md)
 - [PermissionRequest](docs/PermissionRequest.md)
 - [PermissionResponse](docs/PermissionResponse.md)
 - [PrivateIpConfig](docs/PrivateIpConfig.md)
 - [PrivateNetworkAuditResponse](docs/PrivateNetworkAuditResponse.md)
 - [PrivateNetworkResponse](docs/PrivateNetworkResponse.md)
 - [ReinstallInstanceRequest](docs/ReinstallInstanceRequest.md)
 - [ReinstallInstanceResponse](docs/ReinstallInstanceResponse.md)
 - [ReinstallInstanceResponseData](docs/ReinstallInstanceResponseData.md)
 - [ResourcePermissionsResponse](docs/ResourcePermissionsResponse.md)
 - [RoleAuditResponse](docs/RoleAuditResponse.md)
 - [RoleResponse](docs/RoleResponse.md)
 - [RollbackSnapshotResponse](docs/RollbackSnapshotResponse.md)
 - [SecretAuditResponse](docs/SecretAuditResponse.md)
 - [SecretResponse](docs/SecretResponse.md)
 - [SelfLinks](docs/SelfLinks.md)
 - [SnapshotResponse](docs/SnapshotResponse.md)
 - [SnapshotsAuditResponse](docs/SnapshotsAuditResponse.md)
 - [TagAssignmentSelfLinks](docs/TagAssignmentSelfLinks.md)
 - [TagAuditResponse](docs/TagAuditResponse.md)
 - [TagResponse](docs/TagResponse.md)
 - [TagResponse1](docs/TagResponse1.md)
 - [UnassignInstancePrivateNetworkResponse](docs/UnassignInstancePrivateNetworkResponse.md)
 - [UpdateCustomImageRequest](docs/UpdateCustomImageRequest.md)
 - [UpdateCustomImageResponse](docs/UpdateCustomImageResponse.md)
 - [UpdateCustomImageResponseData](docs/UpdateCustomImageResponseData.md)
 - [UpdateObjectStorageResponse](docs/UpdateObjectStorageResponse.md)
 - [UpdateObjectStorageResponseData](docs/UpdateObjectStorageResponseData.md)
 - [UpdateRoleRequest](docs/UpdateRoleRequest.md)
 - [UpdateRoleResponse](docs/UpdateRoleResponse.md)
 - [UpdateSecretRequest](docs/UpdateSecretRequest.md)
 - [UpdateSecretResponse](docs/UpdateSecretResponse.md)
 - [UpdateSnapshotRequest](docs/UpdateSnapshotRequest.md)
 - [UpdateSnapshotResponse](docs/UpdateSnapshotResponse.md)
 - [UpdateTagRequest](docs/UpdateTagRequest.md)
 - [UpdateTagResponse](docs/UpdateTagResponse.md)
 - [UpdateUserRequest](docs/UpdateUserRequest.md)
 - [UpdateUserResponse](docs/UpdateUserResponse.md)
 - [UpgradeAutoScalingType](docs/UpgradeAutoScalingType.md)
 - [UpgradeInstanceData](docs/UpgradeInstanceData.md)
 - [UpgradeInstanceRequest](docs/UpgradeInstanceRequest.md)
 - [UpgradeInstanceResponse](docs/UpgradeInstanceResponse.md)
 - [UpgradeObjectStorageRequest](docs/UpgradeObjectStorageRequest.md)
 - [UserAuditResponse](docs/UserAuditResponse.md)
 - [UserIsPasswordSetResponse](docs/UserIsPasswordSetResponse.md)
 - [UserResponse](docs/UserResponse.md)


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

