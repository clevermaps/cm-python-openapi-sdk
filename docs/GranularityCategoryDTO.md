# GranularityCategoryDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | 
**split_property_name** | **str** |  | 
**style_type** | **str** |  | 

## Example

```python
from cm_python_openapi_sdk.models.granularity_category_dto import GranularityCategoryDTO

# TODO update the JSON string below
json = "{}"
# create an instance of GranularityCategoryDTO from a JSON string
granularity_category_dto_instance = GranularityCategoryDTO.from_json(json)
# print the JSON string representation of the object
print(GranularityCategoryDTO.to_json())

# convert the object into a dict
granularity_category_dto_dict = granularity_category_dto_instance.to_dict()
# create an instance of GranularityCategoryDTO from a dict
granularity_category_dto_from_dict = GranularityCategoryDTO.from_dict(granularity_category_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


