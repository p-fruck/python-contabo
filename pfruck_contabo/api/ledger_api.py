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
from pfruck_contabo.model.list_ledger_entries_reponse import ListLedgerEntriesReponse


class LedgerApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.retrieve_ledger_entries_list_endpoint = _Endpoint(
            settings={
                'response_type': (ListLedgerEntriesReponse,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/v1/ledger/ledger-entries',
                'operation_id': 'retrieve_ledger_entries_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_request_id',
                    'x_trace_id',
                    'page',
                    'size',
                    'order_by',
                    'transaction_start_date',
                    'transaction_end_date',
                ],
                'required': [
                    'x_request_id',
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
                    'x_trace_id':
                        (str,),
                    'page':
                        (int,),
                    'size':
                        (int,),
                    'order_by':
                        ([str],),
                    'transaction_start_date':
                        (str,),
                    'transaction_end_date':
                        (str,),
                },
                'attribute_map': {
                    'x_request_id': 'x-request-id',
                    'x_trace_id': 'x-trace-id',
                    'page': 'page',
                    'size': 'size',
                    'order_by': 'orderBy',
                    'transaction_start_date': 'transactionStartDate',
                    'transaction_end_date': 'transactionEndDate',
                },
                'location_map': {
                    'x_request_id': 'header',
                    'x_trace_id': 'header',
                    'page': 'query',
                    'size': 'query',
                    'order_by': 'query',
                    'transaction_start_date': 'query',
                    'transaction_end_date': 'query',
                },
                'collection_format_map': {
                    'order_by': 'multi',
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

    def retrieve_ledger_entries_list(
        self,
        x_request_id,
        **kwargs
    ):
        """List ledger entries  # noqa: E501

        List all transactions for your account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.retrieve_ledger_entries_list(x_request_id, async_req=True)
        >>> result = thread.get()

        Args:
            x_request_id (str): [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.

        Keyword Args:
            x_trace_id (str): Identifier to trace group of requests.. [optional]
            page (int): Number of page to be fetched.. [optional]
            size (int): Number of elements per page.. [optional]
            order_by ([str]): Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`.. [optional]
            transaction_start_date (str): Start date of the interval in which you want to see the transactions. [optional]
            transaction_end_date (str): Start date of the interval in which you want to see the transactions. [optional]
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
            ListLedgerEntriesReponse
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
        return self.retrieve_ledger_entries_list_endpoint.call_with_http_info(**kwargs)
