# AccessInfoDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**modified_by** | **str** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.access_info_dto import AccessInfoDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AccessInfoDTO from a JSON string
access_info_dto_instance = AccessInfoDTO.from_json(json)
# print the JSON string representation of the object
print(AccessInfoDTO.to_json())

# convert the object into a dict
access_info_dto_dict = access_info_dto_instance.to_dict()
# create an instance of AccessInfoDTO from a dict
access_info_dto_from_dict = AccessInfoDTO.from_dict(access_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


