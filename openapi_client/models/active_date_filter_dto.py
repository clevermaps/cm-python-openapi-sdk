# coding: utf-8

"""
    clevermaps-client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from openapi_client.models.default_values_date_dto import DefaultValuesDateDTO
from typing import Optional, Set
from typing_extensions import Self

class ActiveDateFilterDTO(BaseModel):
    """
    ActiveDateFilterDTO
    """ # noqa: E501
    default_values: DefaultValuesDateDTO = Field(alias="defaultValues")
    type: StrictStr
    var_property: Annotated[str, Field(strict=True)] = Field(alias="property")
    __properties: ClassVar[List[str]] = ["defaultValues", "type", "property"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['date']):
            raise ValueError("must be one of enum values ('date')")
        return value

    @field_validator('var_property')
    def var_property_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-z][a-z0-9_-]*\.[a-z][a-z0-9_-]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-z][a-z0-9_-]*\.[a-z][a-z0-9_-]*$/")
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
        """Create an instance of ActiveDateFilterDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of default_values
        if self.default_values:
            _dict['defaultValues'] = self.default_values.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ActiveDateFilterDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "defaultValues": DefaultValuesDateDTO.from_dict(obj["defaultValues"]) if obj.get("defaultValues") is not None else None,
            "type": obj.get("type"),
            "property": obj.get("property")
        })
        return _obj


