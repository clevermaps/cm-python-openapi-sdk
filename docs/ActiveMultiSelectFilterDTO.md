# ActiveMultiSelectFilterDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_values** | [**DefaultValuesMultiSelectDTO**](DefaultValuesMultiSelectDTO.md) |  | 
**type** | **str** |  | 
**var_property** | **str** |  | 
**order_by** | [**List[OrderByDTO]**](OrderByDTO.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.active_multi_select_filter_dto import ActiveMultiSelectFilterDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveMultiSelectFilterDTO from a JSON string
active_multi_select_filter_dto_instance = ActiveMultiSelectFilterDTO.from_json(json)
# print the JSON string representation of the object
print(ActiveMultiSelectFilterDTO.to_json())

# convert the object into a dict
active_multi_select_filter_dto_dict = active_multi_select_filter_dto_instance.to_dict()
# create an instance of ActiveMultiSelectFilterDTO from a dict
active_multi_select_filter_dto_from_dict = ActiveMultiSelectFilterDTO.from_dict(active_multi_select_filter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


