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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class DataPullRequestS3Upload(BaseModel):
    """
    Object specifying properties for dataPull from any AWS S3.
    """ # noqa: E501
    uri: StrictStr = Field(description="AWS S3 URI (e.g. s3://can-s3-dwh-pull-test/shops.csv).")
    access_key_id: Optional[StrictStr] = Field(default=None, description="AWS S3 Access Key ID with access to the file specified in 'uri'.", alias="accessKeyId")
    secret_access_key: Optional[StrictStr] = Field(default=None, description="AWS S3 Secret Access Key with access to the file specified in 'uri'.", alias="secretAccessKey")
    region: Optional[StrictStr] = Field(default=None, description="AWS S3 region of the file.")
    endpoint_override: Optional[StrictStr] = Field(default=None, description="AWS S3 region of the file.", alias="endpointOverride")
    force_path_style: Optional[StrictBool] = Field(default=None, description="If true, path style is forced for S3 URIs, otherwise virtual hosted style is used.", alias="forcePathStyle")
    __properties: ClassVar[List[str]] = ["uri", "accessKeyId", "secretAccessKey", "region", "endpointOverride", "forcePathStyle"]

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
        """Create an instance of DataPullRequestS3Upload from a JSON string"""
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
        """Create an instance of DataPullRequestS3Upload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uri": obj.get("uri"),
            "accessKeyId": obj.get("accessKeyId"),
            "secretAccessKey": obj.get("secretAccessKey"),
            "region": obj.get("region"),
            "endpointOverride": obj.get("endpointOverride"),
            "forcePathStyle": obj.get("forcePathStyle")
        })
        return _obj


