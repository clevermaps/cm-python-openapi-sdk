# VariableType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from cm_python_openapi_sdk.models.variable_type import VariableType

# TODO update the JSON string below
json = "{}"
# create an instance of VariableType from a JSON string
variable_type_instance = VariableType.from_json(json)
# print the JSON string representation of the object
print(VariableType.to_json())

# convert the object into a dict
variable_type_dict = variable_type_instance.to_dict()
# create an instance of VariableType from a dict
variable_type_from_dict = VariableType.from_dict(variable_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


