# SingleSelectFilterDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**var_property** | **str** |  | 
**order_by** | [**List[OrderByDTO]**](OrderByDTO.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.single_select_filter_dto import SingleSelectFilterDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SingleSelectFilterDTO from a JSON string
single_select_filter_dto_instance = SingleSelectFilterDTO.from_json(json)
# print the JSON string representation of the object
print(SingleSelectFilterDTO.to_json())

# convert the object into a dict
single_select_filter_dto_dict = single_select_filter_dto_instance.to_dict()
# create an instance of SingleSelectFilterDTO from a dict
single_select_filter_dto_from_dict = SingleSelectFilterDTO.from_dict(single_select_filter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


