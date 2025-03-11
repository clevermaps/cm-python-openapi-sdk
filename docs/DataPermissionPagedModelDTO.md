# DataPermissionPagedModelDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[DataPermissionDTO]**](DataPermissionDTO.md) |  | [optional] 
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 
**page** | [**MandatoryKeysForPagableResponse**](MandatoryKeysForPagableResponse.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.data_permission_paged_model_dto import DataPermissionPagedModelDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataPermissionPagedModelDTO from a JSON string
data_permission_paged_model_dto_instance = DataPermissionPagedModelDTO.from_json(json)
# print the JSON string representation of the object
print(DataPermissionPagedModelDTO.to_json())

# convert the object into a dict
data_permission_paged_model_dto_dict = data_permission_paged_model_dto_instance.to_dict()
# create an instance of DataPermissionPagedModelDTO from a dict
data_permission_paged_model_dto_from_dict = DataPermissionPagedModelDTO.from_dict(data_permission_paged_model_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


