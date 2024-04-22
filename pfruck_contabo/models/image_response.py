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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ImageResponse(BaseModel):
    """
    ImageResponse
    """ # noqa: E501
    image_id: StrictStr = Field(description="Image's id", alias="imageId")
    tenant_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Your customer tenant id", alias="tenantId")
    customer_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Customer ID", alias="customerId")
    name: StrictStr = Field(description="Image Name")
    description: StrictStr = Field(description="Image Description")
    url: StrictStr = Field(description="URL from where the image has been downloaded / provided.")
    size_mb: Union[StrictFloat, StrictInt] = Field(description="Image Size in MB", alias="sizeMb")
    uploaded_size_mb: Union[StrictFloat, StrictInt] = Field(description="Image Uploaded Size in MB", alias="uploadedSizeMb")
    os_type: StrictStr = Field(description="Type of operating system (OS)", alias="osType")
    version: StrictStr = Field(description="Version number to distinguish the contents of an image. Could be the version of the operating system for example.")
    format: StrictStr = Field(description="Image format")
    status: StrictStr = Field(description="Image status (e.g. if image is still downloading)")
    error_message: StrictStr = Field(description="Image download error message", alias="errorMessage")
    standard_image: StrictBool = Field(description="Flag indicating that image is either a standard (true) or a custom image (false)", alias="standardImage")
    creation_date: datetime = Field(description="The creation date time for the image", alias="creationDate")
    last_modified_date: datetime = Field(description="The last modified date time for the image", alias="lastModifiedDate")
    __properties: ClassVar[List[str]] = ["imageId", "tenantId", "customerId", "name", "description", "url", "sizeMb", "uploadedSizeMb", "osType", "version", "format", "status", "errorMessage", "standardImage", "creationDate", "lastModifiedDate"]

    @field_validator('tenant_id')
    def tenant_id_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['DE', 'INT']):
            raise ValueError("must be one of enum values ('DE', 'INT')")
        return value

    @field_validator('format')
    def format_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['iso', 'qcow2']):
            raise ValueError("must be one of enum values ('iso', 'qcow2')")
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
        """Create an instance of ImageResponse from a JSON string"""
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
        """Create an instance of ImageResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "imageId": obj.get("imageId"),
            "tenantId": obj.get("tenantId"),
            "customerId": obj.get("customerId"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "url": obj.get("url"),
            "sizeMb": obj.get("sizeMb"),
            "uploadedSizeMb": obj.get("uploadedSizeMb"),
            "osType": obj.get("osType"),
            "version": obj.get("version"),
            "format": obj.get("format"),
            "status": obj.get("status"),
            "errorMessage": obj.get("errorMessage"),
            "standardImage": obj.get("standardImage"),
            "creationDate": obj.get("creationDate"),
            "lastModifiedDate": obj.get("lastModifiedDate")
        })
        return _obj


