# FilterBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** |  | 
**value** | **List[object]** |  | 
**function** | **object** |  | [optional] 
**operator** | **str** |  | 
**query** | [**DwhQueryRequest**](DwhQueryRequest.md) |  | 
**content** | [**List[FilterBy]**](FilterBy.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.filter_by import FilterBy

# TODO update the JSON string below
json = "{}"
# create an instance of FilterBy from a JSON string
filter_by_instance = FilterBy.from_json(json)
# print the JSON string representation of the object
print(FilterBy.to_json())

# convert the object into a dict
filter_by_dict = filter_by_instance.to_dict()
# create an instance of FilterBy from a dict
filter_by_from_dict = FilterBy.from_dict(filter_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


