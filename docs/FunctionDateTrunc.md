# FunctionDateTrunc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**content** | **List[object]** |  | 
**options** | [**FunctionDateTruncOptions**](FunctionDateTruncOptions.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.function_date_trunc import FunctionDateTrunc

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionDateTrunc from a JSON string
function_date_trunc_instance = FunctionDateTrunc.from_json(json)
# print the JSON string representation of the object
print(FunctionDateTrunc.to_json())

# convert the object into a dict
function_date_trunc_dict = function_date_trunc_instance.to_dict()
# create an instance of FunctionDateTrunc from a dict
function_date_trunc_from_dict = FunctionDateTrunc.from_dict(function_date_trunc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


