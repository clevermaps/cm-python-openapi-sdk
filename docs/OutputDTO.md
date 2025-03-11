# OutputDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**format** | **str** |  | 
**filename** | **str** |  | [optional] 
**header** | **str** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.output_dto import OutputDTO

# TODO update the JSON string below
json = "{}"
# create an instance of OutputDTO from a JSON string
output_dto_instance = OutputDTO.from_json(json)
# print the JSON string representation of the object
print(OutputDTO.to_json())

# convert the object into a dict
output_dto_dict = output_dto_instance.to_dict()
# create an instance of OutputDTO from a dict
output_dto_from_dict = OutputDTO.from_dict(output_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


