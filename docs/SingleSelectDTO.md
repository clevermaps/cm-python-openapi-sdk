# SingleSelectDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**var_property** | **str** |  | 
**order_by** | [**List[OrderByDTO]**](OrderByDTO.md) |  | [optional] 
**default_values** | [**DefaultValuesSingleSelectDTO**](DefaultValuesSingleSelectDTO.md) |  | [optional] 
**collapsed** | **bool** |  | [optional] 
**visualized** | **bool** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.single_select_dto import SingleSelectDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SingleSelectDTO from a JSON string
single_select_dto_instance = SingleSelectDTO.from_json(json)
# print the JSON string representation of the object
print(SingleSelectDTO.to_json())

# convert the object into a dict
single_select_dto_dict = single_select_dto_instance.to_dict()
# create an instance of SingleSelectDTO from a dict
single_select_dto_from_dict = SingleSelectDTO.from_dict(single_select_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


