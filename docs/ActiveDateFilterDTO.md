# ActiveDateFilterDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_values** | [**DefaultValuesDateDTO**](DefaultValuesDateDTO.md) |  | 
**type** | **str** |  | 
**var_property** | **str** |  | 

## Example

```python
from cm_python_openapi_sdk.models.active_date_filter_dto import ActiveDateFilterDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDateFilterDTO from a JSON string
active_date_filter_dto_instance = ActiveDateFilterDTO.from_json(json)
# print the JSON string representation of the object
print(ActiveDateFilterDTO.to_json())

# convert the object into a dict
active_date_filter_dto_dict = active_date_filter_dto_instance.to_dict()
# create an instance of ActiveDateFilterDTO from a dict
active_date_filter_dto_from_dict = ActiveDateFilterDTO.from_dict(active_date_filter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


