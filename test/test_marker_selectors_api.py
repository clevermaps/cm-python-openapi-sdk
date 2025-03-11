# coding: utf-8

"""
    clevermaps-client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cm_python_openapi_sdk.api.marker_selectors_api import MarkerSelectorsApi


class TestMarkerSelectorsApi(unittest.TestCase):
    """MarkerSelectorsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MarkerSelectorsApi()

    def tearDown(self) -> None:
        pass

    def test_create_marker_selector(self) -> None:
        """Test case for create_marker_selector

        Creates new Marker Selector.
        """
        pass

    def test_delete_marker_selector_by_id(self) -> None:
        """Test case for delete_marker_selector_by_id

        Deletes marker selector by id
        """
        pass

    def test_get_all_marker_selectors(self) -> None:
        """Test case for get_all_marker_selectors

        Returns paged collection of all Marker Selectors in a project.
        """
        pass

    def test_get_marker_selector_by_id(self) -> None:
        """Test case for get_marker_selector_by_id

        Gets marker selector by id
        """
        pass

    def test_update_marker_selector_by_id(self) -> None:
        """Test case for update_marker_selector_by_id

        Updates marker selector by id
        """
        pass


if __name__ == '__main__':
    unittest.main()
