# FilterByComp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** |  | [optional] 
**value** | **object** |  | [optional] 
**function** | [**DwhQueryPropertyTypes**](DwhQueryPropertyTypes.md) |  | [optional] 
**operator** | **str** |  | 

## Example

```python
from cm_python_openapi_sdk.models.filter_by_comp import FilterByComp

# TODO update the JSON string below
json = "{}"
# create an instance of FilterByComp from a JSON string
filter_by_comp_instance = FilterByComp.from_json(json)
# print the JSON string representation of the object
print(FilterByComp.to_json())

# convert the object into a dict
filter_by_comp_dict = filter_by_comp_instance.to_dict()
# create an instance of FilterByComp from a dict
filter_by_comp_from_dict = FilterByComp.from_dict(filter_by_comp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


