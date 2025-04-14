# DateRangeFunctionFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**content** | [**List[DwhQueryNumberType]**](DwhQueryNumberType.md) |  | 
**options** | [**FunctionDateTruncateOptions**](FunctionDateTruncateOptions.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.date_range_function_function import DateRangeFunctionFunction

# TODO update the JSON string below
json = "{}"
# create an instance of DateRangeFunctionFunction from a JSON string
date_range_function_function_instance = DateRangeFunctionFunction.from_json(json)
# print the JSON string representation of the object
print(DateRangeFunctionFunction.to_json())

# convert the object into a dict
date_range_function_function_dict = date_range_function_function_instance.to_dict()
# create an instance of DateRangeFunctionFunction from a dict
date_range_function_function_from_dict = DateRangeFunctionFunction.from_dict(date_range_function_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


