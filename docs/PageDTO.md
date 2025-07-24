# PageDTO

define keys links and page that are mandatory for all pageble responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** |  | 
**total_elements** | **object** |  | 
**total_pages** | **int** |  | 
**number** | **int** |  | 

## Example

```python
from cm_python_openapi_sdk.models.page_dto import PageDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PageDTO from a JSON string
page_dto_instance = PageDTO.from_json(json)
# print the JSON string representation of the object
print(PageDTO.to_json())

# convert the object into a dict
page_dto_dict = page_dto_instance.to_dict()
# create an instance of PageDTO from a dict
page_dto_from_dict = PageDTO.from_dict(page_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


