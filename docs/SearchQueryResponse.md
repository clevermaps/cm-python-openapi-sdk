# SearchQueryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[SearchQueryHit]**](SearchQueryHit.md) |  | 
**links** | **List[object]** |  | 
**page** | [**PageDTO**](PageDTO.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.search_query_response import SearchQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchQueryResponse from a JSON string
search_query_response_instance = SearchQueryResponse.from_json(json)
# print the JSON string representation of the object
print(SearchQueryResponse.to_json())

# convert the object into a dict
search_query_response_dict = search_query_response_instance.to_dict()
# create an instance of SearchQueryResponse from a dict
search_query_response_from_dict = SearchQueryResponse.from_dict(search_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


