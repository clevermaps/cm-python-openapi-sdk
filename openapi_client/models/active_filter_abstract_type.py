# coding: utf-8

"""
    clevermaps-client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from openapi_client.models.active_date_filter_dto import ActiveDateFilterDTO
from openapi_client.models.active_feature_filter_dto import ActiveFeatureFilterDTO
from openapi_client.models.active_global_date_filter_dto import ActiveGlobalDateFilterDTO
from openapi_client.models.active_histogram_filter_dto import ActiveHistogramFilterDTO
from openapi_client.models.active_indicator_filter_dto import ActiveIndicatorFilterDTO
from openapi_client.models.active_multi_select_filter_dto import ActiveMultiSelectFilterDTO
from openapi_client.models.active_single_select_filter_dto import ActiveSingleSelectFilterDTO
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

ACTIVEFILTERABSTRACTTYPE_ONE_OF_SCHEMAS = ["ActiveDateFilterDTO", "ActiveFeatureFilterDTO", "ActiveGlobalDateFilterDTO", "ActiveHistogramFilterDTO", "ActiveIndicatorFilterDTO", "ActiveMultiSelectFilterDTO", "ActiveSingleSelectFilterDTO"]

class ActiveFilterAbstractType(BaseModel):
    """
    ActiveFilterAbstractType
    """
    # data type: ActiveDateFilterDTO
    oneof_schema_1_validator: Optional[ActiveDateFilterDTO] = None
    # data type: ActiveGlobalDateFilterDTO
    oneof_schema_2_validator: Optional[ActiveGlobalDateFilterDTO] = None
    # data type: ActiveHistogramFilterDTO
    oneof_schema_3_validator: Optional[ActiveHistogramFilterDTO] = None
    # data type: ActiveMultiSelectFilterDTO
    oneof_schema_4_validator: Optional[ActiveMultiSelectFilterDTO] = None
    # data type: ActiveIndicatorFilterDTO
    oneof_schema_5_validator: Optional[ActiveIndicatorFilterDTO] = None
    # data type: ActiveFeatureFilterDTO
    oneof_schema_6_validator: Optional[ActiveFeatureFilterDTO] = None
    # data type: ActiveSingleSelectFilterDTO
    oneof_schema_7_validator: Optional[ActiveSingleSelectFilterDTO] = None
    actual_instance: Optional[Union[ActiveDateFilterDTO, ActiveFeatureFilterDTO, ActiveGlobalDateFilterDTO, ActiveHistogramFilterDTO, ActiveIndicatorFilterDTO, ActiveMultiSelectFilterDTO, ActiveSingleSelectFilterDTO]] = None
    one_of_schemas: Set[str] = { "ActiveDateFilterDTO", "ActiveFeatureFilterDTO", "ActiveGlobalDateFilterDTO", "ActiveHistogramFilterDTO", "ActiveIndicatorFilterDTO", "ActiveMultiSelectFilterDTO", "ActiveSingleSelectFilterDTO" }

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
        instance = ActiveFilterAbstractType.model_construct()
        error_messages = []
        match = 0
        # validate data type: ActiveDateFilterDTO
        if not isinstance(v, ActiveDateFilterDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ActiveDateFilterDTO`")
        else:
            match += 1
        # validate data type: ActiveGlobalDateFilterDTO
        if not isinstance(v, ActiveGlobalDateFilterDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ActiveGlobalDateFilterDTO`")
        else:
            match += 1
        # validate data type: ActiveHistogramFilterDTO
        if not isinstance(v, ActiveHistogramFilterDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ActiveHistogramFilterDTO`")
        else:
            match += 1
        # validate data type: ActiveMultiSelectFilterDTO
        if not isinstance(v, ActiveMultiSelectFilterDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ActiveMultiSelectFilterDTO`")
        else:
            match += 1
        # validate data type: ActiveIndicatorFilterDTO
        if not isinstance(v, ActiveIndicatorFilterDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ActiveIndicatorFilterDTO`")
        else:
            match += 1
        # validate data type: ActiveFeatureFilterDTO
        if not isinstance(v, ActiveFeatureFilterDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ActiveFeatureFilterDTO`")
        else:
            match += 1
        # validate data type: ActiveSingleSelectFilterDTO
        if not isinstance(v, ActiveSingleSelectFilterDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ActiveSingleSelectFilterDTO`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ActiveFilterAbstractType with oneOf schemas: ActiveDateFilterDTO, ActiveFeatureFilterDTO, ActiveGlobalDateFilterDTO, ActiveHistogramFilterDTO, ActiveIndicatorFilterDTO, ActiveMultiSelectFilterDTO, ActiveSingleSelectFilterDTO. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ActiveFilterAbstractType with oneOf schemas: ActiveDateFilterDTO, ActiveFeatureFilterDTO, ActiveGlobalDateFilterDTO, ActiveHistogramFilterDTO, ActiveIndicatorFilterDTO, ActiveMultiSelectFilterDTO, ActiveSingleSelectFilterDTO. Details: " + ", ".join(error_messages))
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

        # deserialize data into ActiveDateFilterDTO
        try:
            instance.actual_instance = ActiveDateFilterDTO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ActiveGlobalDateFilterDTO
        try:
            instance.actual_instance = ActiveGlobalDateFilterDTO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ActiveHistogramFilterDTO
        try:
            instance.actual_instance = ActiveHistogramFilterDTO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ActiveMultiSelectFilterDTO
        try:
            instance.actual_instance = ActiveMultiSelectFilterDTO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ActiveIndicatorFilterDTO
        try:
            instance.actual_instance = ActiveIndicatorFilterDTO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ActiveFeatureFilterDTO
        try:
            instance.actual_instance = ActiveFeatureFilterDTO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ActiveSingleSelectFilterDTO
        try:
            instance.actual_instance = ActiveSingleSelectFilterDTO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ActiveFilterAbstractType with oneOf schemas: ActiveDateFilterDTO, ActiveFeatureFilterDTO, ActiveGlobalDateFilterDTO, ActiveHistogramFilterDTO, ActiveIndicatorFilterDTO, ActiveMultiSelectFilterDTO, ActiveSingleSelectFilterDTO. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ActiveFilterAbstractType with oneOf schemas: ActiveDateFilterDTO, ActiveFeatureFilterDTO, ActiveGlobalDateFilterDTO, ActiveHistogramFilterDTO, ActiveIndicatorFilterDTO, ActiveMultiSelectFilterDTO, ActiveSingleSelectFilterDTO. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], ActiveDateFilterDTO, ActiveFeatureFilterDTO, ActiveGlobalDateFilterDTO, ActiveHistogramFilterDTO, ActiveIndicatorFilterDTO, ActiveMultiSelectFilterDTO, ActiveSingleSelectFilterDTO]]:
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


