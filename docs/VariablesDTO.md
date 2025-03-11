# VariablesDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**title** | **str** |  | 
**variables** | [**List[VariableDTO]**](VariableDTO.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.variables_dto import VariablesDTO

# TODO update the JSON string below
json = "{}"
# create an instance of VariablesDTO from a JSON string
variables_dto_instance = VariablesDTO.from_json(json)
# print the JSON string representation of the object
print(VariablesDTO.to_json())

# convert the object into a dict
variables_dto_dict = variables_dto_instance.to_dict()
# create an instance of VariablesDTO from a dict
variables_dto_from_dict = VariablesDTO.from_dict(variables_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


