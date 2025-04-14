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

from cm_python_openapi_sdk.models.export_request import ExportRequest

class TestExportRequest(unittest.TestCase):
    """ExportRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExportRequest:
        """Test ExportRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExportRequest`
        """
        model = ExportRequest()
        if include_optional:
            return ExportRequest(
                format = 'csv',
                csv_header_format = 'basic',
                query = cm_python_openapi_sdk.models.query.query(),
                csv_options = cm_python_openapi_sdk.models.export_request_csv_options.ExportRequest_csvOptions(
                    header = True, 
                    separator = '', 
                    quote = '', 
                    escape = '', ),
                xlsx_options = cm_python_openapi_sdk.models.xlsx_options.xlsxOptions()
            )
        else:
            return ExportRequest(
                format = 'csv',
                query = cm_python_openapi_sdk.models.query.query(),
        )
        """

    def testExportRequest(self):
        """Test ExportRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
