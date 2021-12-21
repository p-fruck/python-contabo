# coding: utf-8

# flake8: noqa
"""
    Contabo API

    # Introduction  Contabo API allows you to manage your resources using HTTP requests. This documentation includes a set of HTTP endpoints that are designed to RESTful principles. Each endpoint includes descriptions, request syntax, and examples.  Contabo provides also a CLI tool which enables you to manage your resources easily from the command line. [CLI Download and  Installation instructions.](https://github.com/contabo/cntb)  ## Getting Started  In order to use the Contabo API you will need the following credentials which are available from the [Customer Control Panel](https://my.contabo.com/api/details): 1. ClientId 2. ClientSecret 3. API User (your email address to login to the [Customer Control Panel](https://my.contabo.com/api/details)) 4. API Password (this is a new password which you'll set or change in the [Customer Control Panel](https://my.contabo.com/api/details))  You can either use the API directly or by using the `cntb` CLI (Command Line Interface) tool.  ### Using the API directly  #### Via `curl` for Linux/Unix like systems  This requires `curl` and `jq` in your shell (e.g. `bash`, `zsh`). Please replace the first four placeholders with actual values.  ```sh CLIENT_ID=<ClientId from Customer Control Panel> CLIENT_SECRET=<ClientSecret from Customer Control Panel> API_USER=<API User from Customer Control Panel> API_PASSWORD=<API Password from Customer Control Panel> ACCESS_TOKEN=$(curl -d \"client_id=$CLIENT_ID\" -d \"client_secret=$CLIENT_SECRET\" --data-urlencode \"username=$API_USER\" --data-urlencode \"password=$API_PASSWORD\" -d 'grant_type=password' 'https://auth.contabo.com/auth/realms/contabo/protocol/openid-connect/token' | jq -r '.access_token') # get list of your instances curl -X GET -H \"Authorization: Bearer $ACCESS_TOKEN\" -H \"x-request-id: 51A87ECD-754E-4104-9C54-D01AD0F83406\" \"https://api.contabo.com/v1/compute/instances\" | jq ```  #### Via `PowerShell` for Windows  Please open `PowerShell` and execute the following code after replacing the first four placeholders with actual values.  ```powershell $client_id='<ClientId from Customer Control Panel>' $client_secret='<ClientSecret from Customer Control Panel>' $api_user='<API User from Customer Control Panel>' $api_password='<API Password from Customer Control Panel>' $body = @{grant_type='password' client_id=$client_id client_secret=$client_secret username=$api_user password=$api_password} $response = Invoke-WebRequest -Uri 'https://auth.contabo.com/auth/realms/contabo/protocol/openid-connect/token' -Method 'POST' -Body $body $access_token = (ConvertFrom-Json $([String]::new($response.Content))).access_token # get list of your instances $headers = @{} $headers.Add(\"Authorization\",\"Bearer $access_token\") $headers.Add(\"x-request-id\",\"51A87ECD-754E-4104-9C54-D01AD0F83406\") Invoke-WebRequest -Uri 'https://api.contabo.com/v1/compute/instances' -Method 'GET' -Headers $headers ```  ### Using the Contabo API via the `cntb` CLI tool  1. Download `cntb` for your operating system (MacOS, Windows and Linux supported) [here](https://github.com/contabo/cntb) 2. Unzip the downloaded file 3. You might move the executable to any location on your disk. You may update your `PATH` environment variable for easier invocation. 4. Configure it once to use your credentials           ```sh    cntb config set-credentials --oauth2-clientid=<ClientId from Customer Control Panel> --oauth2-client-secret=<ClientSecret from Customer Control Panel> --oauth2-user=<API User from Customer Control Panel> --oauth2-password=<API Password from Customer Control Panel>    ```  5. Use the CLI           ```sh    # get list of your instances    cntb get instances    # help    cntb help    ```  ## API Overiew  ### [Compute Mangement](#tag/Instances)  The Compute Management API allows you to manage compute resources (e.g. creation, deletion, starting, stopping) as well as managing snapshots and custom images. It also offers you to take advantage of [cloud-init](https://cloud-init.io/) at least on our default / standard images (for custom images you'll need to provide cloud-init support packages). The API offers provisioning of cloud-init scripts via the `user_data` field.  Custom images must be provided in `.qcow2` or `.iso` format. This gives you even more flexibilty for setting up your environment.  ### [Secrets Mangement](#tag/Secrets)  You can optionally save your passwords or public ssh keys using the Secrets Managemnt API. You are not required to use it there will be no functional disadvantages.  By using that API you can easily reuse you public ssh keys when setting up different servers without the need to look them up every time. It can also be used to allow Contabo Supporters to access your machine without sending the passwords via potentially unsecure emails.  ### [User Management](#tag/Users)  If you need to allow other persons or automation scripts to access specific API endpoints resp. resources the User Mangement API comes into play. With that API you are able to manage users having possibly restricted access. You are free to define those restrictions to fit your needs. So beside an arbitrary number of users you basically define any number of so called `roles`. Roles allows access and must be one of the following types:  * `apiPermission`          This allows you to specify a restriction to certain functions of an API by allowing control over POST (=Create), GET (=Read), PUT/PATCH (=Update) and DELETE (=Delete) methods for each API endpoint (URL) individually. * `resourcePermission`          In order to restrict access to specific resources create a role with `resourcePermission` type by specifying any number of [tags](#tag-management). These tags need to be assigned to resources for them to take effect. E.g. a tag could be assiged to several compute resources. So that a user with that role (and of course access to the API endpoints via `apiPermission` role type) could only access those compute resources.  The `roles` are then assigned to a `user`. You can assign one or several roles regardless of the role's type. Of course you could also assign a user `admin` privileges without specifying any roles.  ### [Tag Management](#tag/Tags)  The Tag Management API allows you to manage your tags in order to organize your resources in a more convenient way. Simply assign a tag to resources like a compute resource to manage them.The assignments of tags to resources will also enable you to control access to these specific resources to users via the [User Management API](#user-management). For convenience reasons you might choose a color for tag. The Customer Control Panel will use that color to display the tags.  ## Requests  The Contabo API supports HTTP requests like mentioned below. Not every endpoint supports all methods. The allowed methods are listed within this documentation.  Method | Description ---    | --- GET    | To retrieve information about a resource, use the GET method.<br>The data is returned as a JSON object. GET methods are read-only and do not affect any resources. POST   | Issue a POST method to create a new object. Include all needed attributes in the request body encoded as JSON. PATCH  | Some resources support partial modification with PATCH,<br>which modifies specific attributes without updating the entire object representation. PUT    | Use the PUT method to update information about a resource.<br>PUT will set new values on the item without regard to their current values. DELETE | Use the DELETE method to destroy a resource in your account.<br>If it is not found, the operation will return a 4xx error and an appropriate message.  ## Responses  Usually the Contabo API should respond to your requests. The data returned is in [JSON](https://www.json.org/) format allowing easy processing in any programming language or tools.  As common for HTTP requests you will get back a so called HTTP status code. This gives you overall information about success or error. The following table lists common HTTP status codes.  Please note that the description of the endpoints and methods are not listing all possibly status codes in detail as they are generic. Only special return codes with their resp. response data are explicitly listed.  Response Code | Description --- | --- 200 | The response contains your requested information. 201 | Your request was accepted. The resource was created. 204 | Your request succeeded, there is no additional information returned. 400 | Your request was malformed. 401 | You did not supply valid authentication credentials. 402 | Request refused as it requires additional payed service. 403 | You are not allowed to perform the request. 404 | No results were found for your request or resource does not exist. 409 | Conflict with resources. For example violation of unique data contraints detected when trying to create or change resources. 429 | Rate-limit reached. Please wait for some time before doing more requests. 500 | We were unable to perform the request due to server-side problems. In such cases please retry or contact the support.  Not every endpoint returns data. For example DELETE requests usually don't return any data. All others do return data. For easy handling the return values consists of metadata denoted with and underscore (\"_\") like `_links` or `_pagination`. The actual data is returned in a field called `data`. For convenience reasons this `data` field is always returned as an array even if it consists of only one single element.  Some general details about Contabo API from [Contabo](https://contabo.com).   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@contabo.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from pfruck_contabo.models.add_on_response import AddOnResponse
from pfruck_contabo.models.all_of_cancel_instance_response_links import AllOfCancelInstanceResponseLinks
from pfruck_contabo.models.all_of_create_assignment_response_links import AllOfCreateAssignmentResponseLinks
from pfruck_contabo.models.all_of_create_custom_image_response_links import AllOfCreateCustomImageResponseLinks
from pfruck_contabo.models.all_of_create_instance_response_links import AllOfCreateInstanceResponseLinks
from pfruck_contabo.models.all_of_create_role_response_links import AllOfCreateRoleResponseLinks
from pfruck_contabo.models.all_of_create_secret_response_links import AllOfCreateSecretResponseLinks
from pfruck_contabo.models.all_of_create_snapshot_response_links import AllOfCreateSnapshotResponseLinks
from pfruck_contabo.models.all_of_create_tag_response_links import AllOfCreateTagResponseLinks
from pfruck_contabo.models.all_of_create_user_response_links import AllOfCreateUserResponseLinks
from pfruck_contabo.models.all_of_custom_images_stats_response_links import AllOfCustomImagesStatsResponseLinks
from pfruck_contabo.models.all_of_find_assignment_response_links import AllOfFindAssignmentResponseLinks
from pfruck_contabo.models.all_of_find_client_response_links import AllOfFindClientResponseLinks
from pfruck_contabo.models.all_of_find_image_response_links import AllOfFindImageResponseLinks
from pfruck_contabo.models.all_of_find_instance_response_links import AllOfFindInstanceResponseLinks
from pfruck_contabo.models.all_of_find_role_response_links import AllOfFindRoleResponseLinks
from pfruck_contabo.models.all_of_find_secret_response_links import AllOfFindSecretResponseLinks
from pfruck_contabo.models.all_of_find_snapshot_response_links import AllOfFindSnapshotResponseLinks
from pfruck_contabo.models.all_of_find_tag_response_links import AllOfFindTagResponseLinks
from pfruck_contabo.models.all_of_find_user_response_links import AllOfFindUserResponseLinks
from pfruck_contabo.models.all_of_generate_client_secret_response_links import AllOfGenerateClientSecretResponseLinks
from pfruck_contabo.models.all_of_image_audit_response_links import AllOfImageAuditResponseLinks
from pfruck_contabo.models.all_of_image_audit_response_pagination import AllOfImageAuditResponsePagination
from pfruck_contabo.models.all_of_instance_restart_action_response_links import AllOfInstanceRestartActionResponseLinks
from pfruck_contabo.models.all_of_instance_start_action_response_links import AllOfInstanceStartActionResponseLinks
from pfruck_contabo.models.all_of_instance_stop_action_response_links import AllOfInstanceStopActionResponseLinks
from pfruck_contabo.models.all_of_list_api_permission_response_links import AllOfListApiPermissionResponseLinks
from pfruck_contabo.models.all_of_list_assignment_audits_response_links import AllOfListAssignmentAuditsResponseLinks
from pfruck_contabo.models.all_of_list_assignment_audits_response_pagination import AllOfListAssignmentAuditsResponsePagination
from pfruck_contabo.models.all_of_list_assignment_response_links import AllOfListAssignmentResponseLinks
from pfruck_contabo.models.all_of_list_assignment_response_pagination import AllOfListAssignmentResponsePagination
from pfruck_contabo.models.all_of_list_image_response_links import AllOfListImageResponseLinks
from pfruck_contabo.models.all_of_list_image_response_pagination import AllOfListImageResponsePagination
from pfruck_contabo.models.all_of_list_instances_actions_audit_response_links import AllOfListInstancesActionsAuditResponseLinks
from pfruck_contabo.models.all_of_list_instances_actions_audit_response_pagination import AllOfListInstancesActionsAuditResponsePagination
from pfruck_contabo.models.all_of_list_instances_audit_response_links import AllOfListInstancesAuditResponseLinks
from pfruck_contabo.models.all_of_list_instances_audit_response_pagination import AllOfListInstancesAuditResponsePagination
from pfruck_contabo.models.all_of_list_instances_response_links import AllOfListInstancesResponseLinks
from pfruck_contabo.models.all_of_list_instances_response_pagination import AllOfListInstancesResponsePagination
from pfruck_contabo.models.all_of_list_role_audit_response_links import AllOfListRoleAuditResponseLinks
from pfruck_contabo.models.all_of_list_role_response_links import AllOfListRoleResponseLinks
from pfruck_contabo.models.all_of_list_role_response_pagination import AllOfListRoleResponsePagination
from pfruck_contabo.models.all_of_list_secret_audit_response_links import AllOfListSecretAuditResponseLinks
from pfruck_contabo.models.all_of_list_secret_audit_response_pagination import AllOfListSecretAuditResponsePagination
from pfruck_contabo.models.all_of_list_secret_response_links import AllOfListSecretResponseLinks
from pfruck_contabo.models.all_of_list_secret_response_pagination import AllOfListSecretResponsePagination
from pfruck_contabo.models.all_of_list_snapshot_response_links import AllOfListSnapshotResponseLinks
from pfruck_contabo.models.all_of_list_snapshot_response_pagination import AllOfListSnapshotResponsePagination
from pfruck_contabo.models.all_of_list_snapshots_audit_response_links import AllOfListSnapshotsAuditResponseLinks
from pfruck_contabo.models.all_of_list_snapshots_audit_response_pagination import AllOfListSnapshotsAuditResponsePagination
from pfruck_contabo.models.all_of_list_tag_audits_response_links import AllOfListTagAuditsResponseLinks
from pfruck_contabo.models.all_of_list_tag_audits_response_pagination import AllOfListTagAuditsResponsePagination
from pfruck_contabo.models.all_of_list_tag_response_links import AllOfListTagResponseLinks
from pfruck_contabo.models.all_of_list_tag_response_pagination import AllOfListTagResponsePagination
from pfruck_contabo.models.all_of_list_user_audit_response_links import AllOfListUserAuditResponseLinks
from pfruck_contabo.models.all_of_list_user_audit_response_pagination import AllOfListUserAuditResponsePagination
from pfruck_contabo.models.all_of_list_user_response_links import AllOfListUserResponseLinks
from pfruck_contabo.models.all_of_list_user_response_pagination import AllOfListUserResponsePagination
from pfruck_contabo.models.all_of_reinstall_instance_response_links import AllOfReinstallInstanceResponseLinks
from pfruck_contabo.models.all_of_rollback_snapshot_response_links import AllOfRollbackSnapshotResponseLinks
from pfruck_contabo.models.all_of_update_custom_image_response_links import AllOfUpdateCustomImageResponseLinks
from pfruck_contabo.models.all_of_update_role_response_links import AllOfUpdateRoleResponseLinks
from pfruck_contabo.models.all_of_update_secret_response_links import AllOfUpdateSecretResponseLinks
from pfruck_contabo.models.all_of_update_snapshot_response_links import AllOfUpdateSnapshotResponseLinks
from pfruck_contabo.models.all_of_update_tag_response_links import AllOfUpdateTagResponseLinks
from pfruck_contabo.models.all_of_update_user_response_links import AllOfUpdateUserResponseLinks
from pfruck_contabo.models.api_permissions_response import ApiPermissionsResponse
from pfruck_contabo.models.assignment_audit_response import AssignmentAuditResponse
from pfruck_contabo.models.assignment_response import AssignmentResponse
from pfruck_contabo.models.cancel_instance_response import CancelInstanceResponse
from pfruck_contabo.models.cancel_instance_response_data import CancelInstanceResponseData
from pfruck_contabo.models.client_response import ClientResponse
from pfruck_contabo.models.client_secret_response import ClientSecretResponse
from pfruck_contabo.models.create_assignment_response import CreateAssignmentResponse
from pfruck_contabo.models.create_custom_image_request import CreateCustomImageRequest
from pfruck_contabo.models.create_custom_image_response import CreateCustomImageResponse
from pfruck_contabo.models.create_custom_image_response_data import CreateCustomImageResponseData
from pfruck_contabo.models.create_instance_request import CreateInstanceRequest
from pfruck_contabo.models.create_instance_response import CreateInstanceResponse
from pfruck_contabo.models.create_instance_response_data import CreateInstanceResponseData
from pfruck_contabo.models.create_role_request import CreateRoleRequest
from pfruck_contabo.models.create_role_response import CreateRoleResponse
from pfruck_contabo.models.create_role_response_data import CreateRoleResponseData
from pfruck_contabo.models.create_secret_request import CreateSecretRequest
from pfruck_contabo.models.create_secret_response import CreateSecretResponse
from pfruck_contabo.models.create_snapshot_request import CreateSnapshotRequest
from pfruck_contabo.models.create_snapshot_response import CreateSnapshotResponse
from pfruck_contabo.models.create_snapshot_response_data import CreateSnapshotResponseData
from pfruck_contabo.models.create_tag_request import CreateTagRequest
from pfruck_contabo.models.create_tag_response import CreateTagResponse
from pfruck_contabo.models.create_tag_response_data import CreateTagResponseData
from pfruck_contabo.models.create_user_request import CreateUserRequest
from pfruck_contabo.models.create_user_response import CreateUserResponse
from pfruck_contabo.models.create_user_response_data import CreateUserResponseData
from pfruck_contabo.models.custom_images_stats_response import CustomImagesStatsResponse
from pfruck_contabo.models.custom_images_stats_response_data import CustomImagesStatsResponseData
from pfruck_contabo.models.find_assignment_response import FindAssignmentResponse
from pfruck_contabo.models.find_client_response import FindClientResponse
from pfruck_contabo.models.find_image_response import FindImageResponse
from pfruck_contabo.models.find_instance_response import FindInstanceResponse
from pfruck_contabo.models.find_role_response import FindRoleResponse
from pfruck_contabo.models.find_secret_response import FindSecretResponse
from pfruck_contabo.models.find_snapshot_response import FindSnapshotResponse
from pfruck_contabo.models.find_tag_response import FindTagResponse
from pfruck_contabo.models.find_user_response import FindUserResponse
from pfruck_contabo.models.generate_client_secret_response import GenerateClientSecretResponse
from pfruck_contabo.models.image_audit_response import ImageAuditResponse
from pfruck_contabo.models.image_audit_response_data import ImageAuditResponseData
from pfruck_contabo.models.image_response import ImageResponse
from pfruck_contabo.models.instance_response import InstanceResponse
from pfruck_contabo.models.instance_restart_action_response import InstanceRestartActionResponse
from pfruck_contabo.models.instance_restart_action_response_data import InstanceRestartActionResponseData
from pfruck_contabo.models.instance_start_action_response import InstanceStartActionResponse
from pfruck_contabo.models.instance_start_action_response_data import InstanceStartActionResponseData
from pfruck_contabo.models.instance_status import InstanceStatus
from pfruck_contabo.models.instance_stop_action_response import InstanceStopActionResponse
from pfruck_contabo.models.instance_stop_action_response_data import InstanceStopActionResponseData
from pfruck_contabo.models.instances_actions_audit_response import InstancesActionsAuditResponse
from pfruck_contabo.models.instances_audit_response import InstancesAuditResponse
from pfruck_contabo.models.ip_config import IpConfig
from pfruck_contabo.models.ip_v4 import IpV4
from pfruck_contabo.models.ip_v6 import IpV6
from pfruck_contabo.models.links import Links
from pfruck_contabo.models.list_api_permission_response import ListApiPermissionResponse
from pfruck_contabo.models.list_assignment_audits_response import ListAssignmentAuditsResponse
from pfruck_contabo.models.list_assignment_response import ListAssignmentResponse
from pfruck_contabo.models.list_image_response import ListImageResponse
from pfruck_contabo.models.list_image_response_data import ListImageResponseData
from pfruck_contabo.models.list_instances_actions_audit_response import ListInstancesActionsAuditResponse
from pfruck_contabo.models.list_instances_audit_response import ListInstancesAuditResponse
from pfruck_contabo.models.list_instances_response import ListInstancesResponse
from pfruck_contabo.models.list_instances_response_data import ListInstancesResponseData
from pfruck_contabo.models.list_role_audit_response import ListRoleAuditResponse
from pfruck_contabo.models.list_role_response import ListRoleResponse
from pfruck_contabo.models.list_secret_audit_response import ListSecretAuditResponse
from pfruck_contabo.models.list_secret_response import ListSecretResponse
from pfruck_contabo.models.list_snapshot_response import ListSnapshotResponse
from pfruck_contabo.models.list_snapshots_audit_response import ListSnapshotsAuditResponse
from pfruck_contabo.models.list_tag_audits_response import ListTagAuditsResponse
from pfruck_contabo.models.list_tag_response import ListTagResponse
from pfruck_contabo.models.list_user_audit_response import ListUserAuditResponse
from pfruck_contabo.models.list_user_response import ListUserResponse
from pfruck_contabo.models.pagination_meta import PaginationMeta
from pfruck_contabo.models.reinstall_instance_request import ReinstallInstanceRequest
from pfruck_contabo.models.reinstall_instance_response import ReinstallInstanceResponse
from pfruck_contabo.models.reinstall_instance_response_data import ReinstallInstanceResponseData
from pfruck_contabo.models.resource_permissions_response import ResourcePermissionsResponse
from pfruck_contabo.models.role_audit_response import RoleAuditResponse
from pfruck_contabo.models.role_response import RoleResponse
from pfruck_contabo.models.rollback_snapshot_response import RollbackSnapshotResponse
from pfruck_contabo.models.secret_audit_response import SecretAuditResponse
from pfruck_contabo.models.secret_response import SecretResponse
from pfruck_contabo.models.self_links import SelfLinks
from pfruck_contabo.models.snapshot_response import SnapshotResponse
from pfruck_contabo.models.snapshots_audit_response import SnapshotsAuditResponse
from pfruck_contabo.models.tag_assignment_self_links import TagAssignmentSelfLinks
from pfruck_contabo.models.tag_audit_response import TagAuditResponse
from pfruck_contabo.models.tag_response import TagResponse
from pfruck_contabo.models.tag_response1 import TagResponse1
from pfruck_contabo.models.update_custom_image_request import UpdateCustomImageRequest
from pfruck_contabo.models.update_custom_image_response import UpdateCustomImageResponse
from pfruck_contabo.models.update_custom_image_response_data import UpdateCustomImageResponseData
from pfruck_contabo.models.update_role_request import UpdateRoleRequest
from pfruck_contabo.models.update_role_response import UpdateRoleResponse
from pfruck_contabo.models.update_secret_request import UpdateSecretRequest
from pfruck_contabo.models.update_secret_response import UpdateSecretResponse
from pfruck_contabo.models.update_snapshot_request import UpdateSnapshotRequest
from pfruck_contabo.models.update_snapshot_response import UpdateSnapshotResponse
from pfruck_contabo.models.update_tag_request import UpdateTagRequest
from pfruck_contabo.models.update_tag_response import UpdateTagResponse
from pfruck_contabo.models.update_user_request import UpdateUserRequest
from pfruck_contabo.models.update_user_response import UpdateUserResponse
from pfruck_contabo.models.user_audit_response import UserAuditResponse
from pfruck_contabo.models.user_response import UserResponse
