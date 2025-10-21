# AuditLogSingleResource1


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
from cm_python_openapi_sdk.models.audit_log_single_resource1 import AuditLogSingleResource1

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogSingleResource1 from a JSON string
audit_log_single_resource1_instance = AuditLogSingleResource1.from_json(json)
# print the JSON string representation of the object
print(AuditLogSingleResource1.to_json())

# convert the object into a dict
audit_log_single_resource1_dict = audit_log_single_resource1_instance.to_dict()
# create an instance of AuditLogSingleResource1 from a dict
audit_log_single_resource1_from_dict = AuditLogSingleResource1.from_dict(audit_log_single_resource1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


