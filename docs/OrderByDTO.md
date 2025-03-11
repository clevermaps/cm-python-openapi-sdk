# OrderByDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** |  | 
**direction** | **str** |  | [default to 'asc']

## Example

```python
from cm_python_openapi_sdk.models.order_by_dto import OrderByDTO

# TODO update the JSON string below
json = "{}"
# create an instance of OrderByDTO from a JSON string
order_by_dto_instance = OrderByDTO.from_json(json)
# print the JSON string representation of the object
print(OrderByDTO.to_json())

# convert the object into a dict
order_by_dto_dict = order_by_dto_instance.to_dict()
# create an instance of OrderByDTO from a dict
order_by_dto_from_dict = OrderByDTO.from_dict(order_by_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


