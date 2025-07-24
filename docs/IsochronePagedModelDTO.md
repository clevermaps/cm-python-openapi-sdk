# IsochronePagedModelDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 
**content** | [**List[IsochroneDTO]**](IsochroneDTO.md) |  | [optional] 
**page** | [**PageDTO**](PageDTO.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.isochrone_paged_model_dto import IsochronePagedModelDTO

# TODO update the JSON string below
json = "{}"
# create an instance of IsochronePagedModelDTO from a JSON string
isochrone_paged_model_dto_instance = IsochronePagedModelDTO.from_json(json)
# print the JSON string representation of the object
print(IsochronePagedModelDTO.to_json())

# convert the object into a dict
isochrone_paged_model_dto_dict = isochrone_paged_model_dto_instance.to_dict()
# create an instance of IsochronePagedModelDTO from a dict
isochrone_paged_model_dto_from_dict = IsochronePagedModelDTO.from_dict(isochrone_paged_model_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


