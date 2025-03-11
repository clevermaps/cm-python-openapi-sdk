# DataPermissionDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | [**DataPermissionContentDTO**](DataPermissionContentDTO.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.data_permission_dto import DataPermissionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataPermissionDTO from a JSON string
data_permission_dto_instance = DataPermissionDTO.from_json(json)
# print the JSON string representation of the object
print(DataPermissionDTO.to_json())

# convert the object into a dict
data_permission_dto_dict = data_permission_dto_instance.to_dict()
# create an instance of DataPermissionDTO from a dict
data_permission_dto_from_dict = DataPermissionDTO.from_dict(data_permission_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


