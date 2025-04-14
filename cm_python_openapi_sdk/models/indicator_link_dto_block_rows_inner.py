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
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from cm_python_openapi_sdk.models.categories_dto import CategoriesDTO
from cm_python_openapi_sdk.models.distribution_dto import DistributionDTO
from cm_python_openapi_sdk.models.ranking_dto import RankingDTO
from cm_python_openapi_sdk.models.time_series_dto import TimeSeriesDTO
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

INDICATORLINKDTOBLOCKROWSINNER_ONE_OF_SCHEMAS = ["CategoriesDTO", "DistributionDTO", "RankingDTO", "TimeSeriesDTO"]

class IndicatorLinkDTOBlockRowsInner(BaseModel):
    """
    IndicatorLinkDTOBlockRowsInner
    """
    # data type: CategoriesDTO
    oneof_schema_1_validator: Optional[CategoriesDTO] = None
    # data type: DistributionDTO
    oneof_schema_2_validator: Optional[DistributionDTO] = None
    # data type: RankingDTO
    oneof_schema_3_validator: Optional[RankingDTO] = None
    # data type: TimeSeriesDTO
    oneof_schema_4_validator: Optional[TimeSeriesDTO] = None
    actual_instance: Optional[Union[CategoriesDTO, DistributionDTO, RankingDTO, TimeSeriesDTO]] = None
    one_of_schemas: Set[str] = { "CategoriesDTO", "DistributionDTO", "RankingDTO", "TimeSeriesDTO" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = IndicatorLinkDTOBlockRowsInner.model_construct()
        error_messages = []
        match = 0
        # validate data type: CategoriesDTO
        if not isinstance(v, CategoriesDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CategoriesDTO`")
        else:
            match += 1
        # validate data type: DistributionDTO
        if not isinstance(v, DistributionDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DistributionDTO`")
        else:
            match += 1
        # validate data type: RankingDTO
        if not isinstance(v, RankingDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RankingDTO`")
        else:
            match += 1
        # validate data type: TimeSeriesDTO
        if not isinstance(v, TimeSeriesDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TimeSeriesDTO`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in IndicatorLinkDTOBlockRowsInner with oneOf schemas: CategoriesDTO, DistributionDTO, RankingDTO, TimeSeriesDTO. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in IndicatorLinkDTOBlockRowsInner with oneOf schemas: CategoriesDTO, DistributionDTO, RankingDTO, TimeSeriesDTO. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into CategoriesDTO
        try:
            instance.actual_instance = CategoriesDTO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DistributionDTO
        try:
            instance.actual_instance = DistributionDTO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RankingDTO
        try:
            instance.actual_instance = RankingDTO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TimeSeriesDTO
        try:
            instance.actual_instance = TimeSeriesDTO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into IndicatorLinkDTOBlockRowsInner with oneOf schemas: CategoriesDTO, DistributionDTO, RankingDTO, TimeSeriesDTO. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into IndicatorLinkDTOBlockRowsInner with oneOf schemas: CategoriesDTO, DistributionDTO, RankingDTO, TimeSeriesDTO. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], CategoriesDTO, DistributionDTO, RankingDTO, TimeSeriesDTO]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


