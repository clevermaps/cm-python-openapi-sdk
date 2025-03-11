# ExportPagedModelDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[ExportDTO]**](ExportDTO.md) |  | [optional] 
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 
**page** | [**MandatoryKeysForPagableResponse**](MandatoryKeysForPagableResponse.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.export_paged_model_dto import ExportPagedModelDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ExportPagedModelDTO from a JSON string
export_paged_model_dto_instance = ExportPagedModelDTO.from_json(json)
# print the JSON string representation of the object
print(ExportPagedModelDTO.to_json())

# convert the object into a dict
export_paged_model_dto_dict = export_paged_model_dto_instance.to_dict()
# create an instance of ExportPagedModelDTO from a dict
export_paged_model_dto_from_dict = ExportPagedModelDTO.from_dict(export_paged_model_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


