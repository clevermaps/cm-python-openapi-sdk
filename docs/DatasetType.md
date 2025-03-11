# DatasetType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**subtype** | **str** |  | 
**geometry** | **str** |  | [optional] 
**h3_geometries** | **List[str]** |  | [optional] 
**visualizations** | [**List[DatasetVisualizationDTO]**](DatasetVisualizationDTO.md) |  | [optional] 
**table** | **str** |  | [optional] 
**geometry_table** | **str** |  | [optional] 
**primary_key** | **str** |  | 
**categorizable** | **bool** |  | [optional] [default to True]
**full_text_index** | **bool** |  | [optional] 
**spatial_index** | **bool** |  | [optional] 
**properties** | [**List[DwhAbstractProperty]**](DwhAbstractProperty.md) |  | 
**zoom** | [**ZoomDTO**](ZoomDTO.md) |  | [optional] 
**url_template** | **str** |  | 
**resolution** | **int** |  | 

## Example

```python
from cm_python_openapi_sdk.models.dataset_type import DatasetType

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetType from a JSON string
dataset_type_instance = DatasetType.from_json(json)
# print the JSON string representation of the object
print(DatasetType.to_json())

# convert the object into a dict
dataset_type_dict = dataset_type_instance.to_dict()
# create an instance of DatasetType from a dict
dataset_type_from_dict = DatasetType.from_dict(dataset_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


