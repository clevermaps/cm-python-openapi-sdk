# DatasetPagedModelDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[DatasetDTO]**](DatasetDTO.md) |  | [optional] 
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 
**page** | [**MandatoryKeysForPagableResponse**](MandatoryKeysForPagableResponse.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.dataset_paged_model_dto import DatasetPagedModelDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetPagedModelDTO from a JSON string
dataset_paged_model_dto_instance = DatasetPagedModelDTO.from_json(json)
# print the JSON string representation of the object
print(DatasetPagedModelDTO.to_json())

# convert the object into a dict
dataset_paged_model_dto_dict = dataset_paged_model_dto_instance.to_dict()
# create an instance of DatasetPagedModelDTO from a dict
dataset_paged_model_dto_from_dict = DatasetPagedModelDTO.from_dict(dataset_paged_model_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


