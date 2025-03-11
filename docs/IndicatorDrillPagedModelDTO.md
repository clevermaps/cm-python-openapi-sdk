# IndicatorDrillPagedModelDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[IndicatorDrillDTO]**](IndicatorDrillDTO.md) |  | [optional] 
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 
**page** | [**MandatoryKeysForPagableResponse**](MandatoryKeysForPagableResponse.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.indicator_drill_paged_model_dto import IndicatorDrillPagedModelDTO

# TODO update the JSON string below
json = "{}"
# create an instance of IndicatorDrillPagedModelDTO from a JSON string
indicator_drill_paged_model_dto_instance = IndicatorDrillPagedModelDTO.from_json(json)
# print the JSON string representation of the object
print(IndicatorDrillPagedModelDTO.to_json())

# convert the object into a dict
indicator_drill_paged_model_dto_dict = indicator_drill_paged_model_dto_instance.to_dict()
# create an instance of IndicatorDrillPagedModelDTO from a dict
indicator_drill_paged_model_dto_from_dict = IndicatorDrillPagedModelDTO.from_dict(indicator_drill_paged_model_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


