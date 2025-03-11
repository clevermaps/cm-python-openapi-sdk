# DatasetH3GridTypeDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**resolution** | **int** |  | 
**zoom** | [**ZoomDTO**](ZoomDTO.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.dataset_h3_grid_type_dto import DatasetH3GridTypeDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetH3GridTypeDTO from a JSON string
dataset_h3_grid_type_dto_instance = DatasetH3GridTypeDTO.from_json(json)
# print the JSON string representation of the object
print(DatasetH3GridTypeDTO.to_json())

# convert the object into a dict
dataset_h3_grid_type_dto_dict = dataset_h3_grid_type_dto_instance.to_dict()
# create an instance of DatasetH3GridTypeDTO from a dict
dataset_h3_grid_type_dto_from_dict = DatasetH3GridTypeDTO.from_dict(dataset_h3_grid_type_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


