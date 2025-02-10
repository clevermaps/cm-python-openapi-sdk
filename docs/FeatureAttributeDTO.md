# FeatureAttributeDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [default to 'property']
**value** | **str** |  | 
**format** | [**AttributeFormatDTO**](AttributeFormatDTO.md) |  | [optional] 
**layout** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.feature_attribute_dto import FeatureAttributeDTO

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureAttributeDTO from a JSON string
feature_attribute_dto_instance = FeatureAttributeDTO.from_json(json)
# print the JSON string representation of the object
print(FeatureAttributeDTO.to_json())

# convert the object into a dict
feature_attribute_dto_dict = feature_attribute_dto_instance.to_dict()
# create an instance of FeatureAttributeDTO from a dict
feature_attribute_dto_from_dict = FeatureAttributeDTO.from_dict(feature_attribute_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


