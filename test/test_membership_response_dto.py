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

from cm_python_openapi_sdk.models.membership_response_dto import MembershipResponseDTO

class TestMembershipResponseDTO(unittest.TestCase):
    """MembershipResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MembershipResponseDTO:
        """Test MembershipResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MembershipResponseDTO`
        """
        model = MembershipResponseDTO()
        if include_optional:
            return MembershipResponseDTO(
                id = '',
                account_id = '',
                status = 'ENABLED',
                role = 'ANONYMOUS',
                created_at = '',
                modified_at = '',
                account = {preferences={sendNewsletter=true, lastActiveOrganization=lastActiveOrganization, language=language, lastActiveProject=lastActiveProject}, phoneNumber=phoneNumber, fullName=fullName, anonymous=true, onboarding={introShown=[introShown, introShown], tipsShown=[tipsShown, tipsShown]}, links=[{}, {}], id=id, consentGranted=true, email=email, status=ENABLED},
                links = [
                    None
                    ]
            )
        else:
            return MembershipResponseDTO(
                status = 'ENABLED',
                role = 'ANONYMOUS',
        )
        """

    def testMembershipResponseDTO(self):
        """Test MembershipResponseDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
