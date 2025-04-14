# SearchQueryHit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**SearchQueryHitId**](SearchQueryHitId.md) |  | 
**dataset** | **str** |  | 
**title** | **str** |  | 
**subtitle** | **str** |  | 
**highlight** | [**HitHighlight**](HitHighlight.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.search_query_hit import SearchQueryHit

# TODO update the JSON string below
json = "{}"
# create an instance of SearchQueryHit from a JSON string
search_query_hit_instance = SearchQueryHit.from_json(json)
# print the JSON string representation of the object
print(SearchQueryHit.to_json())

# convert the object into a dict
search_query_hit_dict = search_query_hit_instance.to_dict()
# create an instance of SearchQueryHit from a dict
search_query_hit_from_dict = SearchQueryHit.from_dict(search_query_hit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


