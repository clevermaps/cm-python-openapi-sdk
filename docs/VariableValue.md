# VariableValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variable** | **str** |  | 
**value** | **float** |  | 

## Example

```python
from cm_python_openapi_sdk.models.variable_value import VariableValue

# TODO update the JSON string below
json = "{}"
# create an instance of VariableValue from a JSON string
variable_value_instance = VariableValue.from_json(json)
# print the JSON string representation of the object
print(VariableValue.to_json())

# convert the object into a dict
variable_value_dict = variable_value_instance.to_dict()
# create an instance of VariableValue from a dict
variable_value_from_dict = VariableValue.from_dict(variable_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


