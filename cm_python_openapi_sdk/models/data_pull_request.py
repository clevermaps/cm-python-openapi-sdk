# coding: utf-8

"""
    clevermaps-client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
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
from cm_python_openapi_sdk.models.data_pull_request_csv_options import DataPullRequestCsvOptions
from cm_python_openapi_sdk.models.data_pull_request_https_upload import DataPullRequestHttpsUpload
from cm_python_openapi_sdk.models.data_pull_request_s3_upload import DataPullRequestS3Upload
from typing import Optional, Set
from typing_extensions import Self

class DataPullRequest(BaseModel):
    """
    DataPullRequest
    """ # noqa: E501
    dataset: Annotated[str, Field(min_length=1, strict=True)]
    mode: StrictStr
    type: StrictStr
    upload: Optional[StrictStr] = None
    s3_upload: Optional[DataPullRequestS3Upload] = Field(default=None, alias="s3Upload")
    https_upload: Optional[DataPullRequestHttpsUpload] = Field(default=None, alias="httpsUpload")
    csv_options: Optional[DataPullRequestCsvOptions] = Field(default=None, alias="csvOptions")
    skip_refreshing_materialized_views: Optional[StrictBool] = Field(default=None, alias="skipRefreshingMaterializedViews")
    __properties: ClassVar[List[str]] = ["dataset", "mode", "type", "upload", "s3Upload", "httpsUpload", "csvOptions", "skipRefreshingMaterializedViews"]

    @field_validator('mode')
    def mode_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['full', 'incremental']):
            raise ValueError("must be one of enum values ('full', 'incremental')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['csv']):
            raise ValueError("must be one of enum values ('csv')")
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
        """Create an instance of DataPullRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of s3_upload
        if self.s3_upload:
            _dict['s3Upload'] = self.s3_upload.to_dict()
        # override the default output from pydantic by calling `to_dict()` of https_upload
        if self.https_upload:
            _dict['httpsUpload'] = self.https_upload.to_dict()
        # override the default output from pydantic by calling `to_dict()` of csv_options
        if self.csv_options:
            _dict['csvOptions'] = self.csv_options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataPullRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dataset": obj.get("dataset"),
            "mode": obj.get("mode"),
            "type": obj.get("type"),
            "upload": obj.get("upload"),
            "s3Upload": DataPullRequestS3Upload.from_dict(obj["s3Upload"]) if obj.get("s3Upload") is not None else None,
            "httpsUpload": DataPullRequestHttpsUpload.from_dict(obj["httpsUpload"]) if obj.get("httpsUpload") is not None else None,
            "csvOptions": DataPullRequestCsvOptions.from_dict(obj["csvOptions"]) if obj.get("csvOptions") is not None else None,
            "skipRefreshingMaterializedViews": obj.get("skipRefreshingMaterializedViews")
        })
        return _obj


