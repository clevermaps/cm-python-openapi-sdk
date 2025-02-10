# DashboardContentDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_rows** | [**List[BlockRowAbstractType]**](BlockRowAbstractType.md) |  | [optional] 
**dataset_properties** | [**List[DashboardDatasetPropertiesDTO]**](DashboardDatasetPropertiesDTO.md) |  | [optional] 

## Example

```python
from openapi_client.models.dashboard_content_dto import DashboardContentDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardContentDTO from a JSON string
dashboard_content_dto_instance = DashboardContentDTO.from_json(json)
# print the JSON string representation of the object
print(DashboardContentDTO.to_json())

# convert the object into a dict
dashboard_content_dto_dict = dashboard_content_dto_instance.to_dict()
# create an instance of DashboardContentDTO from a dict
dashboard_content_dto_from_dict = DashboardContentDTO.from_dict(dashboard_content_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


