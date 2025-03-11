# FeaturePropertyType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **str** |  | 
**content** | [**List[FunctionPropertyType]**](FunctionPropertyType.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.feature_property_type import FeaturePropertyType

# TODO update the JSON string below
json = "{}"
# create an instance of FeaturePropertyType from a JSON string
feature_property_type_instance = FeaturePropertyType.from_json(json)
# print the JSON string representation of the object
print(FeaturePropertyType.to_json())

# convert the object into a dict
feature_property_type_dict = feature_property_type_instance.to_dict()
# create an instance of FeaturePropertyType from a dict
feature_property_type_from_dict = FeaturePropertyType.from_dict(feature_property_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


