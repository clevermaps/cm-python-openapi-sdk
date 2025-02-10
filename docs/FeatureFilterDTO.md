# FeatureFilterDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**dataset** | **str** |  | 

## Example

```python
from openapi_client.models.feature_filter_dto import FeatureFilterDTO

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureFilterDTO from a JSON string
feature_filter_dto_instance = FeatureFilterDTO.from_json(json)
# print the JSON string representation of the object
print(FeatureFilterDTO.to_json())

# convert the object into a dict
feature_filter_dto_dict = feature_filter_dto_instance.to_dict()
# create an instance of FeatureFilterDTO from a dict
feature_filter_dto_from_dict = FeatureFilterDTO.from_dict(feature_filter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


