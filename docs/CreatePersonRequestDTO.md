# CreatePersonRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** |  | 
**project_id_invitation** | **str** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.create_person_request_dto import CreatePersonRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePersonRequestDTO from a JSON string
create_person_request_dto_instance = CreatePersonRequestDTO.from_json(json)
# print the JSON string representation of the object
print(CreatePersonRequestDTO.to_json())

# convert the object into a dict
create_person_request_dto_dict = create_person_request_dto_instance.to_dict()
# create an instance of CreatePersonRequestDTO from a dict
create_person_request_dto_from_dict = CreatePersonRequestDTO.from_dict(create_person_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


