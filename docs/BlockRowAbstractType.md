# BlockRowAbstractType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**blocks** | [**List[IndicatorLinkDTO]**](IndicatorLinkDTO.md) |  | 
**title** | **str** |  | 
**indicator** | **str** |  | 
**indicator_drill** | **str** |  | 
**layout** | **str** |  | [optional] 
**collapsed** | **bool** |  | [optional] 
**block_rows** | [**List[BlockRowAbstractType]**](BlockRowAbstractType.md) |  | 
**description** | **str** |  | [optional] 
**split_property** | **str** |  | [optional] 
**attribute_style** | **str** |  | [optional] 
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
from cm_python_openapi_sdk.models.block_row_abstract_type import BlockRowAbstractType

# TODO update the JSON string below
json = "{}"
# create an instance of BlockRowAbstractType from a JSON string
block_row_abstract_type_instance = BlockRowAbstractType.from_json(json)
# print the JSON string representation of the object
print(BlockRowAbstractType.to_json())

# convert the object into a dict
block_row_abstract_type_dict = block_row_abstract_type_instance.to_dict()
# create an instance of BlockRowAbstractType from a dict
block_row_abstract_type_from_dict = BlockRowAbstractType.from_dict(block_row_abstract_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


