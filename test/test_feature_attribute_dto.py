# coding: utf-8

"""
    clevermaps-client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cm_python_openapi_sdk.models.feature_attribute_dto import FeatureAttributeDTO

class TestFeatureAttributeDTO(unittest.TestCase):
    """FeatureAttributeDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FeatureAttributeDTO:
        """Test FeatureAttributeDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FeatureAttributeDTO`
        """
        model = FeatureAttributeDTO()
        if include_optional:
            return FeatureAttributeDTO(
                type = 'property',
                value = '',
                format = cm_python_openapi_sdk.models.attribute_format_dto.AttributeFormatDTO(
                    type = 'text', 
                    fraction = 0, 
                    symbol = '', ),
                layout = 'primary'
            )
        else:
            return FeatureAttributeDTO(
                type = 'property',
                value = '',
        )
        """

    def testFeatureAttributeDTO(self):
        """Test FeatureAttributeDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
