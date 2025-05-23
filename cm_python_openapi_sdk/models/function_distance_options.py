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

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from cm_python_openapi_sdk.models.central_point import CentralPoint
from typing import Optional, Set
from typing_extensions import Self

class FunctionDistanceOptions(BaseModel):
    """
    FunctionDistanceOptions
    """ # noqa: E501
    dataset: Annotated[str, Field(strict=True)]
    central_point: CentralPoint = Field(alias="centralPoint")
    __properties: ClassVar[List[str]] = ["dataset", "centralPoint"]

    @field_validator('dataset')
    def dataset_validate_regular_expression(cls, value):
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
        """Create an instance of FunctionDistanceOptions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of central_point
        if self.central_point:
            _dict['centralPoint'] = self.central_point.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FunctionDistanceOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dataset": obj.get("dataset"),
            "centralPoint": CentralPoint.from_dict(obj["centralPoint"]) if obj.get("centralPoint") is not None else None
        })
        return _obj


