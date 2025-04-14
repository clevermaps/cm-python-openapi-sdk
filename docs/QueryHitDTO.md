# QueryHitDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**subtitle** | **str** |  | 
**highlight** | [**HighlightDTO**](HighlightDTO.md) |  | [optional] 
**position** | [**PositionDTO**](PositionDTO.md) |  | 
**bounding_box** | [**BoundingBoxDTO**](BoundingBoxDTO.md) |  | [optional] 
**place_type** | **str** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.query_hit_dto import QueryHitDTO

# TODO update the JSON string below
json = "{}"
# create an instance of QueryHitDTO from a JSON string
query_hit_dto_instance = QueryHitDTO.from_json(json)
# print the JSON string representation of the object
print(QueryHitDTO.to_json())

# convert the object into a dict
query_hit_dto_dict = query_hit_dto_instance.to_dict()
# create an instance of QueryHitDTO from a dict
query_hit_dto_from_dict = QueryHitDTO.from_dict(query_hit_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


