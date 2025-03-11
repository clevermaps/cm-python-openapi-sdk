# coding: utf-8

"""
    clevermaps-client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Optional
from cm_python_openapi_sdk.models.membership_dto import MembershipDTO
from cm_python_openapi_sdk.models.membership_paged_model_dto import MembershipPagedModelDTO
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

GETPROJECTMEMBERS200RESPONSE_ANY_OF_SCHEMAS = ["MembershipDTO", "MembershipPagedModelDTO"]

class GetProjectMembers200Response(BaseModel):
    """
    GetProjectMembers200Response
    """

    # data type: MembershipPagedModelDTO
    anyof_schema_1_validator: Optional[MembershipPagedModelDTO] = None
    # data type: MembershipDTO
    anyof_schema_2_validator: Optional[MembershipDTO] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[MembershipDTO, MembershipPagedModelDTO]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "MembershipDTO", "MembershipPagedModelDTO" }

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

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
    def actual_instance_must_validate_anyof(cls, v):
        instance = GetProjectMembers200Response.model_construct()
        error_messages = []
        # validate data type: MembershipPagedModelDTO
        if not isinstance(v, MembershipPagedModelDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MembershipPagedModelDTO`")
        else:
            return v

        # validate data type: MembershipDTO
        if not isinstance(v, MembershipDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MembershipDTO`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in GetProjectMembers200Response with anyOf schemas: MembershipDTO, MembershipPagedModelDTO. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[MembershipPagedModelDTO] = None
        try:
            instance.actual_instance = MembershipPagedModelDTO.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[MembershipDTO] = None
        try:
            instance.actual_instance = MembershipDTO.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into GetProjectMembers200Response with anyOf schemas: MembershipDTO, MembershipPagedModelDTO. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], MembershipDTO, MembershipPagedModelDTO]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


