# FilterByIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** |  | [optional] 
**function** | **object** |  | [optional] 
**value** | **List[object]** |  | 
**operator** | **str** |  | 

## Example

```python
from cm_python_openapi_sdk.models.filter_by_in import FilterByIn

# TODO update the JSON string below
json = "{}"
# create an instance of FilterByIn from a JSON string
filter_by_in_instance = FilterByIn.from_json(json)
# print the JSON string representation of the object
print(FilterByIn.to_json())

# convert the object into a dict
filter_by_in_dict = filter_by_in_instance.to_dict()
# create an instance of FilterByIn from a dict
filter_by_in_from_dict = FilterByIn.from_dict(filter_by_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


