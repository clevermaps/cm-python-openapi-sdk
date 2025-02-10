# BlockRowDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**blocks** | [**List[IndicatorLinkDTO]**](IndicatorLinkDTO.md) |  | 

## Example

```python
from openapi_client.models.block_row_dto import BlockRowDTO

# TODO update the JSON string below
json = "{}"
# create an instance of BlockRowDTO from a JSON string
block_row_dto_instance = BlockRowDTO.from_json(json)
# print the JSON string representation of the object
print(BlockRowDTO.to_json())

# convert the object into a dict
block_row_dto_dict = block_row_dto_instance.to_dict()
# create an instance of BlockRowDTO from a dict
block_row_dto_from_dict = BlockRowDTO.from_dict(block_row_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


