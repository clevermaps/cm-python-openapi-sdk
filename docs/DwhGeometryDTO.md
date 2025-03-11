# DwhGeometryDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geometry** | **str** |  | 
**foreign_key** | **object** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.dwh_geometry_dto import DwhGeometryDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DwhGeometryDTO from a JSON string
dwh_geometry_dto_instance = DwhGeometryDTO.from_json(json)
# print the JSON string representation of the object
print(DwhGeometryDTO.to_json())

# convert the object into a dict
dwh_geometry_dto_dict = dwh_geometry_dto_instance.to_dict()
# create an instance of DwhGeometryDTO from a dict
dwh_geometry_dto_from_dict = DwhGeometryDTO.from_dict(dwh_geometry_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


