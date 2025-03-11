# FunctionDistance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**options** | [**FunctionDistanceOptions**](FunctionDistanceOptions.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.function_distance import FunctionDistance

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionDistance from a JSON string
function_distance_instance = FunctionDistance.from_json(json)
# print the JSON string representation of the object
print(FunctionDistance.to_json())

# convert the object into a dict
function_distance_dict = function_distance_instance.to_dict()
# create an instance of FunctionDistance from a dict
function_distance_from_dict = FunctionDistance.from_dict(function_distance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


