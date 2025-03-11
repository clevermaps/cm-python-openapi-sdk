# IndicatorDrillContentDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocks** | [**List[BlockAbstractType]**](BlockAbstractType.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.indicator_drill_content_dto import IndicatorDrillContentDTO

# TODO update the JSON string below
json = "{}"
# create an instance of IndicatorDrillContentDTO from a JSON string
indicator_drill_content_dto_instance = IndicatorDrillContentDTO.from_json(json)
# print the JSON string representation of the object
print(IndicatorDrillContentDTO.to_json())

# convert the object into a dict
indicator_drill_content_dto_dict = indicator_drill_content_dto_instance.to_dict()
# create an instance of IndicatorDrillContentDTO from a dict
indicator_drill_content_dto_from_dict = IndicatorDrillContentDTO.from_dict(indicator_drill_content_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


