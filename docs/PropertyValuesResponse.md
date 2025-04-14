# PropertyValuesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[PropertyValuesResponseContentInner]**](PropertyValuesResponseContentInner.md) |  | 
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | 
**page** | [**MandatoryKeysForPagableResponse**](MandatoryKeysForPagableResponse.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.property_values_response import PropertyValuesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyValuesResponse from a JSON string
property_values_response_instance = PropertyValuesResponse.from_json(json)
# print the JSON string representation of the object
print(PropertyValuesResponse.to_json())

# convert the object into a dict
property_values_response_dict = property_values_response_instance.to_dict()
# create an instance of PropertyValuesResponse from a dict
property_values_response_from_dict = PropertyValuesResponse.from_dict(property_values_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


