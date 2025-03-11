# MetricDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | [**DwhQueryFunctionTypes**](DwhQueryFunctionTypes.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.metric_dto import MetricDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MetricDTO from a JSON string
metric_dto_instance = MetricDTO.from_json(json)
# print the JSON string representation of the object
print(MetricDTO.to_json())

# convert the object into a dict
metric_dto_dict = metric_dto_instance.to_dict()
# create an instance of MetricDTO from a dict
metric_dto_from_dict = MetricDTO.from_dict(metric_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


