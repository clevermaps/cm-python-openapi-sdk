# coding: utf-8

"""
    clevermaps-client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cm_python_openapi_sdk.models.isochrone_paged_model_dto import IsochronePagedModelDTO

class TestIsochronePagedModelDTO(unittest.TestCase):
    """IsochronePagedModelDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IsochronePagedModelDTO:
        """Test IsochronePagedModelDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IsochronePagedModelDTO`
        """
        model = IsochronePagedModelDTO()
        if include_optional:
            return IsochronePagedModelDTO(
                links = [
                    None
                    ],
                content = [
                    cm_python_openapi_sdk.models.isochrone_dto.IsochroneDTO(
                        lat = -180.0, 
                        lng = -180.0, 
                        profile = 'car', 
                        unit = 'time', 
                        amount = 1, 
                        geometry = cm_python_openapi_sdk.models.geometry.geometry(), )
                    ],
                page = cm_python_openapi_sdk.models.mandatory_keys_for_pagable_response.mandatory keys for pagable response(
                    size = 56, 
                    total_elements = null, 
                    total_pages = 56, 
                    number = 56, )
            )
        else:
            return IsochronePagedModelDTO(
        )
        """

    def testIsochronePagedModelDTO(self):
        """Test IsochronePagedModelDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
