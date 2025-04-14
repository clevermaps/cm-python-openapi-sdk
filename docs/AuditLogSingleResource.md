# AuditLogSingleResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** |  | 
**account_id** | **str** |  | 
**request_id** | **str** |  | [optional] 
**remote_host** | **str** |  | [optional] 
**project_id** | **str** |  | 
**event_type** | **str** |  | 
**timestamp** | **str** |  | 
**content** | **object** |  | 
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | 

## Example

```python
from cm_python_openapi_sdk.models.audit_log_single_resource import AuditLogSingleResource

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogSingleResource from a JSON string
audit_log_single_resource_instance = AuditLogSingleResource.from_json(json)
# print the JSON string representation of the object
print(AuditLogSingleResource.to_json())

# convert the object into a dict
audit_log_single_resource_dict = audit_log_single_resource_instance.to_dict()
# create an instance of AuditLogSingleResource from a dict
audit_log_single_resource_from_dict = AuditLogSingleResource.from_dict(audit_log_single_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


