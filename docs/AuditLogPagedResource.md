# AuditLogPagedResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | 
**content** | [**List[AuditLogSingleResource]**](AuditLogSingleResource.md) |  | 
**page** | [**AuditLogPagedResourcePage**](AuditLogPagedResourcePage.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.audit_log_paged_resource import AuditLogPagedResource

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogPagedResource from a JSON string
audit_log_paged_resource_instance = AuditLogPagedResource.from_json(json)
# print the JSON string representation of the object
print(AuditLogPagedResource.to_json())

# convert the object into a dict
audit_log_paged_resource_dict = audit_log_paged_resource_instance.to_dict()
# create an instance of AuditLogPagedResource from a dict
audit_log_paged_resource_from_dict = AuditLogPagedResource.from_dict(audit_log_paged_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


