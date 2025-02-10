# coding: utf-8

"""
    clevermaps-client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.indicator_visualizations_dto import IndicatorVisualizationsDTO

class TestIndicatorVisualizationsDTO(unittest.TestCase):
    """IndicatorVisualizationsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IndicatorVisualizationsDTO:
        """Test IndicatorVisualizationsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IndicatorVisualizationsDTO`
        """
        model = IndicatorVisualizationsDTO()
        if include_optional:
            return IndicatorVisualizationsDTO(
                areas = True,
                grid = True,
                zones = True,
                line = True,
                dotmap = True,
                heatmap = True,
                dominance = True,
                heatmap_scale_factor = 1.337
            )
        else:
            return IndicatorVisualizationsDTO(
        )
        """

    def testIndicatorVisualizationsDTO(self):
        """Test IndicatorVisualizationsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
