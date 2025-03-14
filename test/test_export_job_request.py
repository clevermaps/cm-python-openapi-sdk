# coding: utf-8

"""
    clevermaps-client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cm_python_openapi_sdk.models.export_job_request import ExportJobRequest

class TestExportJobRequest(unittest.TestCase):
    """ExportJobRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExportJobRequest:
        """Test ExportJobRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExportJobRequest`
        """
        model = ExportJobRequest()
        if include_optional:
            return ExportJobRequest(
                type = 'E',
                project_id = 'w8q6zgckec0l3o4g',
                content = cm_python_openapi_sdk.models.export_request.ExportRequest(
                    format = 'csv', 
                    csv_header_format = 'basic', 
                    query = cm_python_openapi_sdk.models.query.query(), 
                    csv_options = cm_python_openapi_sdk.models.export_request_csv_options.ExportRequest_csvOptions(
                        header = True, 
                        separator = '', 
                        quote = '', 
                        escape = '', ), 
                    xlsx_options = cm_python_openapi_sdk.models.xlsx_options.xlsxOptions(), )
            )
        else:
            return ExportJobRequest(
                type = 'E',
                project_id = 'w8q6zgckec0l3o4g',
                content = cm_python_openapi_sdk.models.export_request.ExportRequest(
                    format = 'csv', 
                    csv_header_format = 'basic', 
                    query = cm_python_openapi_sdk.models.query.query(), 
                    csv_options = cm_python_openapi_sdk.models.export_request_csv_options.ExportRequest_csvOptions(
                        header = True, 
                        separator = '', 
                        quote = '', 
                        escape = '', ), 
                    xlsx_options = cm_python_openapi_sdk.models.xlsx_options.xlsxOptions(), ),
        )
        """

    def testExportJobRequest(self):
        """Test ExportJobRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
