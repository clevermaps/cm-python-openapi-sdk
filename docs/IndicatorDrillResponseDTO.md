# IndicatorDrillResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | [**IndicatorDrillContentDTO**](IndicatorDrillContentDTO.md) |  | 
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 
**page** | [**PageDTO**](PageDTO.md) |  | [optional] 
**access_info** | [**AccessInfoDTO**](AccessInfoDTO.md) |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.indicator_drill_response_dto import IndicatorDrillResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of IndicatorDrillResponseDTO from a JSON string
indicator_drill_response_dto_instance = IndicatorDrillResponseDTO.from_json(json)
# print the JSON string representation of the object
print(IndicatorDrillResponseDTO.to_json())

# convert the object into a dict
indicator_drill_response_dto_dict = indicator_drill_response_dto_instance.to_dict()
# create an instance of IndicatorDrillResponseDTO from a dict
indicator_drill_response_dto_from_dict = IndicatorDrillResponseDTO.from_dict(indicator_drill_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


