# MaxValueDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zoom** | **int** |  | 
**var_global** | **float** |  | [optional] 
**selection** | **float** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.max_value_dto import MaxValueDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MaxValueDTO from a JSON string
max_value_dto_instance = MaxValueDTO.from_json(json)
# print the JSON string representation of the object
print(MaxValueDTO.to_json())

# convert the object into a dict
max_value_dto_dict = max_value_dto_instance.to_dict()
# create an instance of MaxValueDTO from a dict
max_value_dto_from_dict = MaxValueDTO.from_dict(max_value_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


