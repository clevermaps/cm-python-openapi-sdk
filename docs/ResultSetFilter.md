# ResultSetFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **str** |  | 
**value** | **List[object]** |  | 
**operator** | **str** |  | 

## Example

```python
from cm_python_openapi_sdk.models.result_set_filter import ResultSetFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ResultSetFilter from a JSON string
result_set_filter_instance = ResultSetFilter.from_json(json)
# print the JSON string representation of the object
print(ResultSetFilter.to_json())

# convert the object into a dict
result_set_filter_dict = result_set_filter_instance.to_dict()
# create an instance of ResultSetFilter from a dict
result_set_filter_from_dict = ResultSetFilter.from_dict(result_set_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


