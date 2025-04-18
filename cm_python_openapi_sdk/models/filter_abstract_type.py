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
from cm_python_openapi_sdk.models.date_filter_dto import DateFilterDTO
from cm_python_openapi_sdk.models.feature_filter_dto import FeatureFilterDTO
from cm_python_openapi_sdk.models.global_date_filter_dto import GlobalDateFilterDTO
from cm_python_openapi_sdk.models.histogram_filter_dto import HistogramFilterDTO
from cm_python_openapi_sdk.models.indicator_filter_dto import IndicatorFilterDTO
from cm_python_openapi_sdk.models.multi_select_filter_dto import MultiSelectFilterDTO
from cm_python_openapi_sdk.models.single_select_filter_dto import SingleSelectFilterDTO
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

FILTERABSTRACTTYPE_ONE_OF_SCHEMAS = ["DateFilterDTO", "FeatureFilterDTO", "GlobalDateFilterDTO", "HistogramFilterDTO", "IndicatorFilterDTO", "MultiSelectFilterDTO", "SingleSelectFilterDTO"]

class FilterAbstractType(BaseModel):
    """
    FilterAbstractType
    """
    # data type: DateFilterDTO
    oneof_schema_1_validator: Optional[DateFilterDTO] = None
    # data type: GlobalDateFilterDTO
    oneof_schema_2_validator: Optional[GlobalDateFilterDTO] = None
    # data type: HistogramFilterDTO
    oneof_schema_3_validator: Optional[HistogramFilterDTO] = None
    # data type: MultiSelectFilterDTO
    oneof_schema_4_validator: Optional[MultiSelectFilterDTO] = None
    # data type: IndicatorFilterDTO
    oneof_schema_5_validator: Optional[IndicatorFilterDTO] = None
    # data type: FeatureFilterDTO
    oneof_schema_6_validator: Optional[FeatureFilterDTO] = None
    # data type: SingleSelectFilterDTO
    oneof_schema_7_validator: Optional[SingleSelectFilterDTO] = None
    actual_instance: Optional[Union[DateFilterDTO, FeatureFilterDTO, GlobalDateFilterDTO, HistogramFilterDTO, IndicatorFilterDTO, MultiSelectFilterDTO, SingleSelectFilterDTO]] = None
    one_of_schemas: Set[str] = { "DateFilterDTO", "FeatureFilterDTO", "GlobalDateFilterDTO", "HistogramFilterDTO", "IndicatorFilterDTO", "MultiSelectFilterDTO", "SingleSelectFilterDTO" }

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
        instance = FilterAbstractType.model_construct()
        error_messages = []
        match = 0
        # validate data type: DateFilterDTO
        if not isinstance(v, DateFilterDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DateFilterDTO`")
        else:
            match += 1
        # validate data type: GlobalDateFilterDTO
        if not isinstance(v, GlobalDateFilterDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GlobalDateFilterDTO`")
        else:
            match += 1
        # validate data type: HistogramFilterDTO
        if not isinstance(v, HistogramFilterDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `HistogramFilterDTO`")
        else:
            match += 1
        # validate data type: MultiSelectFilterDTO
        if not isinstance(v, MultiSelectFilterDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MultiSelectFilterDTO`")
        else:
            match += 1
        # validate data type: IndicatorFilterDTO
        if not isinstance(v, IndicatorFilterDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IndicatorFilterDTO`")
        else:
            match += 1
        # validate data type: FeatureFilterDTO
        if not isinstance(v, FeatureFilterDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FeatureFilterDTO`")
        else:
            match += 1
        # validate data type: SingleSelectFilterDTO
        if not isinstance(v, SingleSelectFilterDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SingleSelectFilterDTO`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in FilterAbstractType with oneOf schemas: DateFilterDTO, FeatureFilterDTO, GlobalDateFilterDTO, HistogramFilterDTO, IndicatorFilterDTO, MultiSelectFilterDTO, SingleSelectFilterDTO. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in FilterAbstractType with oneOf schemas: DateFilterDTO, FeatureFilterDTO, GlobalDateFilterDTO, HistogramFilterDTO, IndicatorFilterDTO, MultiSelectFilterDTO, SingleSelectFilterDTO. Details: " + ", ".join(error_messages))
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

        # deserialize data into DateFilterDTO
        try:
            instance.actual_instance = DateFilterDTO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GlobalDateFilterDTO
        try:
            instance.actual_instance = GlobalDateFilterDTO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into HistogramFilterDTO
        try:
            instance.actual_instance = HistogramFilterDTO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into MultiSelectFilterDTO
        try:
            instance.actual_instance = MultiSelectFilterDTO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IndicatorFilterDTO
        try:
            instance.actual_instance = IndicatorFilterDTO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into FeatureFilterDTO
        try:
            instance.actual_instance = FeatureFilterDTO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SingleSelectFilterDTO
        try:
            instance.actual_instance = SingleSelectFilterDTO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into FilterAbstractType with oneOf schemas: DateFilterDTO, FeatureFilterDTO, GlobalDateFilterDTO, HistogramFilterDTO, IndicatorFilterDTO, MultiSelectFilterDTO, SingleSelectFilterDTO. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into FilterAbstractType with oneOf schemas: DateFilterDTO, FeatureFilterDTO, GlobalDateFilterDTO, HistogramFilterDTO, IndicatorFilterDTO, MultiSelectFilterDTO, SingleSelectFilterDTO. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], DateFilterDTO, FeatureFilterDTO, GlobalDateFilterDTO, HistogramFilterDTO, IndicatorFilterDTO, MultiSelectFilterDTO, SingleSelectFilterDTO]]:
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


