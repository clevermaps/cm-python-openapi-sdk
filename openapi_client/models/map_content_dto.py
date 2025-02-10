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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.layer_dto import LayerDTO
from openapi_client.models.map_content_dto_base_layer import MapContentDTOBaseLayer
from openapi_client.models.map_content_dto_options import MapContentDTOOptions
from openapi_client.models.map_context_menu_dto import MapContextMenuDTO
from typing import Optional, Set
from typing_extensions import Self

class MapContentDTO(BaseModel):
    """
    MapContentDTO
    """ # noqa: E501
    options: Optional[MapContentDTOOptions] = None
    base_layer: Optional[MapContentDTOBaseLayer] = Field(default=None, alias="baseLayer")
    context_menu: Optional[MapContextMenuDTO] = Field(default=None, alias="contextMenu")
    layers: Optional[List[LayerDTO]] = None
    __properties: ClassVar[List[str]] = ["options", "baseLayer", "contextMenu", "layers"]

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
        """Create an instance of MapContentDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of options
        if self.options:
            _dict['options'] = self.options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of base_layer
        if self.base_layer:
            _dict['baseLayer'] = self.base_layer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of context_menu
        if self.context_menu:
            _dict['contextMenu'] = self.context_menu.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in layers (list)
        _items = []
        if self.layers:
            for _item_layers in self.layers:
                if _item_layers:
                    _items.append(_item_layers.to_dict())
            _dict['layers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MapContentDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "options": MapContentDTOOptions.from_dict(obj["options"]) if obj.get("options") is not None else None,
            "baseLayer": MapContentDTOBaseLayer.from_dict(obj["baseLayer"]) if obj.get("baseLayer") is not None else None,
            "contextMenu": MapContextMenuDTO.from_dict(obj["contextMenu"]) if obj.get("contextMenu") is not None else None,
            "layers": [LayerDTO.from_dict(_item) for _item in obj["layers"]] if obj.get("layers") is not None else None
        })
        return _obj


