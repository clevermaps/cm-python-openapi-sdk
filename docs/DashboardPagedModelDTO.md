# DashboardPagedModelDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[DashboardDTO]**](DashboardDTO.md) |  | [optional] 
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 
**page** | [**MandatoryKeysForPagableResponse**](MandatoryKeysForPagableResponse.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.dashboard_paged_model_dto import DashboardPagedModelDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardPagedModelDTO from a JSON string
dashboard_paged_model_dto_instance = DashboardPagedModelDTO.from_json(json)
# print the JSON string representation of the object
print(DashboardPagedModelDTO.to_json())

# convert the object into a dict
dashboard_paged_model_dto_dict = dashboard_paged_model_dto_instance.to_dict()
# create an instance of DashboardPagedModelDTO from a dict
dashboard_paged_model_dto_from_dict = DashboardPagedModelDTO.from_dict(dashboard_paged_model_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


