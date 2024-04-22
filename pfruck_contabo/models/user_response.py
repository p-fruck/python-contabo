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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from pfruck_contabo.models.role_response import RoleResponse
from typing import Optional, Set
from typing_extensions import Self

class UserResponse(BaseModel):
    """
    UserResponse
    """ # noqa: E501
    tenant_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Your customer tenant id", alias="tenantId")
    customer_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Your customer number", alias="customerId")
    user_id: StrictStr = Field(description="The identifier of the user.", alias="userId")
    first_name: Annotated[str, Field(min_length=1, strict=True, max_length=255)] = Field(description="The first name of the user. Users may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per user.", alias="firstName")
    last_name: Annotated[str, Field(min_length=1, strict=True, max_length=255)] = Field(description="The last name of the user. Users may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per user.", alias="lastName")
    email: Annotated[str, Field(min_length=1, strict=True, max_length=255)] = Field(description="The email of the user to which activation and forgot password links are being sent to. There is a limit of 255 characters per email.")
    email_verified: StrictBool = Field(description="User email verification status.", alias="emailVerified")
    enabled: StrictBool = Field(description="If uses is not enabled, he can't login and thus use services any longer.")
    totp: StrictBool = Field(description="Enable or disable two-factor authentication (2FA) via time based OTP.")
    locale: StrictStr = Field(description="The locale of the user. This can be `de-DE`, `de`, `en-US`, `en`")
    roles: List[RoleResponse] = Field(description="The roles as list of `roleId`s of the user.")
    owner: StrictBool = Field(description="If user is owner he will have permissions to all API endpoints and resources. Enabling this will superseed all role definitions and `accessAllResources`.")
    __properties: ClassVar[List[str]] = ["tenantId", "customerId", "userId", "firstName", "lastName", "email", "emailVerified", "enabled", "totp", "locale", "roles", "owner"]

    @field_validator('locale')
    def locale_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['de-DE', 'de', 'en-US', 'en']):
            raise ValueError("must be one of enum values ('de-DE', 'de', 'en-US', 'en')")
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
        """Create an instance of UserResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in roles (list)
        _items = []
        if self.roles:
            for _item in self.roles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['roles'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenantId": obj.get("tenantId"),
            "customerId": obj.get("customerId"),
            "userId": obj.get("userId"),
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "email": obj.get("email"),
            "emailVerified": obj.get("emailVerified"),
            "enabled": obj.get("enabled"),
            "totp": obj.get("totp"),
            "locale": obj.get("locale"),
            "roles": [RoleResponse.from_dict(_item) for _item in obj["roles"]] if obj.get("roles") is not None else None,
            "owner": obj.get("owner")
        })
        return _obj


