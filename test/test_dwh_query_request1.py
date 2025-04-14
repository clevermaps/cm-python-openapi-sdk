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

from cm_python_openapi_sdk.models.dwh_query_request1 import DwhQueryRequest1

class TestDwhQueryRequest1(unittest.TestCase):
    """DwhQueryRequest1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DwhQueryRequest1:
        """Test DwhQueryRequest1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DwhQueryRequest1`
        """
        model = DwhQueryRequest1()
        if include_optional:
            return DwhQueryRequest1(
                execution_context = None,
                properties = [
                    null
                    ],
                filter_by = [
                    null
                    ],
                having = [
                    null
                    ],
                result_set_filter = [
                    null
                    ],
                order_by = [
                    {property=, nulls=last, propertyId=propertyId, direction=asc}
                    ],
                variables = [
                    {variable=variable, value=6.027456183070403}
                    ],
                limit = 1
            )
        else:
            return DwhQueryRequest1(
                properties = [
                    null
                    ],
        )
        """

    def testDwhQueryRequest1(self):
        """Test DwhQueryRequest1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
