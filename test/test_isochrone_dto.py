# coding: utf-8

"""
    clevermaps-client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.isochrone_dto import IsochroneDTO

class TestIsochroneDTO(unittest.TestCase):
    """IsochroneDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IsochroneDTO:
        """Test IsochroneDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IsochroneDTO`
        """
        model = IsochroneDTO()
        if include_optional:
            return IsochroneDTO(
                lat = -180.0,
                lng = -180.0,
                profile = 'car',
                unit = 'time',
                amount = 1,
                geometry = None
            )
        else:
            return IsochroneDTO(
        )
        """

    def testIsochroneDTO(self):
        """Test IsochroneDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
