# coding: utf-8

"""
    clevermaps-client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cm_python_openapi_sdk.models.center_dto import CenterDTO

class TestCenterDTO(unittest.TestCase):
    """CenterDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CenterDTO:
        """Test CenterDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CenterDTO`
        """
        model = CenterDTO()
        if include_optional:
            return CenterDTO(
                lat = 1.337,
                lng = 1.337
            )
        else:
            return CenterDTO(
                lat = 1.337,
                lng = 1.337,
        )
        """

    def testCenterDTO(self):
        """Test CenterDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
