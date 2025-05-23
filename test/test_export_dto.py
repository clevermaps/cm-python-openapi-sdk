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

from cm_python_openapi_sdk.models.export_dto import ExportDTO

class TestExportDTO(unittest.TestCase):
    """ExportDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExportDTO:
        """Test ExportDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExportDTO`
        """
        model = ExportDTO()
        if include_optional:
            return ExportDTO(
                id = '',
                name = 'awat5ikwowtta-3mh2lcafqw3zhes',
                type = 'dataset',
                title = '0',
                description = '',
                content = {output={filename=filename, format=csv, header=basic, type=file}, properties=[properties, properties]}
            )
        else:
            return ExportDTO(
                name = 'awat5ikwowtta-3mh2lcafqw3zhes',
                content = {output={filename=filename, format=csv, header=basic, type=file}, properties=[properties, properties]},
        )
        """

    def testExportDTO(self):
        """Test ExportDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
