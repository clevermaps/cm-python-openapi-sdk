# AuditLogPagedResourcePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_evaluated_key** | [**AuditLogPagedResourcePageLastEvaluatedKey**](AuditLogPagedResourcePageLastEvaluatedKey.md) |  | [optional] 
**size** | **int** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.audit_log_paged_resource_page import AuditLogPagedResourcePage

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogPagedResourcePage from a JSON string
audit_log_paged_resource_page_instance = AuditLogPagedResourcePage.from_json(json)
# print the JSON string representation of the object
print(AuditLogPagedResourcePage.to_json())

# convert the object into a dict
audit_log_paged_resource_page_dict = audit_log_paged_resource_page_instance.to_dict()
# create an instance of AuditLogPagedResourcePage from a dict
audit_log_paged_resource_page_from_dict = AuditLogPagedResourcePage.from_dict(audit_log_paged_resource_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


