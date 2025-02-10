# ScaleOptionsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**static** | [**List[StaticScaleOptionDTO]**](StaticScaleOptionDTO.md) |  | [optional] 
**default_distribution** | [**DefaultDistributionDTO**](DefaultDistributionDTO.md) |  | [optional] 

## Example

```python
from openapi_client.models.scale_options_dto import ScaleOptionsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ScaleOptionsDTO from a JSON string
scale_options_dto_instance = ScaleOptionsDTO.from_json(json)
# print the JSON string representation of the object
print(ScaleOptionsDTO.to_json())

# convert the object into a dict
scale_options_dto_dict = scale_options_dto_instance.to_dict()
# create an instance of ScaleOptionsDTO from a dict
scale_options_dto_from_dict = ScaleOptionsDTO.from_dict(scale_options_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


