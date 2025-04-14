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

from cm_python_openapi_sdk.api.data_dump_api import DataDumpApi


class TestDataDumpApi(unittest.TestCase):
    """DataDumpApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DataDumpApi()

    def tearDown(self) -> None:
        pass

    def test_get_data_dump(self) -> None:
        """Test case for get_data_dump

        Get data dump file
        """
        pass


if __name__ == '__main__':
    unittest.main()
