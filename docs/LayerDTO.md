# LayerDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**indicator** | **str** |  | [default to 'inherit']
**base_style** | [**StyleDTO**](StyleDTO.md) |  | [optional] 
**show_indicator_value_labels** | **bool** |  | [optional] 
**cluster_points** | **bool** |  | [optional] [default to True]
**keep_filtered** | **bool** |  | [optional] 
**visible** | **bool** |  | [optional] [default to True]
**default_dataset** | **str** |  | [optional] 
**default_visualization** | **str** |  | [optional] 
**datasets** | [**List[LayerDTODatasetsInner]**](LayerDTODatasetsInner.md) |  | 

## Example

```python
from openapi_client.models.layer_dto import LayerDTO

# TODO update the JSON string below
json = "{}"
# create an instance of LayerDTO from a JSON string
layer_dto_instance = LayerDTO.from_json(json)
# print the JSON string representation of the object
print(LayerDTO.to_json())

# convert the object into a dict
layer_dto_dict = layer_dto_instance.to_dict()
# create an instance of LayerDTO from a dict
layer_dto_from_dict = LayerDTO.from_dict(layer_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


