# GeosearchPagedModelDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 
**content** | [**List[QueryHitDTO]**](QueryHitDTO.md) |  | [optional] 
**page** | [**PageDTO**](PageDTO.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.geosearch_paged_model_dto import GeosearchPagedModelDTO

# TODO update the JSON string below
json = "{}"
# create an instance of GeosearchPagedModelDTO from a JSON string
geosearch_paged_model_dto_instance = GeosearchPagedModelDTO.from_json(json)
# print the JSON string representation of the object
print(GeosearchPagedModelDTO.to_json())

# convert the object into a dict
geosearch_paged_model_dto_dict = geosearch_paged_model_dto_instance.to_dict()
# create an instance of GeosearchPagedModelDTO from a dict
geosearch_paged_model_dto_from_dict = GeosearchPagedModelDTO.from_dict(geosearch_paged_model_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


