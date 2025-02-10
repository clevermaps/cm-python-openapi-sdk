# DefaultSelectedDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | [optional] 
**ids** | **List[object]** |  | [optional] 
**coordinates** | [**List[CenterDTO]**](CenterDTO.md) |  | [optional] 

## Example

```python
from openapi_client.models.default_selected_dto import DefaultSelectedDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultSelectedDTO from a JSON string
default_selected_dto_instance = DefaultSelectedDTO.from_json(json)
# print the JSON string representation of the object
print(DefaultSelectedDTO.to_json())

# convert the object into a dict
default_selected_dto_dict = default_selected_dto_instance.to_dict()
# create an instance of DefaultSelectedDTO from a dict
default_selected_dto_from_dict = DefaultSelectedDTO.from_dict(default_selected_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


