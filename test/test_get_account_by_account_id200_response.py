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

from cm_python_openapi_sdk.models.get_account_by_account_id200_response import GetAccountByAccountId200Response

class TestGetAccountByAccountId200Response(unittest.TestCase):
    """GetAccountByAccountId200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAccountByAccountId200Response:
        """Test GetAccountByAccountId200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAccountByAccountId200Response`
        """
        model = GetAccountByAccountId200Response()
        if include_optional:
            return GetAccountByAccountId200Response(
                id = '',
                full_name = '0',
                email = '',
                status = 'ENABLED',
                preferences = {sendNewsletter=true, lastActiveOrganization=lastActiveOrganization, language=language, lastActiveProject=lastActiveProject},
                consent_granted = True,
                anonymous = True,
                phone_number = '012345',
                onboarding = {introShown=[introShown, introShown], tipsShown=[tipsShown, tipsShown]},
                links = [
                    None
                    ]
            )
        else:
            return GetAccountByAccountId200Response(
                id = '',
                full_name = '0',
                email = '',
                status = 'ENABLED',
        )
        """

    def testGetAccountByAccountId200Response(self):
        """Test GetAccountByAccountId200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
