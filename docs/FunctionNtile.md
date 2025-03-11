# FunctionNtile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**content** | **List[object]** |  | 
**options** | [**FunctionNtileOptions**](FunctionNtileOptions.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.function_ntile import FunctionNtile

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionNtile from a JSON string
function_ntile_instance = FunctionNtile.from_json(json)
# print the JSON string representation of the object
print(FunctionNtile.to_json())

# convert the object into a dict
function_ntile_dict = function_ntile_instance.to_dict()
# create an instance of FunctionNtile from a dict
function_ntile_from_dict = FunctionNtile.from_dict(function_ntile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


