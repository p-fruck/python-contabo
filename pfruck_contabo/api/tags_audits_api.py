# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from datetime import date
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from pfruck_contabo.models.list_tag_audits_response import ListTagAuditsResponse

from pfruck_contabo.api_client import ApiClient, RequestSerialized
from pfruck_contabo.api_response import ApiResponse
from pfruck_contabo.rest import RESTResponseType


class TagsAuditsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def retrieve_tag_audits_list(
        self,
        x_request_id: Annotated[str, Field(strict=True, description="[Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.")],
        x_trace_id: Annotated[Optional[StrictStr], Field(description="Identifier to trace group of requests.")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Number of page to be fetched.")] = None,
        size: Annotated[Optional[StrictInt], Field(description="Number of elements per page.")] = None,
        order_by: Annotated[Optional[List[StrictStr]], Field(description="Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`.")] = None,
        tag_id: Annotated[Optional[StrictInt], Field(description="The identifier of the tag.")] = None,
        request_id: Annotated[Optional[StrictStr], Field(description="The requestId of the API call which led to the change.")] = None,
        changed_by: Annotated[Optional[StrictStr], Field(description="UserId of the user which led to the change.")] = None,
        start_date: Annotated[Optional[date], Field(description="Start of search time range.")] = None,
        end_date: Annotated[Optional[date], Field(description="End of search time range.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ListTagAuditsResponse:
        """List history about your assignments (audit)

        List and filters the history about your assignments.

        :param x_request_id: [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. (required)
        :type x_request_id: str
        :param x_trace_id: Identifier to trace group of requests.
        :type x_trace_id: str
        :param page: Number of page to be fetched.
        :type page: int
        :param size: Number of elements per page.
        :type size: int
        :param order_by: Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`.
        :type order_by: List[str]
        :param tag_id: The identifier of the tag.
        :type tag_id: int
        :param request_id: The requestId of the API call which led to the change.
        :type request_id: str
        :param changed_by: UserId of the user which led to the change.
        :type changed_by: str
        :param start_date: Start of search time range.
        :type start_date: date
        :param end_date: End of search time range.
        :type end_date: date
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._retrieve_tag_audits_list_serialize(
            x_request_id=x_request_id,
            x_trace_id=x_trace_id,
            page=page,
            size=size,
            order_by=order_by,
            tag_id=tag_id,
            request_id=request_id,
            changed_by=changed_by,
            start_date=start_date,
            end_date=end_date,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListTagAuditsResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def retrieve_tag_audits_list_with_http_info(
        self,
        x_request_id: Annotated[str, Field(strict=True, description="[Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.")],
        x_trace_id: Annotated[Optional[StrictStr], Field(description="Identifier to trace group of requests.")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Number of page to be fetched.")] = None,
        size: Annotated[Optional[StrictInt], Field(description="Number of elements per page.")] = None,
        order_by: Annotated[Optional[List[StrictStr]], Field(description="Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`.")] = None,
        tag_id: Annotated[Optional[StrictInt], Field(description="The identifier of the tag.")] = None,
        request_id: Annotated[Optional[StrictStr], Field(description="The requestId of the API call which led to the change.")] = None,
        changed_by: Annotated[Optional[StrictStr], Field(description="UserId of the user which led to the change.")] = None,
        start_date: Annotated[Optional[date], Field(description="Start of search time range.")] = None,
        end_date: Annotated[Optional[date], Field(description="End of search time range.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ListTagAuditsResponse]:
        """List history about your assignments (audit)

        List and filters the history about your assignments.

        :param x_request_id: [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. (required)
        :type x_request_id: str
        :param x_trace_id: Identifier to trace group of requests.
        :type x_trace_id: str
        :param page: Number of page to be fetched.
        :type page: int
        :param size: Number of elements per page.
        :type size: int
        :param order_by: Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`.
        :type order_by: List[str]
        :param tag_id: The identifier of the tag.
        :type tag_id: int
        :param request_id: The requestId of the API call which led to the change.
        :type request_id: str
        :param changed_by: UserId of the user which led to the change.
        :type changed_by: str
        :param start_date: Start of search time range.
        :type start_date: date
        :param end_date: End of search time range.
        :type end_date: date
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._retrieve_tag_audits_list_serialize(
            x_request_id=x_request_id,
            x_trace_id=x_trace_id,
            page=page,
            size=size,
            order_by=order_by,
            tag_id=tag_id,
            request_id=request_id,
            changed_by=changed_by,
            start_date=start_date,
            end_date=end_date,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListTagAuditsResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def retrieve_tag_audits_list_without_preload_content(
        self,
        x_request_id: Annotated[str, Field(strict=True, description="[Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.")],
        x_trace_id: Annotated[Optional[StrictStr], Field(description="Identifier to trace group of requests.")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Number of page to be fetched.")] = None,
        size: Annotated[Optional[StrictInt], Field(description="Number of elements per page.")] = None,
        order_by: Annotated[Optional[List[StrictStr]], Field(description="Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`.")] = None,
        tag_id: Annotated[Optional[StrictInt], Field(description="The identifier of the tag.")] = None,
        request_id: Annotated[Optional[StrictStr], Field(description="The requestId of the API call which led to the change.")] = None,
        changed_by: Annotated[Optional[StrictStr], Field(description="UserId of the user which led to the change.")] = None,
        start_date: Annotated[Optional[date], Field(description="Start of search time range.")] = None,
        end_date: Annotated[Optional[date], Field(description="End of search time range.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List history about your assignments (audit)

        List and filters the history about your assignments.

        :param x_request_id: [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. (required)
        :type x_request_id: str
        :param x_trace_id: Identifier to trace group of requests.
        :type x_trace_id: str
        :param page: Number of page to be fetched.
        :type page: int
        :param size: Number of elements per page.
        :type size: int
        :param order_by: Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`.
        :type order_by: List[str]
        :param tag_id: The identifier of the tag.
        :type tag_id: int
        :param request_id: The requestId of the API call which led to the change.
        :type request_id: str
        :param changed_by: UserId of the user which led to the change.
        :type changed_by: str
        :param start_date: Start of search time range.
        :type start_date: date
        :param end_date: End of search time range.
        :type end_date: date
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._retrieve_tag_audits_list_serialize(
            x_request_id=x_request_id,
            x_trace_id=x_trace_id,
            page=page,
            size=size,
            order_by=order_by,
            tag_id=tag_id,
            request_id=request_id,
            changed_by=changed_by,
            start_date=start_date,
            end_date=end_date,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListTagAuditsResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _retrieve_tag_audits_list_serialize(
        self,
        x_request_id,
        x_trace_id,
        page,
        size,
        order_by,
        tag_id,
        request_id,
        changed_by,
        start_date,
        end_date,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'orderBy': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if page is not None:
            
            _query_params.append(('page', page))
            
        if size is not None:
            
            _query_params.append(('size', size))
            
        if order_by is not None:
            
            _query_params.append(('orderBy', order_by))
            
        if tag_id is not None:
            
            _query_params.append(('tagId', tag_id))
            
        if request_id is not None:
            
            _query_params.append(('requestId', request_id))
            
        if changed_by is not None:
            
            _query_params.append(('changedBy', changed_by))
            
        if start_date is not None:
            if isinstance(start_date, date):
                _query_params.append(
                    (
                        'startDate',
                        start_date.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('startDate', start_date))
            
        if end_date is not None:
            if isinstance(end_date, date):
                _query_params.append(
                    (
                        'endDate',
                        end_date.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('endDate', end_date))
            
        # process the header parameters
        if x_request_id is not None:
            _header_params['x-request-id'] = x_request_id
        if x_trace_id is not None:
            _header_params['x-trace-id'] = x_trace_id
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'bearer'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1/tags/audits',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


