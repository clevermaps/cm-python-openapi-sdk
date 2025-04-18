# coding: utf-8

"""
    clevermaps-client

    CleverMaps REST API provides access to location intelligence and geospatial analytics platform.  ### Main capabilities include: - Project and user access management - Multidimensional data model and metrics management - Data upload and exports - Ad-hoc analysis of geospatial data - Full text and geographic search - Configuration of CleverMaps Studio visualizations 

    The version of the OpenAPI document: 1.0.0
    Contact: support@clevermaps.io
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
                    {variables=[{minValue=0.8008281904610115, maxValue=6.027456183070403, defaultValue=1.4658129805029452, name=name, format={symbol=symbol, type=number, fraction=0}, title=title}, {minValue=0.8008281904610115, maxValue=6.027456183070403, defaultValue=1.4658129805029452, name=name, format={symbol=symbol, type=number, fraction=0}, title=title}], type=type, title=title}
                    ],
                spatial_query = {unit=time, amount=1, lng=22.945559638799807, profile=car, geometry={}, lat=34.63682100059455},
                fitness_groups = 3,
                map_options = {maxZoom=2, customTileLayer={accessToken=accessToken, url=url}, tileLayer=mapbox, center={lng=6.027456183070403, lat=0.8008281904610115}, tileLayerMenu=true, minZoom=0, zoom=9},
                map_context_menu = {items=[{type=googleSatellite}, {type=googleSatellite}]},
                exports = [
                    {export=export}
                    ],
                measure = {type=line, zones=[{unit=time, amount=1, lng=22.945559638799807, profile=car, geometry={}, lat=34.63682100059455}, {unit=time, amount=1, lng=22.945559638799807, profile=car, geometry={}, lat=34.63682100059455}], points=[{unit=time, amount=1, lng=22.945559638799807, profile=car, geometry={}, lat=34.63682100059455}, {unit=time, amount=1, lng=22.945559638799807, profile=car, geometry={}, lat=34.63682100059455}]},
                default_selected = {coordinates=[{lng=6.027456183070403, lat=0.8008281904610115}, {lng=6.027456183070403, lat=0.8008281904610115}], ids=[, ], dataset=dataset},
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
