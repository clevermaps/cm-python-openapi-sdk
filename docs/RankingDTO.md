# RankingDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**title** | **str** |  | [optional] 
**indicator** | **str** |  | [optional] 
**default_layer** | **str** |  | [optional] 
**feature_type** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**collapsed** | **bool** |  | [optional] 
**visualized** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.ranking_dto import RankingDTO

# TODO update the JSON string below
json = "{}"
# create an instance of RankingDTO from a JSON string
ranking_dto_instance = RankingDTO.from_json(json)
# print the JSON string representation of the object
print(RankingDTO.to_json())

# convert the object into a dict
ranking_dto_dict = ranking_dto_instance.to_dict()
# create an instance of RankingDTO from a dict
ranking_dto_from_dict = RankingDTO.from_dict(ranking_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


