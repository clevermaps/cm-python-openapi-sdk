# AvailableDatasetsResponseContentInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_id** | **str** |  | [optional] 
**available_datasets** | **List[object]** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.available_datasets_response_content_inner import AvailableDatasetsResponseContentInner

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableDatasetsResponseContentInner from a JSON string
available_datasets_response_content_inner_instance = AvailableDatasetsResponseContentInner.from_json(json)
# print the JSON string representation of the object
print(AvailableDatasetsResponseContentInner.to_json())

# convert the object into a dict
available_datasets_response_content_inner_dict = available_datasets_response_content_inner_instance.to_dict()
# create an instance of AvailableDatasetsResponseContentInner from a dict
available_datasets_response_content_inner_from_dict = AvailableDatasetsResponseContentInner.from_dict(available_datasets_response_content_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


