# VariableDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**title** | **str** |  | 
**min_value** | **float** |  | 
**max_value** | **float** |  | 
**default_value** | **float** |  | 
**format** | [**FormatDTO**](FormatDTO.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.variable_dto import VariableDTO

# TODO update the JSON string below
json = "{}"
# create an instance of VariableDTO from a JSON string
variable_dto_instance = VariableDTO.from_json(json)
# print the JSON string representation of the object
print(VariableDTO.to_json())

# convert the object into a dict
variable_dto_dict = variable_dto_instance.to_dict()
# create an instance of VariableDTO from a dict
variable_dto_from_dict = VariableDTO.from_dict(variable_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


