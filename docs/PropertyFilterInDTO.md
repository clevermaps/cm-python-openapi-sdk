# PropertyFilterInDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_name** | **str** |  | 
**value** | **List[object]** |  | [optional] 
**operator** | **str** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.property_filter_in_dto import PropertyFilterInDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyFilterInDTO from a JSON string
property_filter_in_dto_instance = PropertyFilterInDTO.from_json(json)
# print the JSON string representation of the object
print(PropertyFilterInDTO.to_json())

# convert the object into a dict
property_filter_in_dto_dict = property_filter_in_dto_instance.to_dict()
# create an instance of PropertyFilterInDTO from a dict
property_filter_in_dto_from_dict = PropertyFilterInDTO.from_dict(property_filter_in_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


