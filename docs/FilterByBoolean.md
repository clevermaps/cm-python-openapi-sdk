# FilterByBoolean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** |  | 
**content** | [**List[FilterBy]**](FilterBy.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.filter_by_boolean import FilterByBoolean

# TODO update the JSON string below
json = "{}"
# create an instance of FilterByBoolean from a JSON string
filter_by_boolean_instance = FilterByBoolean.from_json(json)
# print the JSON string representation of the object
print(FilterByBoolean.to_json())

# convert the object into a dict
filter_by_boolean_dict = filter_by_boolean_instance.to_dict()
# create an instance of FilterByBoolean from a dict
filter_by_boolean_from_dict = FilterByBoolean.from_dict(filter_by_boolean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


