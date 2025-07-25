# ViewResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**type** | **str** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | 
**content** | [**ViewContentDTO**](ViewContentDTO.md) |  | 
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 
**page** | [**PageDTO**](PageDTO.md) |  | [optional] 
**access_info** | [**AccessInfoDTO**](AccessInfoDTO.md) |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.view_response_dto import ViewResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ViewResponseDTO from a JSON string
view_response_dto_instance = ViewResponseDTO.from_json(json)
# print the JSON string representation of the object
print(ViewResponseDTO.to_json())

# convert the object into a dict
view_response_dto_dict = view_response_dto_instance.to_dict()
# create an instance of ViewResponseDTO from a dict
view_response_dto_from_dict = ViewResponseDTO.from_dict(view_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


