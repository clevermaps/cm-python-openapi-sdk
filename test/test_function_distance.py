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

from cm_python_openapi_sdk.models.function_distance import FunctionDistance

class TestFunctionDistance(unittest.TestCase):
    """FunctionDistance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FunctionDistance:
        """Test FunctionDistance
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FunctionDistance`
        """
        model = FunctionDistance()
        if include_optional:
            return FunctionDistance(
                id = 'z0',
                type = 'function_distance',
                options = cm_python_openapi_sdk.models.function_distance_options.FunctionDistanceOptions(
                    dataset = 'awat5ikwowtta-3mh2lcafqw3zhes', 
                    central_point = cm_python_openapi_sdk.models.central_point.CentralPoint(
                        lat = 1.337, 
                        lng = 1.337, ), )
            )
        else:
            return FunctionDistance(
                type = 'function_distance',
                options = cm_python_openapi_sdk.models.function_distance_options.FunctionDistanceOptions(
                    dataset = 'awat5ikwowtta-3mh2lcafqw3zhes', 
                    central_point = cm_python_openapi_sdk.models.central_point.CentralPoint(
                        lat = 1.337, 
                        lng = 1.337, ), ),
        )
        """

    def testFunctionDistance(self):
        """Test FunctionDistance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
