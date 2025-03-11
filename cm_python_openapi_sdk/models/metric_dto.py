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
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from cm_python_openapi_sdk.models.dwh_query_function_types import DwhQueryFunctionTypes
from typing import Optional, Set
from typing_extensions import Self

class MetricDTO(BaseModel):
    """
    MetricDTO
    """ # noqa: E501
    id: Optional[StrictStr] = None
    name: Annotated[str, Field(min_length=1, strict=True, max_length=50)]
    type: Optional[StrictStr] = None
    title: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = None
    description: Optional[Annotated[str, Field(strict=True, max_length=2000)]] = None
    content: DwhQueryFunctionTypes
    __properties: ClassVar[List[str]] = ["id", "name", "type", "title", "description", "content"]

    @field_validator('name')
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-z][a-z0-9_-]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-z][a-z0-9_-]*$/")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['dataset', 'view', 'dashboard', 'indicatorDrill', 'indicator', 'metric', 'marker', 'markerSelector', 'export', 'dataPermission', 'projectSettings', 'share', 'map', 'attributeStyle']):
            raise ValueError("must be one of enum values ('dataset', 'view', 'dashboard', 'indicatorDrill', 'indicator', 'metric', 'marker', 'markerSelector', 'export', 'dataPermission', 'projectSettings', 'share', 'map', 'attributeStyle')")
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
        """Create an instance of MetricDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of content
        if self.content:
            _dict['content'] = self.content.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MetricDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "type": obj.get("type"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "content": DwhQueryFunctionTypes.from_dict(obj["content"]) if obj.get("content") is not None else None
        })
        return _obj


