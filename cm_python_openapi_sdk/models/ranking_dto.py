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
from typing import Optional, Set
from typing_extensions import Self

class RankingDTO(BaseModel):
    """
    RankingDTO
    """ # noqa: E501
    type: StrictStr
    title: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    indicator: Optional[Annotated[str, Field(strict=True)]] = None
    default_layer: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="defaultLayer")
    feature_type: Optional[StrictStr] = Field(default=None, alias="featureType")
    direction: Optional[StrictStr] = None
    collapsed: Optional[StrictBool] = None
    visualized: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["type", "title", "indicator", "defaultLayer", "featureType", "direction", "collapsed", "visualized"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['ranking']):
            raise ValueError("must be one of enum values ('ranking')")
        return value

    @field_validator('indicator')
    def indicator_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\/rest\/projects\/(\$projectId|[a-z0-9]{16})\/md\/indicators(\?name=[a-z0-9_-]+|\/[a-z0-9]+)$", value):
            raise ValueError(r"must validate the regular expression /^\/rest\/projects\/(\$projectId|[a-z0-9]{16})\/md\/indicators(\?name=[a-z0-9_-]+|\/[a-z0-9]+)$/")
        return value

    @field_validator('default_layer')
    def default_layer_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-z][a-z0-9_-]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-z][a-z0-9_-]*$/")
        return value

    @field_validator('feature_type')
    def feature_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['granularity', 'markers']):
            raise ValueError("must be one of enum values ('granularity', 'markers')")
        return value

    @field_validator('direction')
    def direction_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['asc', 'desc']):
            raise ValueError("must be one of enum values ('asc', 'desc')")
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
        """Create an instance of RankingDTO from a JSON string"""
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
        """Create an instance of RankingDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "title": obj.get("title"),
            "indicator": obj.get("indicator"),
            "defaultLayer": obj.get("defaultLayer"),
            "featureType": obj.get("featureType"),
            "direction": obj.get("direction"),
            "collapsed": obj.get("collapsed"),
            "visualized": obj.get("visualized")
        })
        return _obj


