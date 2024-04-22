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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from pfruck_contabo.models.create_instance_addons import CreateInstanceAddons
from typing import Optional, Set
from typing_extensions import Self

class CreateInstanceRequest(BaseModel):
    """
    CreateInstanceRequest
    """ # noqa: E501
    image_id: Optional[StrictStr] = Field(default='afecbb85-e2fc-46f0-9684-b46b1faf00bb', description="ImageId to be used to setup the compute instance. Default is Ubuntu 22.04", alias="imageId")
    product_id: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default='V45', description="Default is V45", alias="productId")
    region: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default='EU', description="Instance Region where the compute instance should be located. Default is EU")
    ssh_keys: Optional[List[StrictInt]] = Field(default=None, description="Array of `secretId`s of public SSH keys for logging into as `defaultUser` with administrator/root privileges. Applies to Linux/BSD systems. Please refer to Secrets Management API.", alias="sshKeys")
    root_password: Optional[StrictInt] = Field(default=None, description="`secretId` of the password for the `defaultUser` with administrator/root privileges. For Linux/BSD please use SSH, for Windows RDP. Please refer to Secrets Management API.", alias="rootPassword")
    user_data: Optional[StrictStr] = Field(default=None, description="[Cloud-Init](https://cloud-init.io/) Config in order to customize during start of compute instance.", alias="userData")
    license: Optional[StrictStr] = Field(default=None, description="Additional licence in order to enhance your chosen product, mainly needed for software licenses on your product (not needed for windows).")
    period: StrictInt = Field(description="Initial contract period in months. Available periods are: 1, 3, 6 and 12 months. Default to 1 month")
    display_name: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="The display name of the instance", alias="displayName")
    default_user: Optional[StrictStr] = Field(default='admin', description="Default user name created for login during (re-)installation with administrative privileges. Allowed values for Linux/BSD are `admin` (use sudo to apply administrative privileges like root) or `root`. Allowed values for Windows are `admin` (has administrative privileges like administrator) or `administrator`.", alias="defaultUser")
    add_ons: Optional[CreateInstanceAddons] = Field(default=None, description="Set attributes in the addons object for the corresponding ones that need to be added to the instance", alias="addOns")
    application_id: Optional[StrictStr] = Field(default=None, description="Application ID", alias="applicationId")
    __properties: ClassVar[List[str]] = ["imageId", "productId", "region", "sshKeys", "rootPassword", "userData", "license", "period", "displayName", "defaultUser", "addOns", "applicationId"]

    @field_validator('region')
    def region_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['EU', 'US-central', 'US-east', 'US-west', 'SIN', 'UK', 'AUS', 'JPN']):
            raise ValueError("must be one of enum values ('EU', 'US-central', 'US-east', 'US-west', 'SIN', 'UK', 'AUS', 'JPN')")
        return value

    @field_validator('license')
    def license_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['cPanel5', 'cPanel30', 'cPanel50', 'cPanel100', 'cPanel150', 'cPanel200', 'cPanel250', 'cPanel300', 'cPanel350', 'cPanel400', 'cPanel450', 'cPanel500', 'cPanel550', 'cPanel600', 'cPanel650', 'cPanel700', 'cPanel750', 'cPanel800', 'cPanel850', 'cPanel900', 'cPanel950', 'cPanel1000', 'PleskAdmin', 'PleskHost', 'PleskPro']):
            raise ValueError("must be one of enum values ('cPanel5', 'cPanel30', 'cPanel50', 'cPanel100', 'cPanel150', 'cPanel200', 'cPanel250', 'cPanel300', 'cPanel350', 'cPanel400', 'cPanel450', 'cPanel500', 'cPanel550', 'cPanel600', 'cPanel650', 'cPanel700', 'cPanel750', 'cPanel800', 'cPanel850', 'cPanel900', 'cPanel950', 'cPanel1000', 'PleskAdmin', 'PleskHost', 'PleskPro')")
        return value

    @field_validator('default_user')
    def default_user_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['root', 'admin', 'administrator']):
            raise ValueError("must be one of enum values ('root', 'admin', 'administrator')")
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
        """Create an instance of CreateInstanceRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of add_ons
        if self.add_ons:
            _dict['addOns'] = self.add_ons.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateInstanceRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "imageId": obj.get("imageId") if obj.get("imageId") is not None else 'afecbb85-e2fc-46f0-9684-b46b1faf00bb',
            "productId": obj.get("productId") if obj.get("productId") is not None else 'V45',
            "region": obj.get("region") if obj.get("region") is not None else 'EU',
            "sshKeys": obj.get("sshKeys"),
            "rootPassword": obj.get("rootPassword"),
            "userData": obj.get("userData"),
            "license": obj.get("license"),
            "period": obj.get("period") if obj.get("period") is not None else 1,
            "displayName": obj.get("displayName"),
            "defaultUser": obj.get("defaultUser") if obj.get("defaultUser") is not None else 'admin',
            "addOns": CreateInstanceAddons.from_dict(obj["addOns"]) if obj.get("addOns") is not None else None,
            "applicationId": obj.get("applicationId")
        })
        return _obj


