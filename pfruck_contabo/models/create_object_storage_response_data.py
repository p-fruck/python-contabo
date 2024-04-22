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

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Union
from typing_extensions import Annotated
from pfruck_contabo.models.auto_scaling_type_response import AutoScalingTypeResponse
from typing import Optional, Set
from typing_extensions import Self

class CreateObjectStorageResponseData(BaseModel):
    """
    CreateObjectStorageResponseData
    """ # noqa: E501
    tenant_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Your customer tenant id", alias="tenantId")
    customer_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Your customer number", alias="customerId")
    object_storage_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Your object storage id", alias="objectStorageId")
    created_date: datetime = Field(description="Creation date for object storage.", alias="createdDate")
    cancel_date: date = Field(description="Cancellation date for object storage.", alias="cancelDate")
    auto_scaling: AutoScalingTypeResponse = Field(description="Autoscaling settings", alias="autoScaling")
    data_center: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The data center of the storage", alias="dataCenter")
    total_purchased_space_tb: Union[StrictFloat, StrictInt] = Field(description="Amount of purchased / requested object storage in TB.", alias="totalPurchasedSpaceTB")
    used_space_tb: Union[StrictFloat, StrictInt] = Field(description="Currently used space in TB.", alias="usedSpaceTB")
    used_space_percentage: Union[Annotated[float, Field(le=100, strict=True, ge=0)], Annotated[int, Field(le=100, strict=True, ge=0)]] = Field(description="Currently used space in percentage.", alias="usedSpacePercentage")
    s3_url: StrictStr = Field(description="S3 URL to connect to your S3 compatible object storage", alias="s3Url")
    s3_tenant_id: StrictStr = Field(description="Your S3 tenantId. Only required for public sharing.", alias="s3TenantId")
    status: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The object storage status")
    region: StrictStr = Field(description="The region where your object storage is located")
    display_name: Annotated[str, Field(min_length=1, strict=True, max_length=255)] = Field(description="Display name for object storage.", alias="displayName")
    __properties: ClassVar[List[str]] = ["tenantId", "customerId", "objectStorageId", "createdDate", "cancelDate", "autoScaling", "dataCenter", "totalPurchasedSpaceTB", "usedSpaceTB", "usedSpacePercentage", "s3Url", "s3TenantId", "status", "region", "displayName"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['READY', 'PROVISIONING', 'UPGRADING', 'CANCELLED', 'ERROR', 'ENABLED', 'DISABLED', 'MANUAL_PROVISIONING', 'PRODUCT_NOT_AVAILABLE', 'LIMIT_EXCEEDED', 'VERIFICATION_REQUIRED', 'COMPLETED', 'ORDER_PROCESSING', 'PENDING_PAYMENT', 'UNKNOWN']):
            raise ValueError("must be one of enum values ('READY', 'PROVISIONING', 'UPGRADING', 'CANCELLED', 'ERROR', 'ENABLED', 'DISABLED', 'MANUAL_PROVISIONING', 'PRODUCT_NOT_AVAILABLE', 'LIMIT_EXCEEDED', 'VERIFICATION_REQUIRED', 'COMPLETED', 'ORDER_PROCESSING', 'PENDING_PAYMENT', 'UNKNOWN')")
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
        """Create an instance of CreateObjectStorageResponseData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of auto_scaling
        if self.auto_scaling:
            _dict['autoScaling'] = self.auto_scaling.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateObjectStorageResponseData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenantId": obj.get("tenantId"),
            "customerId": obj.get("customerId"),
            "objectStorageId": obj.get("objectStorageId"),
            "createdDate": obj.get("createdDate"),
            "cancelDate": obj.get("cancelDate"),
            "autoScaling": AutoScalingTypeResponse.from_dict(obj["autoScaling"]) if obj.get("autoScaling") is not None else None,
            "dataCenter": obj.get("dataCenter"),
            "totalPurchasedSpaceTB": obj.get("totalPurchasedSpaceTB"),
            "usedSpaceTB": obj.get("usedSpaceTB"),
            "usedSpacePercentage": obj.get("usedSpacePercentage"),
            "s3Url": obj.get("s3Url"),
            "s3TenantId": obj.get("s3TenantId"),
            "status": obj.get("status"),
            "region": obj.get("region"),
            "displayName": obj.get("displayName")
        })
        return _obj


