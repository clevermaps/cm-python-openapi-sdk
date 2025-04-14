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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class DwhOverlapsResponseContentInnerResultsInner(BaseModel):
    """
    DwhOverlapsResponseContentInnerResultsInner
    """ # noqa: E501
    operator: Optional[StrictStr] = None
    objects: Optional[Annotated[List[Annotated[str, Field(min_length=1, strict=True)]], Field(min_length=1)]] = None
    value: Optional[Union[StrictFloat, StrictInt]] = None
    __properties: ClassVar[List[str]] = ["operator", "objects", "value"]

    @field_validator('operator')
    def operator_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['self', 'subtract', 'intersect', 'major_dominance', 'minor_dominance', 'equivalent_dominance']):
            raise ValueError("must be one of enum values ('self', 'subtract', 'intersect', 'major_dominance', 'minor_dominance', 'equivalent_dominance')")
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
        """Create an instance of DwhOverlapsResponseContentInnerResultsInner from a JSON string"""
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
        """Create an instance of DwhOverlapsResponseContentInnerResultsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "operator": obj.get("operator"),
            "objects": obj.get("objects"),
            "value": obj.get("value")
        })
        return _obj


