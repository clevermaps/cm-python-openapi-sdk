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
from cm_python_openapi_sdk.models.dataset_dwh_type_dto import DatasetDwhTypeDTO
from cm_python_openapi_sdk.models.dataset_h3_grid_type_dto import DatasetH3GridTypeDTO
from cm_python_openapi_sdk.models.dataset_vt_type_dto import DatasetVtTypeDTO
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

DATASETTYPE_ONE_OF_SCHEMAS = ["DatasetDwhTypeDTO", "DatasetH3GridTypeDTO", "DatasetVtTypeDTO"]

class DatasetType(BaseModel):
    """
    DatasetType
    """
    # data type: DatasetDwhTypeDTO
    oneof_schema_1_validator: Optional[DatasetDwhTypeDTO] = None
    # data type: DatasetVtTypeDTO
    oneof_schema_2_validator: Optional[DatasetVtTypeDTO] = None
    # data type: DatasetH3GridTypeDTO
    oneof_schema_3_validator: Optional[DatasetH3GridTypeDTO] = None
    actual_instance: Optional[Union[DatasetDwhTypeDTO, DatasetH3GridTypeDTO, DatasetVtTypeDTO]] = None
    one_of_schemas: Set[str] = { "DatasetDwhTypeDTO", "DatasetH3GridTypeDTO", "DatasetVtTypeDTO" }

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
        instance = DatasetType.model_construct()
        error_messages = []
        match = 0
        # validate data type: DatasetDwhTypeDTO
        if not isinstance(v, DatasetDwhTypeDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DatasetDwhTypeDTO`")
        else:
            match += 1
        # validate data type: DatasetVtTypeDTO
        if not isinstance(v, DatasetVtTypeDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DatasetVtTypeDTO`")
        else:
            match += 1
        # validate data type: DatasetH3GridTypeDTO
        if not isinstance(v, DatasetH3GridTypeDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DatasetH3GridTypeDTO`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in DatasetType with oneOf schemas: DatasetDwhTypeDTO, DatasetH3GridTypeDTO, DatasetVtTypeDTO. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in DatasetType with oneOf schemas: DatasetDwhTypeDTO, DatasetH3GridTypeDTO, DatasetVtTypeDTO. Details: " + ", ".join(error_messages))
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

        # deserialize data into DatasetDwhTypeDTO
        try:
            instance.actual_instance = DatasetDwhTypeDTO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DatasetVtTypeDTO
        try:
            instance.actual_instance = DatasetVtTypeDTO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DatasetH3GridTypeDTO
        try:
            instance.actual_instance = DatasetH3GridTypeDTO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into DatasetType with oneOf schemas: DatasetDwhTypeDTO, DatasetH3GridTypeDTO, DatasetVtTypeDTO. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into DatasetType with oneOf schemas: DatasetDwhTypeDTO, DatasetH3GridTypeDTO, DatasetVtTypeDTO. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], DatasetDwhTypeDTO, DatasetH3GridTypeDTO, DatasetVtTypeDTO]]:
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


