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
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from pfruck_contabo.models.add_on_response import AddOnResponse
from pfruck_contabo.models.additional_ip import AdditionalIp
from pfruck_contabo.models.instance_status import InstanceStatus
from pfruck_contabo.models.ip_config import IpConfig
from typing import Optional, Set
from typing_extensions import Self

class InstanceResponse(BaseModel):
    """
    InstanceResponse
    """ # noqa: E501
    tenant_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Your customer tenant id", alias="tenantId")
    customer_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Customer ID", alias="customerId")
    additional_ips: List[AdditionalIp] = Field(alias="additionalIps")
    name: StrictStr = Field(description="Instance Name")
    display_name: StrictStr = Field(description="Instance display name", alias="displayName")
    instance_id: StrictInt = Field(description="Instance ID", alias="instanceId")
    data_center: StrictStr = Field(description="The data center where your Private Network is located", alias="dataCenter")
    region: StrictStr = Field(description="Instance region where the compute instance should be located.")
    region_name: StrictStr = Field(description="The name of the region where the instance is located.", alias="regionName")
    product_id: StrictStr = Field(description="Product ID", alias="productId")
    image_id: StrictStr = Field(description="Image's id", alias="imageId")
    ip_config: IpConfig = Field(alias="ipConfig")
    mac_address: StrictStr = Field(description="MAC Address", alias="macAddress")
    ram_mb: Union[StrictFloat, StrictInt] = Field(description="Image RAM size in MB", alias="ramMb")
    cpu_cores: StrictInt = Field(description="CPU core count", alias="cpuCores")
    os_type: StrictStr = Field(description="Type of operating system (OS)", alias="osType")
    disk_mb: Union[StrictFloat, StrictInt] = Field(description="Image Disk size in MB", alias="diskMb")
    ssh_keys: List[StrictInt] = Field(description="Array of `secretId`s of public SSH keys for logging into as `defaultUser` with administrator/root privileges. Applies to Linux/BSD systems. Please refer to Secrets Management API.", alias="sshKeys")
    created_date: datetime = Field(description="The creation date for the instance", alias="createdDate")
    cancel_date: date = Field(description="The date on which the instance will be cancelled", alias="cancelDate")
    status: InstanceStatus
    v_host_id: StrictInt = Field(description="ID of host system", alias="vHostId")
    v_host_number: StrictInt = Field(description="Number of host system", alias="vHostNumber")
    v_host_name: StrictStr = Field(description="Name of host system", alias="vHostName")
    add_ons: List[AddOnResponse] = Field(alias="addOns")
    error_message: Optional[StrictStr] = Field(default=None, description="Message in case of an error.", alias="errorMessage")
    product_type: StrictStr = Field(description="Instance's category depending on Product Id", alias="productType")
    product_name: StrictStr = Field(description="Instance's Product Name", alias="productName")
    default_user: Optional[StrictStr] = Field(default=None, description="Default user name created for login during (re-)installation with administrative privileges. Allowed values for Linux/BSD are `admin` (use sudo to apply administrative privileges like root) or `root`. Allowed values for Windows are `admin` (has administrative privileges like administrator) or `administrator`.", alias="defaultUser")
    __properties: ClassVar[List[str]] = ["tenantId", "customerId", "additionalIps", "name", "displayName", "instanceId", "dataCenter", "region", "regionName", "productId", "imageId", "ipConfig", "macAddress", "ramMb", "cpuCores", "osType", "diskMb", "sshKeys", "createdDate", "cancelDate", "status", "vHostId", "vHostNumber", "vHostName", "addOns", "errorMessage", "productType", "productName", "defaultUser"]

    @field_validator('tenant_id')
    def tenant_id_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['DE', 'INT']):
            raise ValueError("must be one of enum values ('DE', 'INT')")
        return value

    @field_validator('cancel_date')
    def cancel_date_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"yyyy-mm-dd", value):
            raise ValueError(r"must validate the regular expression /yyyy-mm-dd/")
        return value

    @field_validator('product_type')
    def product_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['hdd', 'ssd', 'vds', 'nvme']):
            raise ValueError("must be one of enum values ('hdd', 'ssd', 'vds', 'nvme')")
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
        """Create an instance of InstanceResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in additional_ips (list)
        _items = []
        if self.additional_ips:
            for _item in self.additional_ips:
                if _item:
                    _items.append(_item.to_dict())
            _dict['additionalIps'] = _items
        # override the default output from pydantic by calling `to_dict()` of ip_config
        if self.ip_config:
            _dict['ipConfig'] = self.ip_config.to_dict()
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
        """Create an instance of InstanceResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenantId": obj.get("tenantId"),
            "customerId": obj.get("customerId"),
            "additionalIps": [AdditionalIp.from_dict(_item) for _item in obj["additionalIps"]] if obj.get("additionalIps") is not None else None,
            "name": obj.get("name"),
            "displayName": obj.get("displayName"),
            "instanceId": obj.get("instanceId"),
            "dataCenter": obj.get("dataCenter"),
            "region": obj.get("region"),
            "regionName": obj.get("regionName"),
            "productId": obj.get("productId"),
            "imageId": obj.get("imageId"),
            "ipConfig": IpConfig.from_dict(obj["ipConfig"]) if obj.get("ipConfig") is not None else None,
            "macAddress": obj.get("macAddress"),
            "ramMb": obj.get("ramMb"),
            "cpuCores": obj.get("cpuCores"),
            "osType": obj.get("osType"),
            "diskMb": obj.get("diskMb"),
            "sshKeys": obj.get("sshKeys"),
            "createdDate": obj.get("createdDate"),
            "cancelDate": obj.get("cancelDate"),
            "status": obj.get("status"),
            "vHostId": obj.get("vHostId"),
            "vHostNumber": obj.get("vHostNumber"),
            "vHostName": obj.get("vHostName"),
            "addOns": [AddOnResponse.from_dict(_item) for _item in obj["addOns"]] if obj.get("addOns") is not None else None,
            "errorMessage": obj.get("errorMessage"),
            "productType": obj.get("productType"),
            "productName": obj.get("productName"),
            "defaultUser": obj.get("defaultUser")
        })
        return _obj


