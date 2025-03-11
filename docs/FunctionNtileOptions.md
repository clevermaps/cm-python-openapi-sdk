# FunctionNtileOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sort** | **str** |  | [optional] [default to 'asc']
**buckets** | **int** |  | [default to 4]
**partition_by** | **List[str]** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.function_ntile_options import FunctionNtileOptions

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionNtileOptions from a JSON string
function_ntile_options_instance = FunctionNtileOptions.from_json(json)
# print the JSON string representation of the object
print(FunctionNtileOptions.to_json())

# convert the object into a dict
function_ntile_options_dict = function_ntile_options_instance.to_dict()
# create an instance of FunctionNtileOptions from a dict
function_ntile_options_from_dict = FunctionNtileOptions.from_dict(function_ntile_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


