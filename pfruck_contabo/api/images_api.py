# coding: utf-8

"""
    Contabo API

    # Introduction  Contabo API allows you to manage your resources using HTTP requests. This documentation includes a set of HTTP endpoints that are designed to RESTful principles. Each endpoint includes descriptions, request syntax, and examples.  Contabo provides also a CLI tool which enables you to manage your resources easily from the command line. [CLI Download and  Installation instructions.](https://github.com/contabo/cntb)  ## Getting Started  In order to use the Contabo API you will need the following credentials which are available from the [Customer Control Panel](https://my.contabo.com/api/details): 1. ClientId 2. ClientSecret 3. API User (your email address to login to the [Customer Control Panel](https://my.contabo.com/api/details)) 4. API Password (this is a new password which you'll set or change in the [Customer Control Panel](https://my.contabo.com/api/details))  You can either use the API directly or by using the `cntb` CLI (Command Line Interface) tool.  ### Using the API directly  #### Via `curl` for Linux/Unix like systems  This requires `curl` and `jq` in your shell (e.g. `bash`, `zsh`). Please replace the first four placeholders with actual values.  ```sh CLIENT_ID=<ClientId from Customer Control Panel> CLIENT_SECRET=<ClientSecret from Customer Control Panel> API_USER=<API User from Customer Control Panel> API_PASSWORD='<API Password from Customer Control Panel>' ACCESS_TOKEN=$(curl -d \"client_id=$CLIENT_ID\" -d \"client_secret=$CLIENT_SECRET\" --data-urlencode \"username=$API_USER\" --data-urlencode \"password=$API_PASSWORD\" -d 'grant_type=password' 'https://auth.contabo.com/auth/realms/contabo/protocol/openid-connect/token' | jq -r '.access_token') # get list of your instances curl -X GET -H \"Authorization: Bearer $ACCESS_TOKEN\" -H \"x-request-id: 51A87ECD-754E-4104-9C54-D01AD0F83406\" \"https://api.contabo.com/v1/compute/instances\" | jq ```  #### Via `PowerShell` for Windows  Please open `PowerShell` and execute the following code after replacing the first four placeholders with actual values.  ```powershell $client_id='<ClientId from Customer Control Panel>' $client_secret='<ClientSecret from Customer Control Panel>' $api_user='<API User from Customer Control Panel>' $api_password='<API Password from Customer Control Panel>' $body = @{grant_type='password' client_id=$client_id client_secret=$client_secret username=$api_user password=$api_password} $response = Invoke-WebRequest -Uri 'https://auth.contabo.com/auth/realms/contabo/protocol/openid-connect/token' -Method 'POST' -Body $body $access_token = (ConvertFrom-Json $([String]::new($response.Content))).access_token # get list of your instances $headers = @{} $headers.Add(\"Authorization\",\"Bearer $access_token\") $headers.Add(\"x-request-id\",\"51A87ECD-754E-4104-9C54-D01AD0F83406\") Invoke-WebRequest -Uri 'https://api.contabo.com/v1/compute/instances' -Method 'GET' -Headers $headers ```  ### Using the Contabo API via the `cntb` CLI tool  1. Download `cntb` for your operating system (MacOS, Windows and Linux supported) [here](https://github.com/contabo/cntb) 2. Unzip the downloaded file 3. You might move the executable to any location on your disk. You may update your `PATH` environment variable for easier invocation. 4. Configure it once to use your credentials           ```sh    cntb config set-credentials --oauth2-clientid=<ClientId from Customer Control Panel> --oauth2-client-secret=<ClientSecret from Customer Control Panel> --oauth2-user=<API User from Customer Control Panel> --oauth2-password=<API Password from Customer Control Panel>    ```  5. Use the CLI           ```sh    # get list of your instances    cntb get instances    # help    cntb help    ```  ## API Overiew  ### [Compute Mangement](#tag/Instances)  The Compute Management API allows you to manage compute resources (e.g. creation, deletion, starting, stopping) of VPS and VDS (please note that Storage VPS are not supported via API or CLI) as well as managing snapshots and custom images. It also offers you to take advantage of [cloud-init](https://cloud-init.io/) at least on our default / standard images (for custom images you'll need to provide cloud-init support packages). The API offers provisioning of cloud-init scripts via the `user_data` field.  Custom images must be provided in `.qcow2` or `.iso` format. This gives you even more flexibilty for setting up your environment.  ### [Secrets Mangement](#tag/Secrets)  You can optionally save your passwords or public ssh keys using the Secrets Managemnt API. You are not required to use it there will be no functional disadvantages.  By using that API you can easily reuse you public ssh keys when setting up different servers without the need to look them up every time. It can also be used to allow Contabo Supporters to access your machine without sending the passwords via potentially unsecure emails.  ### [User Management](#tag/Users)  If you need to allow other persons or automation scripts to access specific API endpoints resp. resources the User Mangement API comes into play. With that API you are able to manage users having possibly restricted access. You are free to define those restrictions to fit your needs. So beside an arbitrary number of users you basically define any number of so called `roles`. Roles allows access and must be one of the following types:  * `apiPermission`          This allows you to specify a restriction to certain functions of an API by allowing control over POST (=Create), GET (=Read), PUT/PATCH (=Update) and DELETE (=Delete) methods for each API endpoint (URL) individually. * `resourcePermission`          In order to restrict access to specific resources create a role with `resourcePermission` type by specifying any number of [tags](#tag-management). These tags need to be assigned to resources for them to take effect. E.g. a tag could be assiged to several compute resources. So that a user with that role (and of course access to the API endpoints via `apiPermission` role type) could only access those compute resources.  The `roles` are then assigned to a `user`. You can assign one or several roles regardless of the role's type. Of course you could also assign a user `admin` privileges without specifying any roles.  ### [Tag Management](#tag/Tags)  The Tag Management API allows you to manage your tags in order to organize your resources in a more convenient way. Simply assign a tag to resources like a compute resource to manage them.The assignments of tags to resources will also enable you to control access to these specific resources to users via the [User Management API](#user-management). For convenience reasons you might choose a color for tag. The Customer Control Panel will use that color to display the tags.  ## Requests  The Contabo API supports HTTP requests like mentioned below. Not every endpoint supports all methods. The allowed methods are listed within this documentation.  Method | Description ---    | --- GET    | To retrieve information about a resource, use the GET method.<br>The data is returned as a JSON object. GET methods are read-only and do not affect any resources. POST   | Issue a POST method to create a new object. Include all needed attributes in the request body encoded as JSON. PATCH  | Some resources support partial modification with PATCH,<br>which modifies specific attributes without updating the entire object representation. PUT    | Use the PUT method to update information about a resource.<br>PUT will set new values on the item without regard to their current values. DELETE | Use the DELETE method to destroy a resource in your account.<br>If it is not found, the operation will return a 4xx error and an appropriate message.  ## Responses  Usually the Contabo API should respond to your requests. The data returned is in [JSON](https://www.json.org/) format allowing easy processing in any programming language or tools.  As common for HTTP requests you will get back a so called HTTP status code. This gives you overall information about success or error. The following table lists common HTTP status codes.  Please note that the description of the endpoints and methods are not listing all possibly status codes in detail as they are generic. Only special return codes with their resp. response data are explicitly listed.  Response Code | Description --- | --- 200 | The response contains your requested information. 201 | Your request was accepted. The resource was created. 204 | Your request succeeded, there is no additional information returned. 400 | Your request was malformed. 401 | You did not supply valid authentication credentials. 402 | Request refused as it requires additional payed service. 403 | You are not allowed to perform the request. 404 | No results were found for your request or resource does not exist. 409 | Conflict with resources. For example violation of unique data contraints detected when trying to create or change resources. 429 | Rate-limit reached. Please wait for some time before doing more requests. 500 | We were unable to perform the request due to server-side problems. In such cases please retry or contact the support.  Not every endpoint returns data. For example DELETE requests usually don't return any data. All others do return data. For easy handling the return values consists of metadata denoted with and underscore (\"_\") like `_links` or `_pagination`. The actual data is returned in a field called `data`. For convenience reasons this `data` field is always returned as an array even if it consists of only one single element.  Some general details about Contabo API from [Contabo](https://contabo.com).   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@contabo.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pfruck_contabo.api_client import ApiClient


class ImagesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_custom_image(self, body, x_request_id, **kwargs):  # noqa: E501
        """Provide a custom image  # noqa: E501

        In order to provide a custom image please specify an URL from where the image can be directly downloaded. A custom image must be in either `.iso` or `.qcow2` format. Other formats will be rejected. Please note that downloading can take a while depending on network speed resp. bandwidth and size of image. You can check the status by retrieving information about the image via a GET request. Download will be rejected if you have exceeded your limits.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_custom_image(body, x_request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateCustomImageRequest body: (required)
        :param str x_request_id: [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. (required)
        :param str x_trace_id: Identifier to trace group of requests.
        :return: CreateCustomImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_custom_image_with_http_info(body, x_request_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_custom_image_with_http_info(body, x_request_id, **kwargs)  # noqa: E501
            return data

    def create_custom_image_with_http_info(self, body, x_request_id, **kwargs):  # noqa: E501
        """Provide a custom image  # noqa: E501

        In order to provide a custom image please specify an URL from where the image can be directly downloaded. A custom image must be in either `.iso` or `.qcow2` format. Other formats will be rejected. Please note that downloading can take a while depending on network speed resp. bandwidth and size of image. You can check the status by retrieving information about the image via a GET request. Download will be rejected if you have exceeded your limits.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_custom_image_with_http_info(body, x_request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateCustomImageRequest body: (required)
        :param str x_request_id: [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. (required)
        :param str x_trace_id: Identifier to trace group of requests.
        :return: CreateCustomImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_request_id', 'x_trace_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_custom_image" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_custom_image`")  # noqa: E501
        # verify the required parameter 'x_request_id' is set
        if ('x_request_id' not in params or
                params['x_request_id'] is None):
            raise ValueError("Missing the required parameter `x_request_id` when calling `create_custom_image`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['x-request-id'] = params['x_request_id']  # noqa: E501
        if 'x_trace_id' in params:
            header_params['x-trace-id'] = params['x_trace_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/compute/images', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateCustomImageResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_image(self, x_request_id, image_id, **kwargs):  # noqa: E501
        """Delete an uploaded custom image by its id  # noqa: E501

        Your are free to delete a previously uploaded custom images at any time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_image(x_request_id, image_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. (required)
        :param str image_id: The identifier of the image (required)
        :param str x_trace_id: Identifier to trace group of requests.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_image_with_http_info(x_request_id, image_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_image_with_http_info(x_request_id, image_id, **kwargs)  # noqa: E501
            return data

    def delete_image_with_http_info(self, x_request_id, image_id, **kwargs):  # noqa: E501
        """Delete an uploaded custom image by its id  # noqa: E501

        Your are free to delete a previously uploaded custom images at any time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_image_with_http_info(x_request_id, image_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. (required)
        :param str image_id: The identifier of the image (required)
        :param str x_trace_id: Identifier to trace group of requests.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_request_id', 'image_id', 'x_trace_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_image" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_request_id' is set
        if ('x_request_id' not in params or
                params['x_request_id'] is None):
            raise ValueError("Missing the required parameter `x_request_id` when calling `delete_image`")  # noqa: E501
        # verify the required parameter 'image_id' is set
        if ('image_id' not in params or
                params['image_id'] is None):
            raise ValueError("Missing the required parameter `image_id` when calling `delete_image`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'image_id' in params:
            path_params['imageId'] = params['image_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['x-request-id'] = params['x_request_id']  # noqa: E501
        if 'x_trace_id' in params:
            header_params['x-trace-id'] = params['x_trace_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/compute/images/{imageId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_custom_images_stats(self, x_request_id, **kwargs):  # noqa: E501
        """List statistics regarding the customer's custom images  # noqa: E501

        List statistics regarding the customer's custom images such as the number of custom images uploaded, used disk space, free available disk space and total available disk space  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_custom_images_stats(x_request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. (required)
        :param str x_trace_id: Identifier to trace group of requests.
        :return: CustomImagesStatsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_custom_images_stats_with_http_info(x_request_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_custom_images_stats_with_http_info(x_request_id, **kwargs)  # noqa: E501
            return data

    def retrieve_custom_images_stats_with_http_info(self, x_request_id, **kwargs):  # noqa: E501
        """List statistics regarding the customer's custom images  # noqa: E501

        List statistics regarding the customer's custom images such as the number of custom images uploaded, used disk space, free available disk space and total available disk space  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_custom_images_stats_with_http_info(x_request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. (required)
        :param str x_trace_id: Identifier to trace group of requests.
        :return: CustomImagesStatsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_request_id', 'x_trace_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_custom_images_stats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_request_id' is set
        if ('x_request_id' not in params or
                params['x_request_id'] is None):
            raise ValueError("Missing the required parameter `x_request_id` when calling `retrieve_custom_images_stats`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['x-request-id'] = params['x_request_id']  # noqa: E501
        if 'x_trace_id' in params:
            header_params['x-trace-id'] = params['x_trace_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/compute/images/stats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomImagesStatsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_image(self, x_request_id, image_id, **kwargs):  # noqa: E501
        """Get details about a specific image by its id  # noqa: E501

        Get details about a specific image. This could be either a standard or custom image. In case of an custom image you can also check the download status.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_image(x_request_id, image_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. (required)
        :param str image_id: The identifier of the image (required)
        :param str x_trace_id: Identifier to trace group of requests.
        :return: FindImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_image_with_http_info(x_request_id, image_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_image_with_http_info(x_request_id, image_id, **kwargs)  # noqa: E501
            return data

    def retrieve_image_with_http_info(self, x_request_id, image_id, **kwargs):  # noqa: E501
        """Get details about a specific image by its id  # noqa: E501

        Get details about a specific image. This could be either a standard or custom image. In case of an custom image you can also check the download status.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_image_with_http_info(x_request_id, image_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. (required)
        :param str image_id: The identifier of the image (required)
        :param str x_trace_id: Identifier to trace group of requests.
        :return: FindImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_request_id', 'image_id', 'x_trace_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_image" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_request_id' is set
        if ('x_request_id' not in params or
                params['x_request_id'] is None):
            raise ValueError("Missing the required parameter `x_request_id` when calling `retrieve_image`")  # noqa: E501
        # verify the required parameter 'image_id' is set
        if ('image_id' not in params or
                params['image_id'] is None):
            raise ValueError("Missing the required parameter `image_id` when calling `retrieve_image`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'image_id' in params:
            path_params['imageId'] = params['image_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['x-request-id'] = params['x_request_id']  # noqa: E501
        if 'x_trace_id' in params:
            header_params['x-trace-id'] = params['x_trace_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/compute/images/{imageId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FindImageResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_image_list(self, x_request_id, **kwargs):  # noqa: E501
        """List available standard and custom images  # noqa: E501

        List and filter all available standard images provided by [Contabo](https://contabo.com) and your uploaded custom images.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_image_list(x_request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. (required)
        :param str x_trace_id: Identifier to trace group of requests.
        :param int page: Number of page to be fetched.
        :param int size: Number of elements per page.
        :param list[str] order_by: Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`.
        :param str name: The name of the image
        :param bool standard_image: Flag indicating that image is either a standard (true) or a custom image (false)
        :return: ListImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_image_list_with_http_info(x_request_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_image_list_with_http_info(x_request_id, **kwargs)  # noqa: E501
            return data

    def retrieve_image_list_with_http_info(self, x_request_id, **kwargs):  # noqa: E501
        """List available standard and custom images  # noqa: E501

        List and filter all available standard images provided by [Contabo](https://contabo.com) and your uploaded custom images.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_image_list_with_http_info(x_request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. (required)
        :param str x_trace_id: Identifier to trace group of requests.
        :param int page: Number of page to be fetched.
        :param int size: Number of elements per page.
        :param list[str] order_by: Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`.
        :param str name: The name of the image
        :param bool standard_image: Flag indicating that image is either a standard (true) or a custom image (false)
        :return: ListImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_request_id', 'x_trace_id', 'page', 'size', 'order_by', 'name', 'standard_image']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_image_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_request_id' is set
        if ('x_request_id' not in params or
                params['x_request_id'] is None):
            raise ValueError("Missing the required parameter `x_request_id` when calling `retrieve_image_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('orderBy', params['order_by']))  # noqa: E501
            collection_formats['orderBy'] = 'multi'  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'standard_image' in params:
            query_params.append(('standardImage', params['standard_image']))  # noqa: E501

        header_params = {}
        if 'x_request_id' in params:
            header_params['x-request-id'] = params['x_request_id']  # noqa: E501
        if 'x_trace_id' in params:
            header_params['x-trace-id'] = params['x_trace_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/compute/images', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListImageResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_image(self, body, x_request_id, image_id, **kwargs):  # noqa: E501
        """Update custom image name by its id  # noqa: E501

        Update name of the custom image.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_image(body, x_request_id, image_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateCustomImageRequest body: (required)
        :param str x_request_id: [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. (required)
        :param str image_id: The identifier of the image (required)
        :param str x_trace_id: Identifier to trace group of requests.
        :return: UpdateCustomImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_image_with_http_info(body, x_request_id, image_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_image_with_http_info(body, x_request_id, image_id, **kwargs)  # noqa: E501
            return data

    def update_image_with_http_info(self, body, x_request_id, image_id, **kwargs):  # noqa: E501
        """Update custom image name by its id  # noqa: E501

        Update name of the custom image.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_image_with_http_info(body, x_request_id, image_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateCustomImageRequest body: (required)
        :param str x_request_id: [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. (required)
        :param str image_id: The identifier of the image (required)
        :param str x_trace_id: Identifier to trace group of requests.
        :return: UpdateCustomImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_request_id', 'image_id', 'x_trace_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_image" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_image`")  # noqa: E501
        # verify the required parameter 'x_request_id' is set
        if ('x_request_id' not in params or
                params['x_request_id'] is None):
            raise ValueError("Missing the required parameter `x_request_id` when calling `update_image`")  # noqa: E501
        # verify the required parameter 'image_id' is set
        if ('image_id' not in params or
                params['image_id'] is None):
            raise ValueError("Missing the required parameter `image_id` when calling `update_image`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'image_id' in params:
            path_params['imageId'] = params['image_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['x-request-id'] = params['x_request_id']  # noqa: E501
        if 'x_trace_id' in params:
            header_params['x-trace-id'] = params['x_trace_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/compute/images/{imageId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UpdateCustomImageResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
