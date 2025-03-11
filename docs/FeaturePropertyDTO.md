# FeaturePropertyDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from cm_python_openapi_sdk.models.feature_property_dto import FeaturePropertyDTO

# TODO update the JSON string below
json = "{}"
# create an instance of FeaturePropertyDTO from a JSON string
feature_property_dto_instance = FeaturePropertyDTO.from_json(json)
# print the JSON string representation of the object
print(FeaturePropertyDTO.to_json())

# convert the object into a dict
feature_property_dto_dict = feature_property_dto_instance.to_dict()
# create an instance of FeaturePropertyDTO from a dict
feature_property_dto_from_dict = FeaturePropertyDTO.from_dict(feature_property_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


