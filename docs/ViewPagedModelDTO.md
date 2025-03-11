# ViewPagedModelDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[ViewDTO]**](ViewDTO.md) |  | [optional] 
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 
**page** | [**MandatoryKeysForPagableResponse**](MandatoryKeysForPagableResponse.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.view_paged_model_dto import ViewPagedModelDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ViewPagedModelDTO from a JSON string
view_paged_model_dto_instance = ViewPagedModelDTO.from_json(json)
# print the JSON string representation of the object
print(ViewPagedModelDTO.to_json())

# convert the object into a dict
view_paged_model_dto_dict = view_paged_model_dto_instance.to_dict()
# create an instance of ViewPagedModelDTO from a dict
view_paged_model_dto_from_dict = ViewPagedModelDTO.from_dict(view_paged_model_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


