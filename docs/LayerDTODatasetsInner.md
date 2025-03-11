# LayerDTODatasetsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | 
**visualization** | **str** |  | [optional] 
**attribute_styles** | [**List[LayerDTODatasetsInnerAttributeStylesInner]**](LayerDTODatasetsInnerAttributeStylesInner.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.layer_dto_datasets_inner import LayerDTODatasetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of LayerDTODatasetsInner from a JSON string
layer_dto_datasets_inner_instance = LayerDTODatasetsInner.from_json(json)
# print the JSON string representation of the object
print(LayerDTODatasetsInner.to_json())

# convert the object into a dict
layer_dto_datasets_inner_dict = layer_dto_datasets_inner_instance.to_dict()
# create an instance of LayerDTODatasetsInner from a dict
layer_dto_datasets_inner_from_dict = LayerDTODatasetsInner.from_dict(layer_dto_datasets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


