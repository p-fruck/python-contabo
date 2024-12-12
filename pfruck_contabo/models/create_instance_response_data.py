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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from pfruck_contabo.models.add_on_response import AddOnResponse
from pfruck_contabo.models.instance_status import InstanceStatus
from typing import Optional, Set
from typing_extensions import Self

class CreateInstanceResponseData(BaseModel):
    """
    CreateInstanceResponseData
    """ # noqa: E501
    tenant_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Your customer tenant id", alias="tenantId")
    customer_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Your customer number", alias="customerId")
    instance_id: StrictInt = Field(description="Instance's id", alias="instanceId")
    created_date: datetime = Field(description="Creation date for instance", alias="createdDate")
    image_id: StrictStr = Field(description="Image's id", alias="imageId")
    product_id: StrictStr = Field(description="Product ID", alias="productId")
    region: StrictStr = Field(description="Instance Region where the compute instance should be located.")
    add_ons: List[AddOnResponse] = Field(alias="addOns")
    os_type: StrictStr = Field(description="Type of operating system (OS)", alias="osType")
    status: InstanceStatus
    ssh_keys: List[StrictInt] = Field(description="Array of `secretId`s of public SSH keys for logging into as `defaultUser` with administrator/root privileges. Applies to Linux/BSD systems. Please refer to Secrets Management API.", alias="sshKeys")
    __properties: ClassVar[List[str]] = ["tenantId", "customerId", "instanceId", "createdDate", "imageId", "productId", "region", "addOns", "osType", "status", "sshKeys"]

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
        """Create an instance of CreateInstanceResponseData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in add_ons (list)
        _items = []
        if self.add_ons:
            for _item in self.add_ons:
                if _item:
                    _items.append(_item.to_dict())
            _dict['addOns'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateInstanceResponseData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenantId": obj.get("tenantId"),
            "customerId": obj.get("customerId"),
            "instanceId": obj.get("instanceId"),
            "createdDate": obj.get("createdDate"),
            "imageId": obj.get("imageId"),
            "productId": obj.get("productId"),
            "region": obj.get("region"),
            "addOns": [AddOnResponse.from_dict(_item) for _item in obj["addOns"]] if obj.get("addOns") is not None else None,
            "osType": obj.get("osType"),
            "status": obj.get("status"),
            "sshKeys": obj.get("sshKeys")
        })
        return _obj

