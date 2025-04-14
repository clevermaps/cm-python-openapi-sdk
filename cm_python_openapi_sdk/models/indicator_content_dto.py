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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from cm_python_openapi_sdk.models.format_dto import FormatDTO
from cm_python_openapi_sdk.models.indicator_visualizations_dto import IndicatorVisualizationsDTO
from cm_python_openapi_sdk.models.relations_dto import RelationsDTO
from cm_python_openapi_sdk.models.scale_options_dto import ScaleOptionsDTO
from typing import Optional, Set
from typing_extensions import Self

class IndicatorContentDTO(BaseModel):
    """
    IndicatorContentDTO
    """ # noqa: E501
    metric: Annotated[str, Field(strict=True)]
    scale: Optional[StrictStr] = 'standard'
    distribution: Optional[StrictStr] = 'geometric'
    visualizations: Optional[IndicatorVisualizationsDTO] = None
    format: Optional[FormatDTO] = None
    relations: Optional[RelationsDTO] = None
    scale_options: Optional[ScaleOptionsDTO] = Field(default=None, alias="scaleOptions")
    __properties: ClassVar[List[str]] = ["metric", "scale", "distribution", "visualizations", "format", "relations", "scaleOptions"]

    @field_validator('metric')
    def metric_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\/rest\/projects\/(\$projectId|[a-z0-9]{16})\/md\/metrics(\?name=[a-z0-9_-]+|\/[a-z0-9]+)$", value):
            raise ValueError(r"must validate the regular expression /^\/rest\/projects\/(\$projectId|[a-z0-9]{16})\/md\/metrics(\?name=[a-z0-9_-]+|\/[a-z0-9]+)$/")
        return value

    @field_validator('scale')
    def scale_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['standard', 'positive', 'negative', 'binaryStandard', 'binaryNegative', 'divergingStandard', 'divergingNegative', 'inverse', 'traffic', 'trafficInverse', 'heatmap', 'magma', 'heat', 'viridis', 'divergingWithZeroStandard', 'divergingWithZeroNegative']):
            raise ValueError("must be one of enum values ('standard', 'positive', 'negative', 'binaryStandard', 'binaryNegative', 'divergingStandard', 'divergingNegative', 'inverse', 'traffic', 'trafficInverse', 'heatmap', 'magma', 'heat', 'viridis', 'divergingWithZeroStandard', 'divergingWithZeroNegative')")
        return value

    @field_validator('distribution')
    def distribution_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['geometric', 'uniform']):
            raise ValueError("must be one of enum values ('geometric', 'uniform')")
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
        """Create an instance of IndicatorContentDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of visualizations
        if self.visualizations:
            _dict['visualizations'] = self.visualizations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of format
        if self.format:
            _dict['format'] = self.format.to_dict()
        # override the default output from pydantic by calling `to_dict()` of relations
        if self.relations:
            _dict['relations'] = self.relations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of scale_options
        if self.scale_options:
            _dict['scaleOptions'] = self.scale_options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IndicatorContentDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "metric": obj.get("metric"),
            "scale": obj.get("scale") if obj.get("scale") is not None else 'standard',
            "distribution": obj.get("distribution") if obj.get("distribution") is not None else 'geometric',
            "visualizations": IndicatorVisualizationsDTO.from_dict(obj["visualizations"]) if obj.get("visualizations") is not None else None,
            "format": FormatDTO.from_dict(obj["format"]) if obj.get("format") is not None else None,
            "relations": RelationsDTO.from_dict(obj["relations"]) if obj.get("relations") is not None else None,
            "scaleOptions": ScaleOptionsDTO.from_dict(obj["scaleOptions"]) if obj.get("scaleOptions") is not None else None
        })
        return _obj


