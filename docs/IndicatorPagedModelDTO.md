# IndicatorPagedModelDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[IndicatorDTO]**](IndicatorDTO.md) |  | [optional] 
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 
**page** | [**MandatoryKeysForPagableResponse**](MandatoryKeysForPagableResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.indicator_paged_model_dto import IndicatorPagedModelDTO

# TODO update the JSON string below
json = "{}"
# create an instance of IndicatorPagedModelDTO from a JSON string
indicator_paged_model_dto_instance = IndicatorPagedModelDTO.from_json(json)
# print the JSON string representation of the object
print(IndicatorPagedModelDTO.to_json())

# convert the object into a dict
indicator_paged_model_dto_dict = indicator_paged_model_dto_instance.to_dict()
# create an instance of IndicatorPagedModelDTO from a dict
indicator_paged_model_dto_from_dict = IndicatorPagedModelDTO.from_dict(indicator_paged_model_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


