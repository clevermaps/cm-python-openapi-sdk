# MultiSelectFilterDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**var_property** | **str** |  | 
**order_by** | [**List[OrderByDTO]**](OrderByDTO.md) |  | [optional] 

## Example

```python
from openapi_client.models.multi_select_filter_dto import MultiSelectFilterDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MultiSelectFilterDTO from a JSON string
multi_select_filter_dto_instance = MultiSelectFilterDTO.from_json(json)
# print the JSON string representation of the object
print(MultiSelectFilterDTO.to_json())

# convert the object into a dict
multi_select_filter_dto_dict = multi_select_filter_dto_instance.to_dict()
# create an instance of MultiSelectFilterDTO from a dict
multi_select_filter_dto_from_dict = MultiSelectFilterDTO.from_dict(multi_select_filter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


