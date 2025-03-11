# FeatureFunctionDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **str** |  | 
**content** | [**List[FunctionPropertyType]**](FunctionPropertyType.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.feature_function_dto import FeatureFunctionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureFunctionDTO from a JSON string
feature_function_dto_instance = FeatureFunctionDTO.from_json(json)
# print the JSON string representation of the object
print(FeatureFunctionDTO.to_json())

# convert the object into a dict
feature_function_dto_dict = feature_function_dto_instance.to_dict()
# create an instance of FeatureFunctionDTO from a dict
feature_function_dto_from_dict = FeatureFunctionDTO.from_dict(feature_function_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


