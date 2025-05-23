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

from cm_python_openapi_sdk.models.dwh_date_range_request import DwhDateRangeRequest

class TestDwhDateRangeRequest(unittest.TestCase):
    """DwhDateRangeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DwhDateRangeRequest:
        """Test DwhDateRangeRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DwhDateRangeRequest`
        """
        model = DwhDateRangeRequest()
        if include_optional:
            return DwhDateRangeRequest(
                execution_context = {feature=feature, viewName=viewName},
                var_from = 'awat5ikwowtta-3mh2lcafqw3zhes.i16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwscq-4zge8f37mn0',
                filter = {endDate=null, startDate={value=value}}
            )
        else:
            return DwhDateRangeRequest(
                var_from = 'awat5ikwowtta-3mh2lcafqw3zhes.i16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwscq-4zge8f37mn0',
        )
        """

    def testDwhDateRangeRequest(self):
        """Test DwhDateRangeRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
