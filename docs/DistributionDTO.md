# DistributionDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**title** | **str** |  | [optional] 
**indicator** | **str** |  | [optional] 
**default_dataset** | **str** |  | [optional] 
**collapsed** | **bool** |  | [optional] 
**visualized** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.distribution_dto import DistributionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DistributionDTO from a JSON string
distribution_dto_instance = DistributionDTO.from_json(json)
# print the JSON string representation of the object
print(DistributionDTO.to_json())

# convert the object into a dict
distribution_dto_dict = distribution_dto_instance.to_dict()
# create an instance of DistributionDTO from a dict
distribution_dto_from_dict = DistributionDTO.from_dict(distribution_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


