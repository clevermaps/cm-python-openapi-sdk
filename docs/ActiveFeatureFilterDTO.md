# ActiveFeatureFilterDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_values** | [**DefaultValuesFeatureDTO**](DefaultValuesFeatureDTO.md) |  | 
**compared** | **bool** |  | [optional] 
**type** | **str** |  | 
**dataset** | **str** |  | 

## Example

```python
from cm_python_openapi_sdk.models.active_feature_filter_dto import ActiveFeatureFilterDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveFeatureFilterDTO from a JSON string
active_feature_filter_dto_instance = ActiveFeatureFilterDTO.from_json(json)
# print the JSON string representation of the object
print(ActiveFeatureFilterDTO.to_json())

# convert the object into a dict
active_feature_filter_dto_dict = active_feature_filter_dto_instance.to_dict()
# create an instance of ActiveFeatureFilterDTO from a dict
active_feature_filter_dto_from_dict = ActiveFeatureFilterDTO.from_dict(active_feature_filter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


