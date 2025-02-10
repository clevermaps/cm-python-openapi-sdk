# DashboardDatasetPropertiesDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | 
**default_search** | **str** |  | [optional] 
**feature_attributes** | [**List[FeatureAttributeDTO]**](FeatureAttributeDTO.md) |  | 

## Example

```python
from openapi_client.models.dashboard_dataset_properties_dto import DashboardDatasetPropertiesDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardDatasetPropertiesDTO from a JSON string
dashboard_dataset_properties_dto_instance = DashboardDatasetPropertiesDTO.from_json(json)
# print the JSON string representation of the object
print(DashboardDatasetPropertiesDTO.to_json())

# convert the object into a dict
dashboard_dataset_properties_dto_dict = dashboard_dataset_properties_dto_instance.to_dict()
# create an instance of DashboardDatasetPropertiesDTO from a dict
dashboard_dataset_properties_dto_from_dict = DashboardDatasetPropertiesDTO.from_dict(dashboard_dataset_properties_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


