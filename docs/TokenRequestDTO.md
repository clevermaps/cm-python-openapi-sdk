# TokenRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh_token** | **str** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.token_request_dto import TokenRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TokenRequestDTO from a JSON string
token_request_dto_instance = TokenRequestDTO.from_json(json)
# print the JSON string representation of the object
print(TokenRequestDTO.to_json())

# convert the object into a dict
token_request_dto_dict = token_request_dto_instance.to_dict()
# create an instance of TokenRequestDTO from a dict
token_request_dto_from_dict = TokenRequestDTO.from_dict(token_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


