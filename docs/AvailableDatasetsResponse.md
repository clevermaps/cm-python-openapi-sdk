# AvailableDatasetsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[AvailableDatasetsResponseContentInner]**](AvailableDatasetsResponseContentInner.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.available_datasets_response import AvailableDatasetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableDatasetsResponse from a JSON string
available_datasets_response_instance = AvailableDatasetsResponse.from_json(json)
# print the JSON string representation of the object
print(AvailableDatasetsResponse.to_json())

# convert the object into a dict
available_datasets_response_dict = available_datasets_response_instance.to_dict()
# create an instance of AvailableDatasetsResponse from a dict
available_datasets_response_from_dict = AvailableDatasetsResponse.from_dict(available_datasets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


