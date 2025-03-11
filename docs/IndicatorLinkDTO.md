# IndicatorLinkDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**title** | **str** |  | [optional] 
**indicator** | **str** |  | 
**indicator_drill** | **str** |  | 
**layout** | **str** |  | [optional] 
**collapsed** | **bool** |  | [optional] 
**block_rows** | [**List[IndicatorLinkDTOBlockRowsInner]**](IndicatorLinkDTOBlockRowsInner.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.indicator_link_dto import IndicatorLinkDTO

# TODO update the JSON string below
json = "{}"
# create an instance of IndicatorLinkDTO from a JSON string
indicator_link_dto_instance = IndicatorLinkDTO.from_json(json)
# print the JSON string representation of the object
print(IndicatorLinkDTO.to_json())

# convert the object into a dict
indicator_link_dto_dict = indicator_link_dto_instance.to_dict()
# create an instance of IndicatorLinkDTO from a dict
indicator_link_dto_from_dict = IndicatorLinkDTO.from_dict(indicator_link_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


