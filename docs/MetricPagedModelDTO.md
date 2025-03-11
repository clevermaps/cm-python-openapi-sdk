# MetricPagedModelDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[MetricDTO]**](MetricDTO.md) |  | [optional] 
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 
**page** | [**MandatoryKeysForPagableResponse**](MandatoryKeysForPagableResponse.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.metric_paged_model_dto import MetricPagedModelDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MetricPagedModelDTO from a JSON string
metric_paged_model_dto_instance = MetricPagedModelDTO.from_json(json)
# print the JSON string representation of the object
print(MetricPagedModelDTO.to_json())

# convert the object into a dict
metric_paged_model_dto_dict = metric_paged_model_dto_instance.to_dict()
# create an instance of MetricPagedModelDTO from a dict
metric_paged_model_dto_from_dict = MetricPagedModelDTO.from_dict(metric_paged_model_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


