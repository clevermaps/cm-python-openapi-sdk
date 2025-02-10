# MandatoryKeysForPagableResponse

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
from openapi_client.models.mandatory_keys_for_pagable_response import MandatoryKeysForPagableResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MandatoryKeysForPagableResponse from a JSON string
mandatory_keys_for_pagable_response_instance = MandatoryKeysForPagableResponse.from_json(json)
# print the JSON string representation of the object
print(MandatoryKeysForPagableResponse.to_json())

# convert the object into a dict
mandatory_keys_for_pagable_response_dict = mandatory_keys_for_pagable_response_instance.to_dict()
# create an instance of MandatoryKeysForPagableResponse from a dict
mandatory_keys_for_pagable_response_from_dict = MandatoryKeysForPagableResponse.from_dict(mandatory_keys_for_pagable_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


