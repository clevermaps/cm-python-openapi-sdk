# DatasetDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**type** | **str** |  | 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**origin** | **str** |  | [optional] 
**properties** | [**DatasetPropertiesDTO**](DatasetPropertiesDTO.md) |  | [optional] 
**ref** | [**DatasetType**](DatasetType.md) |  | 
**data_sources** | [**List[DataSourceDTO]**](DataSourceDTO.md) |  | [optional] 
**content** | **object** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.dataset_dto import DatasetDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetDTO from a JSON string
dataset_dto_instance = DatasetDTO.from_json(json)
# print the JSON string representation of the object
print(DatasetDTO.to_json())

# convert the object into a dict
dataset_dto_dict = dataset_dto_instance.to_dict()
# create an instance of DatasetDTO from a dict
dataset_dto_from_dict = DatasetDTO.from_dict(dataset_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


