# FunctionNtileContentInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**content** | **List[object]** |  | 
**options** | **object** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.function_ntile_content_inner import FunctionNtileContentInner

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionNtileContentInner from a JSON string
function_ntile_content_inner_instance = FunctionNtileContentInner.from_json(json)
# print the JSON string representation of the object
print(FunctionNtileContentInner.to_json())

# convert the object into a dict
function_ntile_content_inner_dict = function_ntile_content_inner_instance.to_dict()
# create an instance of FunctionNtileContentInner from a dict
function_ntile_content_inner_from_dict = FunctionNtileContentInner.from_dict(function_ntile_content_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


