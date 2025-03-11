# ActiveIndicatorFilterDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_values** | [**DefaultValuesIndicatorDTO**](DefaultValuesIndicatorDTO.md) |  | 
**type** | **str** |  | 
**indicator** | **str** |  | 
**filter_selection** | **bool** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.active_indicator_filter_dto import ActiveIndicatorFilterDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveIndicatorFilterDTO from a JSON string
active_indicator_filter_dto_instance = ActiveIndicatorFilterDTO.from_json(json)
# print the JSON string representation of the object
print(ActiveIndicatorFilterDTO.to_json())

# convert the object into a dict
active_indicator_filter_dto_dict = active_indicator_filter_dto_instance.to_dict()
# create an instance of ActiveIndicatorFilterDTO from a dict
active_indicator_filter_dto_from_dict = ActiveIndicatorFilterDTO.from_dict(active_indicator_filter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


