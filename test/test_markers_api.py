# coding: utf-8

"""
    clevermaps-client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cm_python_openapi_sdk.api.markers_api import MarkersApi


class TestMarkersApi(unittest.TestCase):
    """MarkersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MarkersApi()

    def tearDown(self) -> None:
        pass

    def test_create_marker(self) -> None:
        """Test case for create_marker

        Creates new Marker.
        """
        pass

    def test_delete_marker_by_id(self) -> None:
        """Test case for delete_marker_by_id

        Deletes marker by id
        """
        pass

    def test_get_all_markers(self) -> None:
        """Test case for get_all_markers

        Returns paged collection of all Markers in a project.
        """
        pass

    def test_get_marker_by_id(self) -> None:
        """Test case for get_marker_by_id

        Gets marker by id
        """
        pass

    def test_update_marker_by_id(self) -> None:
        """Test case for update_marker_by_id

        Updates marker by id
        """
        pass


if __name__ == '__main__':
    unittest.main()
