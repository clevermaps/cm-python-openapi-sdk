# coding: utf-8

"""
    clevermaps-client

    CleverMaps REST API provides access to location intelligence and geospatial analytics platform.  ### Main capabilities include: - Project and user access management - Multidimensional data model and metrics management - Data upload and exports - Ad-hoc analysis of geospatial data - Full text and geographic search - Configuration of CleverMaps Studio visualizations 

    The version of the OpenAPI document: 1.0.0
    Contact: support@clevermaps.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cm_python_openapi_sdk.models.isochrone_dto import IsochroneDTO
from typing import Optional, Set
from typing_extensions import Self

class MeasureDTO(BaseModel):
    """
    MeasureDTO
    """ # noqa: E501
    type: Optional[StrictStr] = None
    points: Optional[List[IsochroneDTO]] = None
    zones: Optional[List[IsochroneDTO]] = None
    __properties: ClassVar[List[str]] = ["type", "points", "zones"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['line', 'isoline']):
            raise ValueError("must be one of enum values ('line', 'isoline')")
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
        """Create an instance of MeasureDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in points (list)
        _items = []
        if self.points:
            for _item_points in self.points:
                if _item_points:
                    _items.append(_item_points.to_dict())
            _dict['points'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in zones (list)
        _items = []
        if self.zones:
            for _item_zones in self.zones:
                if _item_zones:
                    _items.append(_item_zones.to_dict())
            _dict['zones'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MeasureDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "points": [IsochroneDTO.from_dict(_item) for _item in obj["points"]] if obj.get("points") is not None else None,
            "zones": [IsochroneDTO.from_dict(_item) for _item in obj["zones"]] if obj.get("zones") is not None else None
        })
        return _obj


