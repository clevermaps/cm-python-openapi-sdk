# coding: utf-8

"""
    clevermaps-client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cm_python_openapi_sdk.models.indicator_drill_dto import IndicatorDrillDTO

class TestIndicatorDrillDTO(unittest.TestCase):
    """IndicatorDrillDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IndicatorDrillDTO:
        """Test IndicatorDrillDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IndicatorDrillDTO`
        """
        model = IndicatorDrillDTO()
        if include_optional:
            return IndicatorDrillDTO(
                id = '',
                name = 'awat5ikwowtta-3mh2lcafqw3zhes',
                type = 'dataset',
                title = '0',
                description = '',
                content = cm_python_openapi_sdk.models.indicator_drill_content_dto.IndicatorDrillContentDTO(
                    blocks = [
                        null
                        ], )
            )
        else:
            return IndicatorDrillDTO(
                name = 'awat5ikwowtta-3mh2lcafqw3zhes',
                content = cm_python_openapi_sdk.models.indicator_drill_content_dto.IndicatorDrillContentDTO(
                    blocks = [
                        null
                        ], ),
        )
        """

    def testIndicatorDrillDTO(self):
        """Test IndicatorDrillDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
