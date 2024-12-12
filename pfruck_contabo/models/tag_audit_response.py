# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class TagAuditResponse(BaseModel):
    """
    TagAuditResponse
    """ # noqa: E501
    tenant_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Your customer tenant id", alias="tenantId")
    customer_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Your customer number", alias="customerId")
    id: Union[StrictFloat, StrictInt] = Field(description="The identifier of the audit entry.")
    tag_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="The identifier of the audit entry.", alias="tagId")
    action: StrictStr = Field(description="Type of the action.")
    timestamp: datetime = Field(description="When the change took place.")
    changed_by: Annotated[str, Field(min_length=1, strict=True)] = Field(description="User ID", alias="changedBy")
    username: StrictStr = Field(description="Name of the user which led to the change.")
    request_id: StrictStr = Field(description="The requestId of the API call which led to the change.", alias="requestId")
    trace_id: StrictStr = Field(description="The traceId of the API call which led to the change.", alias="traceId")
    changes: Optional[Dict[str, Any]] = Field(default=None, description="List of actual changes.")
    __properties: ClassVar[List[str]] = ["tenantId", "customerId", "id", "tagId", "action", "timestamp", "changedBy", "username", "requestId", "traceId", "changes"]

    @field_validator('action')
    def action_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['CREATED', 'DELETED', 'UPDATED']):
            raise ValueError("must be one of enum values ('CREATED', 'DELETED', 'UPDATED')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TagAuditResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TagAuditResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenantId": obj.get("tenantId"),
            "customerId": obj.get("customerId"),
            "id": obj.get("id"),
            "tagId": obj.get("tagId"),
            "action": obj.get("action"),
            "timestamp": obj.get("timestamp"),
            "changedBy": obj.get("changedBy"),
            "username": obj.get("username"),
            "requestId": obj.get("requestId"),
            "traceId": obj.get("traceId"),
            "changes": obj.get("changes")
        })
        return _obj

