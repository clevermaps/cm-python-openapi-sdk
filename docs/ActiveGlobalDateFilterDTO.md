# ActiveGlobalDateFilterDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_values** | [**DefaultValuesDateDTO**](DefaultValuesDateDTO.md) |  | 
**type** | **str** |  | 
**var_property** | **str** |  | 

## Example

```python
from openapi_client.models.active_global_date_filter_dto import ActiveGlobalDateFilterDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveGlobalDateFilterDTO from a JSON string
active_global_date_filter_dto_instance = ActiveGlobalDateFilterDTO.from_json(json)
# print the JSON string representation of the object
print(ActiveGlobalDateFilterDTO.to_json())

# convert the object into a dict
active_global_date_filter_dto_dict = active_global_date_filter_dto_instance.to_dict()
# create an instance of ActiveGlobalDateFilterDTO from a dict
active_global_date_filter_dto_from_dict = ActiveGlobalDateFilterDTO.from_dict(active_global_date_filter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


