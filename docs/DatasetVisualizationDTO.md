# DatasetVisualizationDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**zoom** | [**ZoomDTO**](ZoomDTO.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.dataset_visualization_dto import DatasetVisualizationDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetVisualizationDTO from a JSON string
dataset_visualization_dto_instance = DatasetVisualizationDTO.from_json(json)
# print the JSON string representation of the object
print(DatasetVisualizationDTO.to_json())

# convert the object into a dict
dataset_visualization_dto_dict = dataset_visualization_dto_instance.to_dict()
# create an instance of DatasetVisualizationDTO from a dict
dataset_visualization_dto_from_dict = DatasetVisualizationDTO.from_dict(dataset_visualization_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


