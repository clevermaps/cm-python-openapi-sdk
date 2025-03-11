# DwhPropertyDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geometry** | **object** |  | [optional] 
**foreign_key** | **object** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.dwh_property_dto import DwhPropertyDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DwhPropertyDTO from a JSON string
dwh_property_dto_instance = DwhPropertyDTO.from_json(json)
# print the JSON string representation of the object
print(DwhPropertyDTO.to_json())

# convert the object into a dict
dwh_property_dto_dict = dwh_property_dto_instance.to_dict()
# create an instance of DwhPropertyDTO from a dict
dwh_property_dto_from_dict = DwhPropertyDTO.from_dict(dwh_property_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


