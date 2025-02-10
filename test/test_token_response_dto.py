# coding: utf-8

"""
    clevermaps-client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.token_response_dto import TokenResponseDTO

class TestTokenResponseDTO(unittest.TestCase):
    """TokenResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokenResponseDTO:
        """Test TokenResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokenResponseDTO`
        """
        model = TokenResponseDTO()
        if include_optional:
            return TokenResponseDTO(
                token_type = '',
                expires_in = 56,
                access_token = '',
                scope = '',
                refresh_token = '',
                id_token = ''
            )
        else:
            return TokenResponseDTO(
                access_token = '',
        )
        """

    def testTokenResponseDTO(self):
        """Test TokenResponseDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
