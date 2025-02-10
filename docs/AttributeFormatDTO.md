# AttributeFormatDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [default to 'text']
**fraction** | **int** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.attribute_format_dto import AttributeFormatDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeFormatDTO from a JSON string
attribute_format_dto_instance = AttributeFormatDTO.from_json(json)
# print the JSON string representation of the object
print(AttributeFormatDTO.to_json())

# convert the object into a dict
attribute_format_dto_dict = attribute_format_dto_instance.to_dict()
# create an instance of AttributeFormatDTO from a dict
attribute_format_dto_from_dict = AttributeFormatDTO.from_dict(attribute_format_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


