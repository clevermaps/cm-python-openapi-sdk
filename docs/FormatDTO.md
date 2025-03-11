# FormatDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [default to 'number']
**fraction** | **int** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.format_dto import FormatDTO

# TODO update the JSON string below
json = "{}"
# create an instance of FormatDTO from a JSON string
format_dto_instance = FormatDTO.from_json(json)
# print the JSON string representation of the object
print(FormatDTO.to_json())

# convert the object into a dict
format_dto_dict = format_dto_instance.to_dict()
# create an instance of FormatDTO from a dict
format_dto_from_dict = FormatDTO.from_dict(format_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


