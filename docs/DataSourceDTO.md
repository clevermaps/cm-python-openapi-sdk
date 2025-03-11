# DataSourceDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**licence_holder** | **str** |  | 
**licence_holder_url** | **str** |  | 
**licence_holder_logo** | **str** |  | [optional] 
**licence_url** | **str** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.data_source_dto import DataSourceDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourceDTO from a JSON string
data_source_dto_instance = DataSourceDTO.from_json(json)
# print the JSON string representation of the object
print(DataSourceDTO.to_json())

# convert the object into a dict
data_source_dto_dict = data_source_dto_instance.to_dict()
# create an instance of DataSourceDTO from a dict
data_source_dto_from_dict = DataSourceDTO.from_dict(data_source_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


