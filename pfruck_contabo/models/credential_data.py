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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class CredentialData(BaseModel):
    """
    CredentialData
    """ # noqa: E501
    tenant_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Your customer tenant id", alias="tenantId")
    customer_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Your customer number", alias="customerId")
    access_key: StrictStr = Field(description="Access key ID.", alias="accessKey")
    secret_key: StrictStr = Field(description="Secret key ID.", alias="secretKey")
    object_storage_id: StrictStr = Field(description="Object Storage ID.", alias="objectStorageId")
    display_name: StrictStr = Field(description="Object Storage Name.", alias="displayName")
    region: StrictStr = Field(description="Object Storage Region.")
    credential_id: Union[StrictFloat, StrictInt] = Field(description="Object Storage Credential ID", alias="credentialId")
    __properties: ClassVar[List[str]] = ["tenantId", "customerId", "accessKey", "secretKey", "objectStorageId", "displayName", "region", "credentialId"]

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
        """Create an instance of CredentialData from a JSON string"""
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
        """Create an instance of CredentialData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenantId": obj.get("tenantId"),
            "customerId": obj.get("customerId"),
            "accessKey": obj.get("accessKey"),
            "secretKey": obj.get("secretKey"),
            "objectStorageId": obj.get("objectStorageId"),
            "displayName": obj.get("displayName"),
            "region": obj.get("region"),
            "credentialId": obj.get("credentialId")
        })
        return _obj


