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

from cm_python_openapi_sdk.models.queries_response import QueriesResponse

class TestQueriesResponse(unittest.TestCase):
    """QueriesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QueriesResponse:
        """Test QueriesResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QueriesResponse`
        """
        model = QueriesResponse()
        if include_optional:
            return QueriesResponse(
                execution_detail = {feature=feature, viewName=viewName, dwhQueryMetricNames=[dwhQueryMetricNames, dwhQueryMetricNames], doubleCountingWarnings=[{detailMessage=detailMessage, propertyId=propertyId}, {detailMessage=detailMessage, propertyId=propertyId}]}
            )
        else:
            return QueriesResponse(
                execution_detail = {feature=feature, viewName=viewName, dwhQueryMetricNames=[dwhQueryMetricNames, dwhQueryMetricNames], doubleCountingWarnings=[{detailMessage=detailMessage, propertyId=propertyId}, {detailMessage=detailMessage, propertyId=propertyId}]},
        )
        """

    def testQueriesResponse(self):
        """Test QueriesResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
