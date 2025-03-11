# IndicatorLinkDTOBlockRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**split_property** | **str** |  | [optional] 
**attribute_style** | **str** |  | [optional] 
**indicator** | **str** |  | [optional] 
**collapsed** | **bool** |  | [optional] 
**visualized** | **bool** |  | [optional] 
**filterable** | **bool** |  | [optional] 
**hide_null_items** | **bool** |  | [optional] 
**size_limit** | **int** |  | [optional] 
**order_by** | [**OrderByDTO**](OrderByDTO.md) |  | [optional] 
**vertical** | **bool** |  | [optional] 
**condensed** | **bool** |  | [optional] 
**dual_property** | **str** |  | [optional] 
**dual_attribute_style** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**default_dataset** | **str** |  | [optional] 
**default_layer** | **str** |  | [optional] 
**feature_type** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**default_period** | **str** |  | [optional] 
**additional_series** | [**List[AdditionalSeriesLinkDTO]**](AdditionalSeriesLinkDTO.md) |  | [optional] 
**annotations** | [**List[AnnotationLinkDTO]**](AnnotationLinkDTO.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.indicator_link_dto_block_rows_inner import IndicatorLinkDTOBlockRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of IndicatorLinkDTOBlockRowsInner from a JSON string
indicator_link_dto_block_rows_inner_instance = IndicatorLinkDTOBlockRowsInner.from_json(json)
# print the JSON string representation of the object
print(IndicatorLinkDTOBlockRowsInner.to_json())

# convert the object into a dict
indicator_link_dto_block_rows_inner_dict = indicator_link_dto_block_rows_inner_instance.to_dict()
# create an instance of IndicatorLinkDTOBlockRowsInner from a dict
indicator_link_dto_block_rows_inner_from_dict = IndicatorLinkDTOBlockRowsInner.from_dict(indicator_link_dto_block_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


