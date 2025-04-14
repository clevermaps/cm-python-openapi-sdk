# coding: utf-8

"""
    clevermaps-client

    CleverMaps REST API provides access to location intelligence and geospatial analytics platform.  ### Main capabilities include: - Project and user access management - Multidimensional data model and metrics management - Data upload and exports - Ad-hoc analysis of geospatial data - Full text and geographic search - Configuration of CleverMaps Studio visualizations 

    The version of the OpenAPI document: 1.0.0
    Contact: support@clevermaps.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cm_python_openapi_sdk.models.property_values_response import PropertyValuesResponse

class TestPropertyValuesResponse(unittest.TestCase):
    """PropertyValuesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PropertyValuesResponse:
        """Test PropertyValuesResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PropertyValuesResponse`
        """
        model = PropertyValuesResponse()
        if include_optional:
            return PropertyValuesResponse(
                content = [
                    null
                    ],
                links = [
                    None
                    ],
                page = {number=1, size=0, totalPages=6, totalElements=}
            )
        else:
            return PropertyValuesResponse(
                content = [
                    null
                    ],
                links = [
                    None
                    ],
                page = {number=1, size=0, totalPages=6, totalElements=},
        )
        """

    def testPropertyValuesResponse(self):
        """Test PropertyValuesResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
