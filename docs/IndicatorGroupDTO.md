# IndicatorGroupDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**collapsed** | **bool** |  | [optional] 
**block_rows** | [**List[BlockRowAbstractType]**](BlockRowAbstractType.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.indicator_group_dto import IndicatorGroupDTO

# TODO update the JSON string below
json = "{}"
# create an instance of IndicatorGroupDTO from a JSON string
indicator_group_dto_instance = IndicatorGroupDTO.from_json(json)
# print the JSON string representation of the object
print(IndicatorGroupDTO.to_json())

# convert the object into a dict
indicator_group_dto_dict = indicator_group_dto_instance.to_dict()
# create an instance of IndicatorGroupDTO from a dict
indicator_group_dto_from_dict = IndicatorGroupDTO.from_dict(indicator_group_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


