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

from cm_python_openapi_sdk.api.project_settings_api import ProjectSettingsApi


class TestProjectSettingsApi(unittest.TestCase):
    """ProjectSettingsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProjectSettingsApi()

    def tearDown(self) -> None:
        pass

    def test_create_project_settings(self) -> None:
        """Test case for create_project_settings

        Creates new project settings
        """
        pass

    def test_delete_project_settings_by_id(self) -> None:
        """Test case for delete_project_settings_by_id

        Deletes project settings by id
        """
        pass

    def test_get_all_project_settings(self) -> None:
        """Test case for get_all_project_settings

        Returns paged collection of all Project Settings objects in a project. This page will always contain only one object.
        """
        pass

    def test_get_project_settings_by_id(self) -> None:
        """Test case for get_project_settings_by_id

        Gets project settings by id
        """
        pass

    def test_get_project_settings_by_name(self) -> None:
        """Test case for get_project_settings_by_name

        Gets projectSettings by name
        """
        pass

    def test_update_project_settings_by_id(self) -> None:
        """Test case for update_project_settings_by_id

        Updates project settings by id
        """
        pass


if __name__ == '__main__':
    unittest.main()
