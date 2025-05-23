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

from cm_python_openapi_sdk.models.dataset_type import DatasetType

class TestDatasetType(unittest.TestCase):
    """DatasetType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatasetType:
        """Test DatasetType
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatasetType`
        """
        model = DatasetType()
        if include_optional:
            return DatasetType(
                type = 'dwh',
                subtype = 'geometryPolygon',
                geometry = '0',
                h3_geometries = [
                    'awat5ikwowtta-3mh2lcafqw3zhes'
                    ],
                visualizations = [
                    {zoom={min=3, optimal=11, max=4, visibleFrom=11}, type=areas}
                    ],
                table = 'awat5ikwowtta-3mh2lcafqw3zhes',
                geometry_table = 'awat5ikwowtta-3mh2lcafqw3zhes',
                primary_key = 'awat5ikwowtta-3mh2lcafqw3zhes',
                categorizable = True,
                full_text_index = True,
                spatial_index = True,
                properties = [
                    {filterable=true, name=name, column=column, description=description, title=title, type=type, calculated=true, displayOptions={valueOptions=[{hexColor=hexColor, color=purple, pattern=solid, weight=5.637376656633329, value=}, {hexColor=hexColor, color=purple, pattern=solid, weight=5.637376656633329, value=}]}}
                    ],
                zoom = {min=3, optimal=11, max=4, visibleFrom=11},
                url_template = '',
                resolution = 2
            )
        else:
            return DatasetType(
                type = 'dwh',
                subtype = 'geometryPolygon',
                primary_key = 'awat5ikwowtta-3mh2lcafqw3zhes',
                properties = [
                    {filterable=true, name=name, column=column, description=description, title=title, type=type, calculated=true, displayOptions={valueOptions=[{hexColor=hexColor, color=purple, pattern=solid, weight=5.637376656633329, value=}, {hexColor=hexColor, color=purple, pattern=solid, weight=5.637376656633329, value=}]}}
                    ],
                url_template = '',
                resolution = 2,
        )
        """

    def testDatasetType(self):
        """Test DatasetType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
