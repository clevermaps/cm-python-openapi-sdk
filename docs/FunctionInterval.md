# FunctionInterval


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**content** | [**List[DwhQueryNumberType]**](DwhQueryNumberType.md) |  | 
**options** | [**FunctionDateTruncateOptions**](FunctionDateTruncateOptions.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.function_interval import FunctionInterval

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionInterval from a JSON string
function_interval_instance = FunctionInterval.from_json(json)
# print the JSON string representation of the object
print(FunctionInterval.to_json())

# convert the object into a dict
function_interval_dict = function_interval_instance.to_dict()
# create an instance of FunctionInterval from a dict
function_interval_from_dict = FunctionInterval.from_dict(function_interval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


