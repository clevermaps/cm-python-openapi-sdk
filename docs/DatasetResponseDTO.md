# DatasetResponseDTO


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
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 
**page** | [**PageDTO**](PageDTO.md) |  | [optional] 
**access_info** | [**AccessInfoDTO**](AccessInfoDTO.md) |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.dataset_response_dto import DatasetResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetResponseDTO from a JSON string
dataset_response_dto_instance = DatasetResponseDTO.from_json(json)
# print the JSON string representation of the object
print(DatasetResponseDTO.to_json())

# convert the object into a dict
dataset_response_dto_dict = dataset_response_dto_instance.to_dict()
# create an instance of DatasetResponseDTO from a dict
dataset_response_dto_from_dict = DatasetResponseDTO.from_dict(dataset_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


