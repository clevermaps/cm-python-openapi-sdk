# CategoryDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | 
**markers** | [**List[MarkerLinkDTO]**](MarkerLinkDTO.md) |  | 
**linked_layers** | [**List[LinkedLayerDTO]**](LinkedLayerDTO.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.category_dto import CategoryDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryDTO from a JSON string
category_dto_instance = CategoryDTO.from_json(json)
# print the JSON string representation of the object
print(CategoryDTO.to_json())

# convert the object into a dict
category_dto_dict = category_dto_instance.to_dict()
# create an instance of CategoryDTO from a dict
category_dto_from_dict = CategoryDTO.from_dict(category_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


