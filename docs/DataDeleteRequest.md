# DataDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasets** | [**List[DatasetDeleteSpec]**](DatasetDeleteSpec.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.data_delete_request import DataDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DataDeleteRequest from a JSON string
data_delete_request_instance = DataDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(DataDeleteRequest.to_json())

# convert the object into a dict
data_delete_request_dict = data_delete_request_instance.to_dict()
# create an instance of DataDeleteRequest from a dict
data_delete_request_from_dict = DataDeleteRequest.from_dict(data_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


