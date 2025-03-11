# DefaultValuesDateDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | [**DateFilterDefaultValueType**](DateFilterDefaultValueType.md) |  | [optional] 
**end_date** | [**DateFilterDefaultValueType**](DateFilterDefaultValueType.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.default_values_date_dto import DefaultValuesDateDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultValuesDateDTO from a JSON string
default_values_date_dto_instance = DefaultValuesDateDTO.from_json(json)
# print the JSON string representation of the object
print(DefaultValuesDateDTO.to_json())

# convert the object into a dict
default_values_date_dto_dict = default_values_date_dto_instance.to_dict()
# create an instance of DefaultValuesDateDTO from a dict
default_values_date_dto_from_dict = DefaultValuesDateDTO.from_dict(default_values_date_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


