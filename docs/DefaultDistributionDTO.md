# DefaultDistributionDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | **List[float]** |  | [optional] 
**breaks** | **List[float]** |  | [optional] 
**display_intervals** | **List[float]** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.default_distribution_dto import DefaultDistributionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultDistributionDTO from a JSON string
default_distribution_dto_instance = DefaultDistributionDTO.from_json(json)
# print the JSON string representation of the object
print(DefaultDistributionDTO.to_json())

# convert the object into a dict
default_distribution_dto_dict = default_distribution_dto_instance.to_dict()
# create an instance of DefaultDistributionDTO from a dict
default_distribution_dto_from_dict = DefaultDistributionDTO.from_dict(default_distribution_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


