# FunctionAggTypeGeneral


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**content** | **List[object]** |  | 
**options** | **object** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.function_agg_type_general import FunctionAggTypeGeneral

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionAggTypeGeneral from a JSON string
function_agg_type_general_instance = FunctionAggTypeGeneral.from_json(json)
# print the JSON string representation of the object
print(FunctionAggTypeGeneral.to_json())

# convert the object into a dict
function_agg_type_general_dict = function_agg_type_general_instance.to_dict()
# create an instance of FunctionAggTypeGeneral from a dict
function_agg_type_general_from_dict = FunctionAggTypeGeneral.from_dict(function_agg_type_general_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


