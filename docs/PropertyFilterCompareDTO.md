# PropertyFilterCompareDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_name** | **str** |  | 
**value** | **object** |  | 
**operator** | **str** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.property_filter_compare_dto import PropertyFilterCompareDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyFilterCompareDTO from a JSON string
property_filter_compare_dto_instance = PropertyFilterCompareDTO.from_json(json)
# print the JSON string representation of the object
print(PropertyFilterCompareDTO.to_json())

# convert the object into a dict
property_filter_compare_dto_dict = property_filter_compare_dto_instance.to_dict()
# create an instance of PropertyFilterCompareDTO from a dict
property_filter_compare_dto_from_dict = PropertyFilterCompareDTO.from_dict(property_filter_compare_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


