# FunctionRank


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**content** | [**List[DwhQueryPropertyTypesFunctionRank]**](DwhQueryPropertyTypesFunctionRank.md) |  | 
**options** | **object** |  | 

## Example

```python
from cm_python_openapi_sdk.models.function_rank import FunctionRank

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionRank from a JSON string
function_rank_instance = FunctionRank.from_json(json)
# print the JSON string representation of the object
print(FunctionRank.to_json())

# convert the object into a dict
function_rank_dict = function_rank_instance.to_dict()
# create an instance of FunctionRank from a dict
function_rank_from_dict = FunctionRank.from_dict(function_rank_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


