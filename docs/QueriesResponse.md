# QueriesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_detail** | [**ExecutionDetail**](ExecutionDetail.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.queries_response import QueriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueriesResponse from a JSON string
queries_response_instance = QueriesResponse.from_json(json)
# print the JSON string representation of the object
print(QueriesResponse.to_json())

# convert the object into a dict
queries_response_dict = queries_response_instance.to_dict()
# create an instance of QueriesResponse from a dict
queries_response_from_dict = QueriesResponse.from_dict(queries_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


