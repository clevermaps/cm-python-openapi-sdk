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
from cm_python_openapi_sdk.models.cuzk_parcel_info_dto import CuzkParcelInfoDTO
from cm_python_openapi_sdk.models.google_earth_dto import GoogleEarthDTO
from cm_python_openapi_sdk.models.google_satellite_dto import GoogleSatelliteDTO
from cm_python_openapi_sdk.models.google_street_view_dto import GoogleStreetViewDTO
from cm_python_openapi_sdk.models.mapycz_ortophoto_dto import MapyczOrtophotoDTO
from cm_python_openapi_sdk.models.mapycz_panorama_dto import MapyczPanoramaDTO
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

MAPCONTEXTMENUITEMABSTRACTTYPE_ONE_OF_SCHEMAS = ["CuzkParcelInfoDTO", "GoogleEarthDTO", "GoogleSatelliteDTO", "GoogleStreetViewDTO", "MapyczOrtophotoDTO", "MapyczPanoramaDTO"]

class MapContextMenuItemAbstractType(BaseModel):
    """
    MapContextMenuItemAbstractType
    """
    # data type: GoogleSatelliteDTO
    oneof_schema_1_validator: Optional[GoogleSatelliteDTO] = None
    # data type: GoogleStreetViewDTO
    oneof_schema_2_validator: Optional[GoogleStreetViewDTO] = None
    # data type: GoogleEarthDTO
    oneof_schema_3_validator: Optional[GoogleEarthDTO] = None
    # data type: MapyczPanoramaDTO
    oneof_schema_4_validator: Optional[MapyczPanoramaDTO] = None
    # data type: MapyczOrtophotoDTO
    oneof_schema_5_validator: Optional[MapyczOrtophotoDTO] = None
    # data type: CuzkParcelInfoDTO
    oneof_schema_6_validator: Optional[CuzkParcelInfoDTO] = None
    actual_instance: Optional[Union[CuzkParcelInfoDTO, GoogleEarthDTO, GoogleSatelliteDTO, GoogleStreetViewDTO, MapyczOrtophotoDTO, MapyczPanoramaDTO]] = None
    one_of_schemas: Set[str] = { "CuzkParcelInfoDTO", "GoogleEarthDTO", "GoogleSatelliteDTO", "GoogleStreetViewDTO", "MapyczOrtophotoDTO", "MapyczPanoramaDTO" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
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
    def actual_instance_must_validate_oneof(cls, v):
        instance = MapContextMenuItemAbstractType.model_construct()
        error_messages = []
        match = 0
        # validate data type: GoogleSatelliteDTO
        if not isinstance(v, GoogleSatelliteDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GoogleSatelliteDTO`")
        else:
            match += 1
        # validate data type: GoogleStreetViewDTO
        if not isinstance(v, GoogleStreetViewDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GoogleStreetViewDTO`")
        else:
            match += 1
        # validate data type: GoogleEarthDTO
        if not isinstance(v, GoogleEarthDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GoogleEarthDTO`")
        else:
            match += 1
        # validate data type: MapyczPanoramaDTO
        if not isinstance(v, MapyczPanoramaDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MapyczPanoramaDTO`")
        else:
            match += 1
        # validate data type: MapyczOrtophotoDTO
        if not isinstance(v, MapyczOrtophotoDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MapyczOrtophotoDTO`")
        else:
            match += 1
        # validate data type: CuzkParcelInfoDTO
        if not isinstance(v, CuzkParcelInfoDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CuzkParcelInfoDTO`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in MapContextMenuItemAbstractType with oneOf schemas: CuzkParcelInfoDTO, GoogleEarthDTO, GoogleSatelliteDTO, GoogleStreetViewDTO, MapyczOrtophotoDTO, MapyczPanoramaDTO. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in MapContextMenuItemAbstractType with oneOf schemas: CuzkParcelInfoDTO, GoogleEarthDTO, GoogleSatelliteDTO, GoogleStreetViewDTO, MapyczOrtophotoDTO, MapyczPanoramaDTO. Details: " + ", ".join(error_messages))
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

        # use oneOf discriminator to lookup the data type
        _data_type = json.loads(json_str).get("type")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `type` in the input.")

        # check if data type is `CuzkParcelInfoDTO`
        if _data_type == "cuzkParcelInfo":
            instance.actual_instance = CuzkParcelInfoDTO.from_json(json_str)
            return instance

        # check if data type is `GoogleEarthDTO`
        if _data_type == "googleEarth":
            instance.actual_instance = GoogleEarthDTO.from_json(json_str)
            return instance

        # check if data type is `GoogleSatelliteDTO`
        if _data_type == "googleSatellite":
            instance.actual_instance = GoogleSatelliteDTO.from_json(json_str)
            return instance

        # check if data type is `GoogleStreetViewDTO`
        if _data_type == "googleStreetView":
            instance.actual_instance = GoogleStreetViewDTO.from_json(json_str)
            return instance

        # check if data type is `MapyczOrtophotoDTO`
        if _data_type == "mapyczOrtophoto":
            instance.actual_instance = MapyczOrtophotoDTO.from_json(json_str)
            return instance

        # check if data type is `MapyczPanoramaDTO`
        if _data_type == "mapyczPanorama":
            instance.actual_instance = MapyczPanoramaDTO.from_json(json_str)
            return instance

        # check if data type is `CuzkParcelInfoDTO`
        if _data_type == "CuzkParcelInfoDTO":
            instance.actual_instance = CuzkParcelInfoDTO.from_json(json_str)
            return instance

        # check if data type is `GoogleEarthDTO`
        if _data_type == "GoogleEarthDTO":
            instance.actual_instance = GoogleEarthDTO.from_json(json_str)
            return instance

        # check if data type is `GoogleSatelliteDTO`
        if _data_type == "GoogleSatelliteDTO":
            instance.actual_instance = GoogleSatelliteDTO.from_json(json_str)
            return instance

        # check if data type is `GoogleStreetViewDTO`
        if _data_type == "GoogleStreetViewDTO":
            instance.actual_instance = GoogleStreetViewDTO.from_json(json_str)
            return instance

        # check if data type is `MapyczOrtophotoDTO`
        if _data_type == "MapyczOrtophotoDTO":
            instance.actual_instance = MapyczOrtophotoDTO.from_json(json_str)
            return instance

        # check if data type is `MapyczPanoramaDTO`
        if _data_type == "MapyczPanoramaDTO":
            instance.actual_instance = MapyczPanoramaDTO.from_json(json_str)
            return instance

        # deserialize data into GoogleSatelliteDTO
        try:
            instance.actual_instance = GoogleSatelliteDTO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GoogleStreetViewDTO
        try:
            instance.actual_instance = GoogleStreetViewDTO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GoogleEarthDTO
        try:
            instance.actual_instance = GoogleEarthDTO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into MapyczPanoramaDTO
        try:
            instance.actual_instance = MapyczPanoramaDTO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into MapyczOrtophotoDTO
        try:
            instance.actual_instance = MapyczOrtophotoDTO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CuzkParcelInfoDTO
        try:
            instance.actual_instance = CuzkParcelInfoDTO.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into MapContextMenuItemAbstractType with oneOf schemas: CuzkParcelInfoDTO, GoogleEarthDTO, GoogleSatelliteDTO, GoogleStreetViewDTO, MapyczOrtophotoDTO, MapyczPanoramaDTO. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into MapContextMenuItemAbstractType with oneOf schemas: CuzkParcelInfoDTO, GoogleEarthDTO, GoogleSatelliteDTO, GoogleStreetViewDTO, MapyczOrtophotoDTO, MapyczPanoramaDTO. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], CuzkParcelInfoDTO, GoogleEarthDTO, GoogleSatelliteDTO, GoogleStreetViewDTO, MapyczOrtophotoDTO, MapyczPanoramaDTO]]:
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


