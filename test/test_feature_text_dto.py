# coding: utf-8

"""
    clevermaps-client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cm_python_openapi_sdk.models.feature_text_dto import FeatureTextDTO

class TestFeatureTextDTO(unittest.TestCase):
    """FeatureTextDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FeatureTextDTO:
        """Test FeatureTextDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FeatureTextDTO`
        """
        model = FeatureTextDTO()
        if include_optional:
            return FeatureTextDTO(
                type = 'text',
                value = ''
            )
        else:
            return FeatureTextDTO(
                type = 'text',
                value = '',
        )
        """

    def testFeatureTextDTO(self):
        """Test FeatureTextDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
