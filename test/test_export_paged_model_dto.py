# coding: utf-8

"""
    clevermaps-client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cm_python_openapi_sdk.models.export_paged_model_dto import ExportPagedModelDTO

class TestExportPagedModelDTO(unittest.TestCase):
    """ExportPagedModelDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExportPagedModelDTO:
        """Test ExportPagedModelDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExportPagedModelDTO`
        """
        model = ExportPagedModelDTO()
        if include_optional:
            return ExportPagedModelDTO(
                content = [
                    cm_python_openapi_sdk.models.export_dto.ExportDTO(
                        id = '', 
                        name = 'awat5ikwowtta-3mh2lcafqw3zhes', 
                        type = 'dataset', 
                        title = '0', 
                        description = '', 
                        content = cm_python_openapi_sdk.models.export_content_dto.ExportContentDTO(
                            properties = [
                                'awat5ikwowtta-3mh2lcafqw3zhes.i16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwscq-4zge8f37mn0'
                                ], 
                            output = cm_python_openapi_sdk.models.output_dto.OutputDTO(
                                type = 'file', 
                                format = 'csv', 
                                filename = '26bUUGjjNSwg0_bs9ZayIMhcsv', 
                                header = 'basic', ), ), )
                    ],
                links = [
                    None
                    ],
                page = cm_python_openapi_sdk.models.mandatory_keys_for_pagable_response.mandatory keys for pagable response(
                    size = 56, 
                    total_elements = null, 
                    total_pages = 56, 
                    number = 56, )
            )
        else:
            return ExportPagedModelDTO(
        )
        """

    def testExportPagedModelDTO(self):
        """Test ExportPagedModelDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
