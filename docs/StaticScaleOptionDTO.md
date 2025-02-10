# StaticScaleOptionDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | [optional] 
**breaks** | [**StaticScaleOptionDTOBreaks**](StaticScaleOptionDTOBreaks.md) |  | 
**max_values** | [**List[MaxValueDTO]**](MaxValueDTO.md) |  | [optional] 

## Example

```python
from openapi_client.models.static_scale_option_dto import StaticScaleOptionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of StaticScaleOptionDTO from a JSON string
static_scale_option_dto_instance = StaticScaleOptionDTO.from_json(json)
# print the JSON string representation of the object
print(StaticScaleOptionDTO.to_json())

# convert the object into a dict
static_scale_option_dto_dict = static_scale_option_dto_instance.to_dict()
# create an instance of StaticScaleOptionDTO from a dict
static_scale_option_dto_from_dict = StaticScaleOptionDTO.from_dict(static_scale_option_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


