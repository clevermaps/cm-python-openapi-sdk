# IndicatorFilterDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**indicator** | **str** |  | 
**filter_selection** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.indicator_filter_dto import IndicatorFilterDTO

# TODO update the JSON string below
json = "{}"
# create an instance of IndicatorFilterDTO from a JSON string
indicator_filter_dto_instance = IndicatorFilterDTO.from_json(json)
# print the JSON string representation of the object
print(IndicatorFilterDTO.to_json())

# convert the object into a dict
indicator_filter_dto_dict = indicator_filter_dto_instance.to_dict()
# create an instance of IndicatorFilterDTO from a dict
indicator_filter_dto_from_dict = IndicatorFilterDTO.from_dict(indicator_filter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


