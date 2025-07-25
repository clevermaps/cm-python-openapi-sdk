# TokenResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_type** | **str** |  | [optional] 
**expires_in** | **int** |  | [optional] 
**access_token** | **str** |  | 
**refresh_token** | **str** |  | [optional] 
**id_token** | **str** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.token_response_dto import TokenResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TokenResponseDTO from a JSON string
token_response_dto_instance = TokenResponseDTO.from_json(json)
# print the JSON string representation of the object
print(TokenResponseDTO.to_json())

# convert the object into a dict
token_response_dto_dict = token_response_dto_instance.to_dict()
# create an instance of TokenResponseDTO from a dict
token_response_dto_from_dict = TokenResponseDTO.from_dict(token_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


