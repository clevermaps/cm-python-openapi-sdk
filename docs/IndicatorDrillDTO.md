# IndicatorDrillDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | [**IndicatorDrillContentDTO**](IndicatorDrillContentDTO.md) |  | 

## Example

```python
from openapi_client.models.indicator_drill_dto import IndicatorDrillDTO

# TODO update the JSON string below
json = "{}"
# create an instance of IndicatorDrillDTO from a JSON string
indicator_drill_dto_instance = IndicatorDrillDTO.from_json(json)
# print the JSON string representation of the object
print(IndicatorDrillDTO.to_json())

# convert the object into a dict
indicator_drill_dto_dict = indicator_drill_dto_instance.to_dict()
# create an instance of IndicatorDrillDTO from a dict
indicator_drill_dto_from_dict = IndicatorDrillDTO.from_dict(indicator_drill_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


