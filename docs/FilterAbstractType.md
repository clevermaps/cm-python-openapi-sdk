# FilterAbstractType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**var_property** | **str** |  | 
**format** | [**FormatDTO**](FormatDTO.md) |  | [optional] 
**order_by** | [**List[OrderByDTO]**](OrderByDTO.md) |  | [optional] 
**indicator** | **str** |  | 
**filter_selection** | **bool** |  | [optional] 
**dataset** | **str** |  | 

## Example

```python
from cm_python_openapi_sdk.models.filter_abstract_type import FilterAbstractType

# TODO update the JSON string below
json = "{}"
# create an instance of FilterAbstractType from a JSON string
filter_abstract_type_instance = FilterAbstractType.from_json(json)
# print the JSON string representation of the object
print(FilterAbstractType.to_json())

# convert the object into a dict
filter_abstract_type_dict = filter_abstract_type_instance.to_dict()
# create an instance of FilterAbstractType from a dict
filter_abstract_type_from_dict = FilterAbstractType.from_dict(filter_abstract_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


