# coding: utf-8

"""
    clevermaps-client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cm_python_openapi_sdk.models.dataset_dwh_type_dto import DatasetDwhTypeDTO

class TestDatasetDwhTypeDTO(unittest.TestCase):
    """DatasetDwhTypeDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatasetDwhTypeDTO:
        """Test DatasetDwhTypeDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatasetDwhTypeDTO`
        """
        model = DatasetDwhTypeDTO()
        if include_optional:
            return DatasetDwhTypeDTO(
                type = 'dwh',
                subtype = 'geometryPolygon',
                geometry = '0',
                h3_geometries = [
                    'awat5ikwowtta-3mh2lcafqw3zhes'
                    ],
                visualizations = [
                    cm_python_openapi_sdk.models.dataset_visualization_dto.DatasetVisualizationDTO(
                        type = 'areas', 
                        zoom = cm_python_openapi_sdk.models.zoom_dto.ZoomDTO(
                            min = 2, 
                            optimal = 2, 
                            max = 2, 
                            visible_from = 2, ), )
                    ],
                table = 'awat5ikwowtta-3mh2lcafqw3zhes',
                geometry_table = 'awat5ikwowtta-3mh2lcafqw3zhes',
                primary_key = 'awat5ikwowtta-3mh2lcafqw3zhes',
                categorizable = True,
                full_text_index = True,
                spatial_index = True,
                properties = [
                    null
                    ],
                zoom = cm_python_openapi_sdk.models.zoom_dto.ZoomDTO(
                    min = 2, 
                    optimal = 2, 
                    max = 2, 
                    visible_from = 2, )
            )
        else:
            return DatasetDwhTypeDTO(
                type = 'dwh',
                subtype = 'geometryPolygon',
                primary_key = 'awat5ikwowtta-3mh2lcafqw3zhes',
                properties = [
                    null
                    ],
        )
        """

    def testDatasetDwhTypeDTO(self):
        """Test DatasetDwhTypeDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
