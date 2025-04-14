# FilterByAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** |  | [optional] 
**function** | **object** |  | [optional] 
**query** | [**DwhQueryRequest**](DwhQueryRequest.md) |  | 
**operator** | **str** |  | 

## Example

```python
from cm_python_openapi_sdk.models.filter_by_attribute import FilterByAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of FilterByAttribute from a JSON string
filter_by_attribute_instance = FilterByAttribute.from_json(json)
# print the JSON string representation of the object
print(FilterByAttribute.to_json())

# convert the object into a dict
filter_by_attribute_dict = filter_by_attribute_instance.to_dict()
# create an instance of FilterByAttribute from a dict
filter_by_attribute_from_dict = FilterByAttribute.from_dict(filter_by_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


