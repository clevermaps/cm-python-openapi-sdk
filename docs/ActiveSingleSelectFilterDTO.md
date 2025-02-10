# ActiveSingleSelectFilterDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_values** | [**DefaultValuesSingleSelectDTO**](DefaultValuesSingleSelectDTO.md) |  | 
**type** | **str** |  | 
**var_property** | **str** |  | 
**order_by** | [**List[OrderByDTO]**](OrderByDTO.md) |  | [optional] 

## Example

```python
from openapi_client.models.active_single_select_filter_dto import ActiveSingleSelectFilterDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveSingleSelectFilterDTO from a JSON string
active_single_select_filter_dto_instance = ActiveSingleSelectFilterDTO.from_json(json)
# print the JSON string representation of the object
print(ActiveSingleSelectFilterDTO.to_json())

# convert the object into a dict
active_single_select_filter_dto_dict = active_single_select_filter_dto_instance.to_dict()
# create an instance of ActiveSingleSelectFilterDTO from a dict
active_single_select_filter_dto_from_dict = ActiveSingleSelectFilterDTO.from_dict(active_single_select_filter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


