# RelationsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [default to 'self']
**reversed_metric** | **str** |  | 

## Example

```python
from openapi_client.models.relations_dto import RelationsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of RelationsDTO from a JSON string
relations_dto_instance = RelationsDTO.from_json(json)
# print the JSON string representation of the object
print(RelationsDTO.to_json())

# convert the object into a dict
relations_dto_dict = relations_dto_instance.to_dict()
# create an instance of RelationsDTO from a dict
relations_dto_from_dict = RelationsDTO.from_dict(relations_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


