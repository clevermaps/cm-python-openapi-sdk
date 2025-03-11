# DisplayOptionsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value_options** | [**List[ValueOptionDTO]**](ValueOptionDTO.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.display_options_dto import DisplayOptionsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DisplayOptionsDTO from a JSON string
display_options_dto_instance = DisplayOptionsDTO.from_json(json)
# print the JSON string representation of the object
print(DisplayOptionsDTO.to_json())

# convert the object into a dict
display_options_dto_dict = display_options_dto_instance.to_dict()
# create an instance of DisplayOptionsDTO from a dict
display_options_dto_from_dict = DisplayOptionsDTO.from_dict(display_options_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


