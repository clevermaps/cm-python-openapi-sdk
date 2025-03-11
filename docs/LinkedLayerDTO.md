# LinkedLayerDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | 
**style** | **str** |  | [optional] 
**visible** | **bool** |  | [optional] [default to True]

## Example

```python
from cm_python_openapi_sdk.models.linked_layer_dto import LinkedLayerDTO

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedLayerDTO from a JSON string
linked_layer_dto_instance = LinkedLayerDTO.from_json(json)
# print the JSON string representation of the object
print(LinkedLayerDTO.to_json())

# convert the object into a dict
linked_layer_dto_dict = linked_layer_dto_instance.to_dict()
# create an instance of LinkedLayerDTO from a dict
linked_layer_dto_from_dict = LinkedLayerDTO.from_dict(linked_layer_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


