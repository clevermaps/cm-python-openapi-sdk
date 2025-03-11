# IndicatorContentDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** |  | 
**scale** | **str** |  | [optional] [default to 'standard']
**distribution** | **str** |  | [optional] [default to 'geometric']
**visualizations** | [**IndicatorVisualizationsDTO**](IndicatorVisualizationsDTO.md) |  | [optional] 
**format** | [**FormatDTO**](FormatDTO.md) |  | [optional] 
**relations** | [**RelationsDTO**](RelationsDTO.md) |  | [optional] 
**scale_options** | [**ScaleOptionsDTO**](ScaleOptionsDTO.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.indicator_content_dto import IndicatorContentDTO

# TODO update the JSON string below
json = "{}"
# create an instance of IndicatorContentDTO from a JSON string
indicator_content_dto_instance = IndicatorContentDTO.from_json(json)
# print the JSON string representation of the object
print(IndicatorContentDTO.to_json())

# convert the object into a dict
indicator_content_dto_dict = indicator_content_dto_instance.to_dict()
# create an instance of IndicatorContentDTO from a dict
indicator_content_dto_from_dict = IndicatorContentDTO.from_dict(indicator_content_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


