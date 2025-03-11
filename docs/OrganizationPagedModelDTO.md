# OrganizationPagedModelDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 
**content** | [**List[OrganizationResponseDTO]**](OrganizationResponseDTO.md) |  | [optional] 
**page** | [**MandatoryKeysForPagableResponse**](MandatoryKeysForPagableResponse.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.organization_paged_model_dto import OrganizationPagedModelDTO

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationPagedModelDTO from a JSON string
organization_paged_model_dto_instance = OrganizationPagedModelDTO.from_json(json)
# print the JSON string representation of the object
print(OrganizationPagedModelDTO.to_json())

# convert the object into a dict
organization_paged_model_dto_dict = organization_paged_model_dto_instance.to_dict()
# create an instance of OrganizationPagedModelDTO from a dict
organization_paged_model_dto_from_dict = OrganizationPagedModelDTO.from_dict(organization_paged_model_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


