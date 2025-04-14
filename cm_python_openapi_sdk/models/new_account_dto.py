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
from cm_python_openapi_sdk.models.account_job_info import AccountJobInfo
from cm_python_openapi_sdk.models.account_preferences import AccountPreferences
from cm_python_openapi_sdk.models.account_utm_parameters import AccountUtmParameters
from typing import Optional, Set
from typing_extensions import Self

class NewAccountDTO(BaseModel):
    """
    NewAccountDTO
    """ # noqa: E501
    given_name: Annotated[str, Field(min_length=1, strict=True, max_length=50)] = Field(alias="givenName")
    surname: Annotated[str, Field(min_length=1, strict=True, max_length=50)]
    email: StrictStr
    password: Annotated[str, Field(strict=True, max_length=100)]
    consent_granted: Optional[StrictBool] = Field(default=None, alias="consentGranted")
    phone_number: Optional[Annotated[str, Field(min_length=6, strict=True, max_length=20)]] = Field(default=None, alias="phoneNumber")
    require_additional_attributes: Optional[StrictBool] = Field(default=None, alias="requireAdditionalAttributes")
    preferences: Optional[AccountPreferences] = None
    utm_parameters: Optional[AccountUtmParameters] = Field(default=None, alias="utmParameters")
    job_info: Optional[AccountJobInfo] = Field(default=None, alias="jobInfo")
    __properties: ClassVar[List[str]] = ["givenName", "surname", "email", "password", "consentGranted", "phoneNumber", "requireAdditionalAttributes", "preferences", "utmParameters", "jobInfo"]

    @field_validator('given_name')
    def given_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\p{L} \'-]+$", value):
            raise ValueError(r"must validate the regular expression /^[\p{L} '-]+$/")
        return value

    @field_validator('surname')
    def surname_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\p{L} \'-]+$", value):
            raise ValueError(r"must validate the regular expression /^[\p{L} '-]+$/")
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
        """Create an instance of NewAccountDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of preferences
        if self.preferences:
            _dict['preferences'] = self.preferences.to_dict()
        # override the default output from pydantic by calling `to_dict()` of utm_parameters
        if self.utm_parameters:
            _dict['utmParameters'] = self.utm_parameters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of job_info
        if self.job_info:
            _dict['jobInfo'] = self.job_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NewAccountDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "givenName": obj.get("givenName"),
            "surname": obj.get("surname"),
            "email": obj.get("email"),
            "password": obj.get("password"),
            "consentGranted": obj.get("consentGranted"),
            "phoneNumber": obj.get("phoneNumber"),
            "requireAdditionalAttributes": obj.get("requireAdditionalAttributes"),
            "preferences": AccountPreferences.from_dict(obj["preferences"]) if obj.get("preferences") is not None else None,
            "utmParameters": AccountUtmParameters.from_dict(obj["utmParameters"]) if obj.get("utmParameters") is not None else None,
            "jobInfo": AccountJobInfo.from_dict(obj["jobInfo"]) if obj.get("jobInfo") is not None else None
        })
        return _obj


