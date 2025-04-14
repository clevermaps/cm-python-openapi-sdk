# FunctionRowNumber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**content** | [**List[FunctionNtileContentInner]**](FunctionNtileContentInner.md) |  | 
**options** | **object** |  | 

## Example

```python
from cm_python_openapi_sdk.models.function_row_number import FunctionRowNumber

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionRowNumber from a JSON string
function_row_number_instance = FunctionRowNumber.from_json(json)
# print the JSON string representation of the object
print(FunctionRowNumber.to_json())

# convert the object into a dict
function_row_number_dict = function_row_number_instance.to_dict()
# create an instance of FunctionRowNumber from a dict
function_row_number_from_dict = FunctionRowNumber.from_dict(function_row_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


