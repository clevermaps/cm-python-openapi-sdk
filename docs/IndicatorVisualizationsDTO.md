# IndicatorVisualizationsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**areas** | **bool** |  | [optional] 
**grid** | **bool** |  | [optional] 
**zones** | **bool** |  | [optional] 
**line** | **bool** |  | [optional] 
**dotmap** | **bool** |  | [optional] 
**heatmap** | **bool** |  | [optional] 
**dominance** | **bool** |  | [optional] 
**heatmap_scale_factor** | **float** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.indicator_visualizations_dto import IndicatorVisualizationsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of IndicatorVisualizationsDTO from a JSON string
indicator_visualizations_dto_instance = IndicatorVisualizationsDTO.from_json(json)
# print the JSON string representation of the object
print(IndicatorVisualizationsDTO.to_json())

# convert the object into a dict
indicator_visualizations_dto_dict = indicator_visualizations_dto_instance.to_dict()
# create an instance of IndicatorVisualizationsDTO from a dict
indicator_visualizations_dto_from_dict = IndicatorVisualizationsDTO.from_dict(indicator_visualizations_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


