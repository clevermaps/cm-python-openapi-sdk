# BoundingBoxDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_x** | **float** |  | [optional] 
**min_y** | **float** |  | [optional] 
**max_x** | **float** |  | [optional] 
**max_y** | **float** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.bounding_box_dto import BoundingBoxDTO

# TODO update the JSON string below
json = "{}"
# create an instance of BoundingBoxDTO from a JSON string
bounding_box_dto_instance = BoundingBoxDTO.from_json(json)
# print the JSON string representation of the object
print(BoundingBoxDTO.to_json())

# convert the object into a dict
bounding_box_dto_dict = bounding_box_dto_instance.to_dict()
# create an instance of BoundingBoxDTO from a dict
bounding_box_dto_from_dict = BoundingBoxDTO.from_dict(bounding_box_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


