# ValueOptionDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **object** |  | 
**color** | **str** |  | [optional] 
**hex_color** | **str** |  | [optional] 
**weight** | **float** |  | [optional] 
**pattern** | **str** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.value_option_dto import ValueOptionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ValueOptionDTO from a JSON string
value_option_dto_instance = ValueOptionDTO.from_json(json)
# print the JSON string representation of the object
print(ValueOptionDTO.to_json())

# convert the object into a dict
value_option_dto_dict = value_option_dto_instance.to_dict()
# create an instance of ValueOptionDTO from a dict
value_option_dto_from_dict = ValueOptionDTO.from_dict(value_option_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


