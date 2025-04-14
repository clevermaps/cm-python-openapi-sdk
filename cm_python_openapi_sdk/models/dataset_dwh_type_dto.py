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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from cm_python_openapi_sdk.models.dataset_visualization_dto import DatasetVisualizationDTO
from cm_python_openapi_sdk.models.dwh_abstract_property import DwhAbstractProperty
from cm_python_openapi_sdk.models.zoom_dto import ZoomDTO
from typing import Optional, Set
from typing_extensions import Self

class DatasetDwhTypeDTO(BaseModel):
    """
    DatasetDwhTypeDTO
    """ # noqa: E501
    type: StrictStr
    subtype: StrictStr
    geometry: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    h3_geometries: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, alias="h3Geometries")
    visualizations: Optional[List[DatasetVisualizationDTO]] = None
    table: Optional[Annotated[str, Field(strict=True)]] = None
    geometry_table: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="geometryTable")
    primary_key: Annotated[str, Field(strict=True)] = Field(alias="primaryKey")
    categorizable: Optional[StrictBool] = True
    full_text_index: Optional[StrictBool] = Field(default=None, alias="fullTextIndex")
    spatial_index: Optional[StrictBool] = Field(default=None, alias="spatialIndex")
    properties: Annotated[List[DwhAbstractProperty], Field(min_length=1)]
    zoom: Optional[ZoomDTO] = None
    __properties: ClassVar[List[str]] = ["type", "subtype", "geometry", "h3Geometries", "visualizations", "table", "geometryTable", "primaryKey", "categorizable", "fullTextIndex", "spatialIndex", "properties", "zoom"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['dwh']):
            raise ValueError("must be one of enum values ('dwh')")
        return value

    @field_validator('subtype')
    def subtype_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['geometryPolygon', 'geometryPoint', 'geometryLine', 'basic', 'date']):
            raise ValueError("must be one of enum values ('geometryPolygon', 'geometryPoint', 'geometryLine', 'basic', 'date')")
        return value

    @field_validator('table')
    def table_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-z][a-z0-9_-]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-z][a-z0-9_-]*$/")
        return value

    @field_validator('geometry_table')
    def geometry_table_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-z][a-z0-9_-]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-z][a-z0-9_-]*$/")
        return value

    @field_validator('primary_key')
    def primary_key_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-z][a-z0-9_-]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-z][a-z0-9_-]*$/")
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
        """Create an instance of DatasetDwhTypeDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in visualizations (list)
        _items = []
        if self.visualizations:
            for _item_visualizations in self.visualizations:
                if _item_visualizations:
                    _items.append(_item_visualizations.to_dict())
            _dict['visualizations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in properties (list)
        _items = []
        if self.properties:
            for _item_properties in self.properties:
                if _item_properties:
                    _items.append(_item_properties.to_dict())
            _dict['properties'] = _items
        # override the default output from pydantic by calling `to_dict()` of zoom
        if self.zoom:
            _dict['zoom'] = self.zoom.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DatasetDwhTypeDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "subtype": obj.get("subtype"),
            "geometry": obj.get("geometry"),
            "h3Geometries": obj.get("h3Geometries"),
            "visualizations": [DatasetVisualizationDTO.from_dict(_item) for _item in obj["visualizations"]] if obj.get("visualizations") is not None else None,
            "table": obj.get("table"),
            "geometryTable": obj.get("geometryTable"),
            "primaryKey": obj.get("primaryKey"),
            "categorizable": obj.get("categorizable") if obj.get("categorizable") is not None else True,
            "fullTextIndex": obj.get("fullTextIndex"),
            "spatialIndex": obj.get("spatialIndex"),
            "properties": [DwhAbstractProperty.from_dict(_item) for _item in obj["properties"]] if obj.get("properties") is not None else None,
            "zoom": ZoomDTO.from_dict(obj["zoom"]) if obj.get("zoom") is not None else None
        })
        return _obj


