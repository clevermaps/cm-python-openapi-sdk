# DataPermissionContentDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**filters** | **List[object]** |  | 

## Example

```python
from cm_python_openapi_sdk.models.data_permission_content_dto import DataPermissionContentDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataPermissionContentDTO from a JSON string
data_permission_content_dto_instance = DataPermissionContentDTO.from_json(json)
# print the JSON string representation of the object
print(DataPermissionContentDTO.to_json())

# convert the object into a dict
data_permission_content_dto_dict = data_permission_content_dto_instance.to_dict()
# create an instance of DataPermissionContentDTO from a dict
data_permission_content_dto_from_dict = DataPermissionContentDTO.from_dict(data_permission_content_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


