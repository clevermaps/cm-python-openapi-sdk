# ViewContentDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icon** | **str** |  | [optional] 
**dashboard** | **str** |  | 
**map** | **str** |  | [optional] 
**marker_selector** | **str** |  | [optional] 
**markers_only** | **bool** |  | [optional] 
**show_attributes_on_drill** | **bool** |  | [optional] 
**default_granularity** | **str** |  | [optional] 
**default_visualized** | **str** |  | [optional] 
**default_visualization** | **str** |  | [optional] 
**default_drilled** | **str** |  | [optional] 
**default_tool** | **str** |  | [optional] 
**default_compare_type** | **str** |  | [optional] 
**compare_collapsed** | **bool** |  | [optional] 
**filter_group** | [**List[FilterAbstractType]**](FilterAbstractType.md) |  | [optional] 
**default_active_filters** | [**List[ActiveFilterAbstractType]**](ActiveFilterAbstractType.md) |  | [optional] 
**variables** | [**List[VariablesDTO]**](VariablesDTO.md) |  | [optional] 
**spatial_query** | [**IsochroneDTO**](IsochroneDTO.md) |  | [optional] 
**fitness_groups** | **int** |  | [optional] 
**map_options** | [**MapOptionsDTO**](MapOptionsDTO.md) |  | [optional] 
**map_context_menu** | [**MapContextMenuDTO**](MapContextMenuDTO.md) |  | [optional] 
**exports** | [**List[ExportLinkDTO]**](ExportLinkDTO.md) |  | [optional] 
**measure** | [**MeasureDTO**](MeasureDTO.md) |  | [optional] 
**default_selected** | [**DefaultSelectedDTO**](DefaultSelectedDTO.md) |  | [optional] 
**exclude_datasets** | **List[str]** |  | [optional] 
**disable_fitness** | **bool** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.view_content_dto import ViewContentDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ViewContentDTO from a JSON string
view_content_dto_instance = ViewContentDTO.from_json(json)
# print the JSON string representation of the object
print(ViewContentDTO.to_json())

# convert the object into a dict
view_content_dto_dict = view_content_dto_instance.to_dict()
# create an instance of ViewContentDTO from a dict
view_content_dto_from_dict = ViewContentDTO.from_dict(view_content_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


