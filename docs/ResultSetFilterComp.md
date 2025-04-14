# ResultSetFilterComp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **str** |  | 
**value** | **object** |  | [optional] 
**operator** | **str** |  | 

## Example

```python
from cm_python_openapi_sdk.models.result_set_filter_comp import ResultSetFilterComp

# TODO update the JSON string below
json = "{}"
# create an instance of ResultSetFilterComp from a JSON string
result_set_filter_comp_instance = ResultSetFilterComp.from_json(json)
# print the JSON string representation of the object
print(ResultSetFilterComp.to_json())

# convert the object into a dict
result_set_filter_comp_dict = result_set_filter_comp_instance.to_dict()
# create an instance of ResultSetFilterComp from a dict
result_set_filter_comp_from_dict = ResultSetFilterComp.from_dict(result_set_filter_comp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


