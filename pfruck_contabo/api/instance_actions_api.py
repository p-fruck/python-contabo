"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from pfruck_contabo.api_client import ApiClient, Endpoint as _Endpoint
from pfruck_contabo.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from pfruck_contabo.model.instance_restart_action_response import InstanceRestartActionResponse
from pfruck_contabo.model.instance_shutdown_action_response import InstanceShutdownActionResponse
from pfruck_contabo.model.instance_start_action_response import InstanceStartActionResponse
from pfruck_contabo.model.instance_stop_action_response import InstanceStopActionResponse


class InstanceActionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.restart_endpoint = _Endpoint(
            settings={
                'response_type': (InstanceRestartActionResponse,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/v1/compute/instances/{instanceId}/actions/restart',
                'operation_id': 'restart',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_request_id',
                    'instance_id',
                    'x_trace_id',
                ],
                'required': [
                    'x_request_id',
                    'instance_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'x_request_id',
                ]
            },
            root_map={
                'validations': {
                    ('x_request_id',): {

                        'regex': {
                            'pattern': r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-5][0-9A-Fa-f]{3}-[089abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_request_id':
                        (str,),
                    'instance_id':
                        (int,),
                    'x_trace_id':
                        (str,),
                },
                'attribute_map': {
                    'x_request_id': 'x-request-id',
                    'instance_id': 'instanceId',
                    'x_trace_id': 'x-trace-id',
                },
                'location_map': {
                    'x_request_id': 'header',
                    'instance_id': 'path',
                    'x_trace_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.shutdown_endpoint = _Endpoint(
            settings={
                'response_type': (InstanceShutdownActionResponse,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/v1/compute/instances/{instanceId}/actions/shutdown',
                'operation_id': 'shutdown',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_request_id',
                    'instance_id',
                    'x_trace_id',
                ],
                'required': [
                    'x_request_id',
                    'instance_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'x_request_id',
                ]
            },
            root_map={
                'validations': {
                    ('x_request_id',): {

                        'regex': {
                            'pattern': r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-5][0-9A-Fa-f]{3}-[089abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_request_id':
                        (str,),
                    'instance_id':
                        (int,),
                    'x_trace_id':
                        (str,),
                },
                'attribute_map': {
                    'x_request_id': 'x-request-id',
                    'instance_id': 'instanceId',
                    'x_trace_id': 'x-trace-id',
                },
                'location_map': {
                    'x_request_id': 'header',
                    'instance_id': 'path',
                    'x_trace_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.start_endpoint = _Endpoint(
            settings={
                'response_type': (InstanceStartActionResponse,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/v1/compute/instances/{instanceId}/actions/start',
                'operation_id': 'start',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_request_id',
                    'instance_id',
                    'x_trace_id',
                ],
                'required': [
                    'x_request_id',
                    'instance_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'x_request_id',
                ]
            },
            root_map={
                'validations': {
                    ('x_request_id',): {

                        'regex': {
                            'pattern': r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-5][0-9A-Fa-f]{3}-[089abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_request_id':
                        (str,),
                    'instance_id':
                        (int,),
                    'x_trace_id':
                        (str,),
                },
                'attribute_map': {
                    'x_request_id': 'x-request-id',
                    'instance_id': 'instanceId',
                    'x_trace_id': 'x-trace-id',
                },
                'location_map': {
                    'x_request_id': 'header',
                    'instance_id': 'path',
                    'x_trace_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.stop_endpoint = _Endpoint(
            settings={
                'response_type': (InstanceStopActionResponse,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/v1/compute/instances/{instanceId}/actions/stop',
                'operation_id': 'stop',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_request_id',
                    'instance_id',
                    'x_trace_id',
                ],
                'required': [
                    'x_request_id',
                    'instance_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'x_request_id',
                ]
            },
            root_map={
                'validations': {
                    ('x_request_id',): {

                        'regex': {
                            'pattern': r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-5][0-9A-Fa-f]{3}-[089abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_request_id':
                        (str,),
                    'instance_id':
                        (int,),
                    'x_trace_id':
                        (str,),
                },
                'attribute_map': {
                    'x_request_id': 'x-request-id',
                    'instance_id': 'instanceId',
                    'x_trace_id': 'x-trace-id',
                },
                'location_map': {
                    'x_request_id': 'header',
                    'instance_id': 'path',
                    'x_trace_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def restart(
        self,
        x_request_id,
        instance_id,
        **kwargs
    ):
        """Restart a compute instance / resource identified by its id  # noqa: E501

        Restarting a compute instance / resource is like powering off and powering on again a real server. If the compute instance / resource is already started it will stopped and started again. If it is stopped the compute instance / resource will be started. So please be aware that data may be lost. You may check the current status anytime when getting information about a compute instance / resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.restart(x_request_id, instance_id, async_req=True)
        >>> result = thread.get()

        Args:
            x_request_id (str): [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
            instance_id (int): The identifier of the compute instance / resource to be started.

        Keyword Args:
            x_trace_id (str): Identifier to trace group of requests.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InstanceRestartActionResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['x_request_id'] = \
            x_request_id
        kwargs['instance_id'] = \
            instance_id
        return self.restart_endpoint.call_with_http_info(**kwargs)

    def shutdown(
        self,
        x_request_id,
        instance_id,
        **kwargs
    ):
        """Shutdown compute instance / resource by its id  # noqa: E501

        Shutdown an compute instance / resource. This is similar to pressing the power button on a physical machine. This will send an ACPI event for the guest OS, which should then proceed to a clean shutdown.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.shutdown(x_request_id, instance_id, async_req=True)
        >>> result = thread.get()

        Args:
            x_request_id (str): [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
            instance_id (int): The identifier of the instance to be shutdown

        Keyword Args:
            x_trace_id (str): Identifier to trace group of requests.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InstanceShutdownActionResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['x_request_id'] = \
            x_request_id
        kwargs['instance_id'] = \
            instance_id
        return self.shutdown_endpoint.call_with_http_info(**kwargs)

    def start(
        self,
        x_request_id,
        instance_id,
        **kwargs
    ):
        """Start a compute instance / resource identified by its id  # noqa: E501

        Starting a compute instance / resource is like powering on a real server. If the compute instance / resource is already started nothing will happen. You may check the current status anytime when getting information about a compute instance / resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.start(x_request_id, instance_id, async_req=True)
        >>> result = thread.get()

        Args:
            x_request_id (str): [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
            instance_id (int): The identifier of the compute instance / resource to be started.

        Keyword Args:
            x_trace_id (str): Identifier to trace group of requests.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InstanceStartActionResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['x_request_id'] = \
            x_request_id
        kwargs['instance_id'] = \
            instance_id
        return self.start_endpoint.call_with_http_info(**kwargs)

    def stop(
        self,
        x_request_id,
        instance_id,
        **kwargs
    ):
        """Stop compute instance / resource by its id  # noqa: E501

        Stopping a compute instance / resource is like powering off a real server. So please be aware that data may be lost. Alternatively you may log in and shut your compute instance / resource gracefully via the operating system. If the compute instance / resource is already stopped nothing will happen. You may check the current status anytime when getting information about a compute instance / resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.stop(x_request_id, instance_id, async_req=True)
        >>> result = thread.get()

        Args:
            x_request_id (str): [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
            instance_id (int): The identifier of the instance to stop

        Keyword Args:
            x_trace_id (str): Identifier to trace group of requests.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InstanceStopActionResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['x_request_id'] = \
            x_request_id
        kwargs['instance_id'] = \
            instance_id
        return self.stop_endpoint.call_with_http_info(**kwargs)

