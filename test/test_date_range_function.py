# coding: utf-8

"""
    clevermaps-client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cm_python_openapi_sdk.models.date_range_function import DateRangeFunction

class TestDateRangeFunction(unittest.TestCase):
    """DateRangeFunction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DateRangeFunction:
        """Test DateRangeFunction
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DateRangeFunction`
        """
        model = DateRangeFunction()
        if include_optional:
            return DateRangeFunction(
                function = cm_python_openapi_sdk.models.function.function()
            )
        else:
            return DateRangeFunction(
                function = cm_python_openapi_sdk.models.function.function(),
        )
        """

    def testDateRangeFunction(self):
        """Test DateRangeFunction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
