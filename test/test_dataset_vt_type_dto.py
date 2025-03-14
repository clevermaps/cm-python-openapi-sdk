# coding: utf-8

"""
    clevermaps-client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cm_python_openapi_sdk.models.dataset_vt_type_dto import DatasetVtTypeDTO

class TestDatasetVtTypeDTO(unittest.TestCase):
    """DatasetVtTypeDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatasetVtTypeDTO:
        """Test DatasetVtTypeDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatasetVtTypeDTO`
        """
        model = DatasetVtTypeDTO()
        if include_optional:
            return DatasetVtTypeDTO(
                type = 'vt',
                url_template = '',
                zoom = cm_python_openapi_sdk.models.zoom_dto.ZoomDTO(
                    min = 2, 
                    optimal = 2, 
                    max = 2, 
                    visible_from = 2, )
            )
        else:
            return DatasetVtTypeDTO(
                type = 'vt',
                url_template = '',
        )
        """

    def testDatasetVtTypeDTO(self):
        """Test DatasetVtTypeDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
