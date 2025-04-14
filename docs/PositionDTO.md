# PositionDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** |  | 
**lng** | **float** |  | 

## Example

```python
from cm_python_openapi_sdk.models.position_dto import PositionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PositionDTO from a JSON string
position_dto_instance = PositionDTO.from_json(json)
# print the JSON string representation of the object
print(PositionDTO.to_json())

# convert the object into a dict
position_dto_dict = position_dto_instance.to_dict()
# create an instance of PositionDTO from a dict
position_dto_from_dict = PositionDTO.from_dict(position_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


