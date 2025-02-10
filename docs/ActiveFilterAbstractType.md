# ActiveFilterAbstractType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_values** | [**DefaultValuesSingleSelectDTO**](DefaultValuesSingleSelectDTO.md) |  | 
**type** | **str** |  | 
**var_property** | **str** |  | 
**format** | [**FormatDTO**](FormatDTO.md) |  | [optional] 
**order_by** | [**List[OrderByDTO]**](OrderByDTO.md) |  | [optional] 
**indicator** | **str** |  | 
**filter_selection** | **bool** |  | [optional] 
**compared** | **bool** |  | [optional] 
**dataset** | **str** |  | 

## Example

```python
from openapi_client.models.active_filter_abstract_type import ActiveFilterAbstractType

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveFilterAbstractType from a JSON string
active_filter_abstract_type_instance = ActiveFilterAbstractType.from_json(json)
# print the JSON string representation of the object
print(ActiveFilterAbstractType.to_json())

# convert the object into a dict
active_filter_abstract_type_dict = active_filter_abstract_type_instance.to_dict()
# create an instance of ActiveFilterAbstractType from a dict
active_filter_abstract_type_from_dict = ActiveFilterAbstractType.from_dict(active_filter_abstract_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


