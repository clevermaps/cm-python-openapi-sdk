# ImportProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force** | **bool** |  | 
**source_project_id** | **str** |  | 
**cascade_from** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**attribute_styles** | **bool** |  | [optional] [default to False]
**dashboard** | **bool** |  | [optional] [default to False]
**data_permissions** | **bool** |  | [optional] [default to False]
**datasets** | **bool** |  | [optional] [default to False]
**exports** | **bool** |  | [optional] [default to False]
**indicators** | **bool** |  | [optional] [default to False]
**indicator_drills** | **bool** |  | [optional] [default to False]
**maps** | **bool** |  | [optional] [default to False]
**markers** | **bool** |  | [optional] [default to False]
**marker_selectors** | **bool** |  | [optional] [default to False]
**metrics** | **bool** |  | [optional] [default to False]
**project_settings** | **bool** |  | [optional] [default to False]
**views** | **bool** |  | [optional] [default to False]
**skip_data** | **bool** |  | [optional] [default to False]

## Example

```python
from cm_python_openapi_sdk.models.import_project_request import ImportProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportProjectRequest from a JSON string
import_project_request_instance = ImportProjectRequest.from_json(json)
# print the JSON string representation of the object
print(ImportProjectRequest.to_json())

# convert the object into a dict
import_project_request_dict = import_project_request_instance.to_dict()
# create an instance of ImportProjectRequest from a dict
import_project_request_from_dict = ImportProjectRequest.from_dict(import_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


