# IndicatorDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**type** | **str** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | 
**content** | [**IndicatorContentDTO**](IndicatorContentDTO.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.indicator_dto import IndicatorDTO

# TODO update the JSON string below
json = "{}"
# create an instance of IndicatorDTO from a JSON string
indicator_dto_instance = IndicatorDTO.from_json(json)
# print the JSON string representation of the object
print(IndicatorDTO.to_json())

# convert the object into a dict
indicator_dto_dict = indicator_dto_instance.to_dict()
# create an instance of IndicatorDTO from a dict
indicator_dto_from_dict = IndicatorDTO.from_dict(indicator_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


