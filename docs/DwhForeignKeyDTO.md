# DwhForeignKeyDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**foreign_key** | **str** |  | 
**geometry** | **object** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.dwh_foreign_key_dto import DwhForeignKeyDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DwhForeignKeyDTO from a JSON string
dwh_foreign_key_dto_instance = DwhForeignKeyDTO.from_json(json)
# print the JSON string representation of the object
print(DwhForeignKeyDTO.to_json())

# convert the object into a dict
dwh_foreign_key_dto_dict = dwh_foreign_key_dto_instance.to_dict()
# create an instance of DwhForeignKeyDTO from a dict
dwh_foreign_key_dto_from_dict = DwhForeignKeyDTO.from_dict(dwh_foreign_key_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


