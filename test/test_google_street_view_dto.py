# coding: utf-8

"""
    clevermaps-client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cm_python_openapi_sdk.models.google_street_view_dto import GoogleStreetViewDTO

class TestGoogleStreetViewDTO(unittest.TestCase):
    """GoogleStreetViewDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GoogleStreetViewDTO:
        """Test GoogleStreetViewDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GoogleStreetViewDTO`
        """
        model = GoogleStreetViewDTO()
        if include_optional:
            return GoogleStreetViewDTO(
                type = 'googleStreetView'
            )
        else:
            return GoogleStreetViewDTO(
        )
        """

    def testGoogleStreetViewDTO(self):
        """Test GoogleStreetViewDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
