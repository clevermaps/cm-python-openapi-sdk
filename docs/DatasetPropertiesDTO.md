# DatasetPropertiesDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_title** | [**FeaturePropertyType**](FeaturePropertyType.md) |  | [optional] 
**feature_subtitle** | [**FeaturePropertyType**](FeaturePropertyType.md) |  | [optional] 
**feature_attributes** | [**List[FeatureAttributeDTO]**](FeatureAttributeDTO.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.dataset_properties_dto import DatasetPropertiesDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetPropertiesDTO from a JSON string
dataset_properties_dto_instance = DatasetPropertiesDTO.from_json(json)
# print the JSON string representation of the object
print(DatasetPropertiesDTO.to_json())

# convert the object into a dict
dataset_properties_dto_dict = dataset_properties_dto_instance.to_dict()
# create an instance of DatasetPropertiesDTO from a dict
dataset_properties_dto_from_dict = DatasetPropertiesDTO.from_dict(dataset_properties_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


