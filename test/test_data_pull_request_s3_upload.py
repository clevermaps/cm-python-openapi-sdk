# coding: utf-8

"""
    clevermaps-client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cm_python_openapi_sdk.models.data_pull_request_s3_upload import DataPullRequestS3Upload

class TestDataPullRequestS3Upload(unittest.TestCase):
    """DataPullRequestS3Upload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataPullRequestS3Upload:
        """Test DataPullRequestS3Upload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataPullRequestS3Upload`
        """
        model = DataPullRequestS3Upload()
        if include_optional:
            return DataPullRequestS3Upload(
                uri = '',
                access_key_id = '',
                secret_access_key = '',
                region = '',
                endpoint_override = '',
                force_path_style = True
            )
        else:
            return DataPullRequestS3Upload(
                uri = '',
        )
        """

    def testDataPullRequestS3Upload(self):
        """Test DataPullRequestS3Upload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
