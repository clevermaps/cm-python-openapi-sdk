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

from cm_python_openapi_sdk.api.indicators_api import IndicatorsApi


class TestIndicatorsApi(unittest.TestCase):
    """IndicatorsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = IndicatorsApi()

    def tearDown(self) -> None:
        pass

    def test_create_indicator(self) -> None:
        """Test case for create_indicator

        Creates new Indicator.
        """
        pass

    def test_delete_indicator_by_id(self) -> None:
        """Test case for delete_indicator_by_id

        Deletes indicator by id
        """
        pass

    def test_get_all_indicators(self) -> None:
        """Test case for get_all_indicators

        Returns paged collection of all Indicators in a project.
        """
        pass

    def test_get_indicator_by_id(self) -> None:
        """Test case for get_indicator_by_id

        Gets indicator by id
        """
        pass

    def test_get_indicator_by_name(self) -> None:
        """Test case for get_indicator_by_name

        Gets indicator by name
        """
        pass

    def test_update_indicator_by_id(self) -> None:
        """Test case for update_indicator_by_id

        Updates indicator by id
        """
        pass


if __name__ == '__main__':
    unittest.main()
