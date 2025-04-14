# FunctionDistanceOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | 
**central_point** | [**CentralPoint**](CentralPoint.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.function_distance_options import FunctionDistanceOptions

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionDistanceOptions from a JSON string
function_distance_options_instance = FunctionDistanceOptions.from_json(json)
# print the JSON string representation of the object
print(FunctionDistanceOptions.to_json())

# convert the object into a dict
function_distance_options_dict = function_distance_options_instance.to_dict()
# create an instance of FunctionDistanceOptions from a dict
function_distance_options_from_dict = FunctionDistanceOptions.from_dict(function_distance_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


