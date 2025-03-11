# DatasetVtTypeDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**url_template** | **str** |  | 
**zoom** | [**ZoomDTO**](ZoomDTO.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.dataset_vt_type_dto import DatasetVtTypeDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetVtTypeDTO from a JSON string
dataset_vt_type_dto_instance = DatasetVtTypeDTO.from_json(json)
# print the JSON string representation of the object
print(DatasetVtTypeDTO.to_json())

# convert the object into a dict
dataset_vt_type_dto_dict = dataset_vt_type_dto_instance.to_dict()
# create an instance of DatasetVtTypeDTO from a dict
dataset_vt_type_dto_from_dict = DatasetVtTypeDTO.from_dict(dataset_vt_type_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


