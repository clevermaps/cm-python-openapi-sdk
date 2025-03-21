# coding: utf-8

"""
    clevermaps-client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cm_python_openapi_sdk.models.view_content_dto import ViewContentDTO

class TestViewContentDTO(unittest.TestCase):
    """ViewContentDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ViewContentDTO:
        """Test ViewContentDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ViewContentDTO`
        """
        model = ViewContentDTO()
        if include_optional:
            return ViewContentDTO(
                icon = 'q',
                dashboard = '/rest/projects/8q6zgckec0l3o4gi/md/dashboards?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc',
                map = '/rest/projects/8q6zgckec0l3o4gi/md/maps?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc',
                marker_selector = '/rest/projects/8q6zgckec0l3o4gi/md/markerSelectors?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc',
                markers_only = True,
                show_attributes_on_drill = True,
                default_granularity = '/rest/projects/8q6zgckec0l3o4gi/md/datasets?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc',
                default_visualized = '/rest/projects/8q6zgckec0l3o4gi/md/indicators?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc',
                default_visualization = 'areas',
                default_drilled = '/rest/projects/8q6zgckec0l3o4gi/md/indicators?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc',
                default_tool = 'search',
                default_compare_type = 'dominance',
                compare_collapsed = True,
                filter_group = [
                    null
                    ],
                default_active_filters = [
                    null
                    ],
                variables = [
                    cm_python_openapi_sdk.models.variables_dto.VariablesDTO(
                        type = 'variables', 
                        title = '0', 
                        variables = [
                            cm_python_openapi_sdk.models.variable_dto.VariableDTO(
                                name = 'awat5ikwowtta-3mh2lcafqw3zhes', 
                                title = '0', 
                                min_value = 1.337, 
                                max_value = 1.337, 
                                default_value = 1.337, 
                                format = cm_python_openapi_sdk.models.format_dto.FormatDTO(
                                    type = 'number', 
                                    fraction = 0, 
                                    symbol = '', ), )
                            ], )
                    ],
                spatial_query = cm_python_openapi_sdk.models.isochrone_dto.IsochroneDTO(
                    lat = -180.0, 
                    lng = -180.0, 
                    profile = 'car', 
                    unit = 'time', 
                    amount = 1, 
                    geometry = cm_python_openapi_sdk.models.geometry.geometry(), ),
                fitness_groups = 3,
                map_options = cm_python_openapi_sdk.models.map_options_dto.MapOptionsDTO(
                    center = cm_python_openapi_sdk.models.center_dto.CenterDTO(
                        lat = 1.337, 
                        lng = 1.337, ), 
                    zoom = 56, 
                    min_zoom = 0, 
                    max_zoom = 56, 
                    tile_layer_menu = True, 
                    tile_layer = 'mapbox', 
                    custom_tile_layer = cm_python_openapi_sdk.models.map_options_dto_custom_tile_layer.MapOptionsDTO_customTileLayer(
                        url = 'mapbox://styles/jUR,rZ#UM/?R,Fp^l6$ARj', 
                        access_token = '0', ), ),
                map_context_menu = cm_python_openapi_sdk.models.map_context_menu_dto.MapContextMenuDTO(
                    items = [
                        null
                        ], ),
                exports = [
                    cm_python_openapi_sdk.models.export_link_dto.ExportLinkDTO(
                        export = '/rest/projects/8q6zgckec0l3o4gi/md/exports?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc', )
                    ],
                measure = cm_python_openapi_sdk.models.measure_dto.MeasureDTO(
                    type = 'line', 
                    points = [
                        cm_python_openapi_sdk.models.isochrone_dto.IsochroneDTO(
                            lat = -180.0, 
                            lng = -180.0, 
                            profile = 'car', 
                            unit = 'time', 
                            amount = 1, 
                            geometry = cm_python_openapi_sdk.models.geometry.geometry(), )
                        ], 
                    zones = [
                        cm_python_openapi_sdk.models.isochrone_dto.IsochroneDTO(
                            lat = -180.0, 
                            lng = -180.0, 
                            profile = 'car', 
                            unit = 'time', 
                            amount = 1, 
                            geometry = cm_python_openapi_sdk.models.geometry.geometry(), )
                        ], ),
                default_selected = cm_python_openapi_sdk.models.default_selected_dto.DefaultSelectedDTO(
                    dataset = '/rest/projects/8q6zgckec0l3o4gi/md/datasets?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc', 
                    ids = [
                        null
                        ], 
                    coordinates = [
                        cm_python_openapi_sdk.models.center_dto.CenterDTO(
                            lat = 1.337, 
                            lng = 1.337, )
                        ], ),
                exclude_datasets = [
                    ''
                    ],
                disable_fitness = True
            )
        else:
            return ViewContentDTO(
                dashboard = '/rest/projects/8q6zgckec0l3o4gi/md/dashboards?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc',
        )
        """

    def testViewContentDTO(self):
        """Test ViewContentDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
