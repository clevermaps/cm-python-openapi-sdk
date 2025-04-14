# AvailableDatasetsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | [**List[DwhQueryPropertyTypes]**](DwhQueryPropertyTypes.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.available_datasets_request import AvailableDatasetsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableDatasetsRequest from a JSON string
available_datasets_request_instance = AvailableDatasetsRequest.from_json(json)
# print the JSON string representation of the object
print(AvailableDatasetsRequest.to_json())

# convert the object into a dict
available_datasets_request_dict = available_datasets_request_instance.to_dict()
# create an instance of AvailableDatasetsRequest from a dict
available_datasets_request_from_dict = AvailableDatasetsRequest.from_dict(available_datasets_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


