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

from cm_python_openapi_sdk.models.new_account_dto import NewAccountDTO

class TestNewAccountDTO(unittest.TestCase):
    """NewAccountDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NewAccountDTO:
        """Test NewAccountDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NewAccountDTO`
        """
        model = NewAccountDTO()
        if include_optional:
            return NewAccountDTO(
                given_name = 'L0',
                surname = 'L0',
                email = '',
                password = '',
                consent_granted = True,
                phone_number = '012345',
                require_additional_attributes = True,
                preferences = {sendNewsletter=true, lastActiveOrganization=lastActiveOrganization, language=language, lastActiveProject=lastActiveProject},
                utm_parameters = {referrer=referrer, campaign=campaign, medium=medium, source=source},
                job_info = {companyName=companyName, industry=industry, jobPosition=jobPosition}
            )
        else:
            return NewAccountDTO(
                given_name = 'L0',
                surname = 'L0',
                email = '',
                password = '',
        )
        """

    def testNewAccountDTO(self):
        """Test NewAccountDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
