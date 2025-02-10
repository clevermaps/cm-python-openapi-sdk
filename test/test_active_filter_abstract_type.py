# coding: utf-8

"""
    clevermaps-client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.active_filter_abstract_type import ActiveFilterAbstractType

class TestActiveFilterAbstractType(unittest.TestCase):
    """ActiveFilterAbstractType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActiveFilterAbstractType:
        """Test ActiveFilterAbstractType
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActiveFilterAbstractType`
        """
        model = ActiveFilterAbstractType()
        if include_optional:
            return ActiveFilterAbstractType(
                default_values = openapi_client.models.default_values_single_select_dto.DefaultValuesSingleSelectDTO(
                    value = '', ),
                type = 'date',
                var_property = 'awat5ikwowtta-3mh2lcafqw3zhes.i16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwscq-4zge8f37mn0',
                format = openapi_client.models.format_dto.FormatDTO(
                    type = 'number', 
                    fraction = 0, 
                    symbol = '', ),
                order_by = [
                    openapi_client.models.order_by_dto.OrderByDTO(
                        property = 'awat5ikwowtta-3mh2lcafqw3zhes.i16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwscq-4zge8f37mn0', 
                        direction = 'asc', )
                    ],
                indicator = '/rest/projects/8q6zgckec0l3o4gi/md/indicators?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc',
                filter_selection = True,
                compared = True,
                dataset = '/rest/projects/8q6zgckec0l3o4gi/md/datasets?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc'
            )
        else:
            return ActiveFilterAbstractType(
                default_values = openapi_client.models.default_values_single_select_dto.DefaultValuesSingleSelectDTO(
                    value = '', ),
                type = 'date',
                var_property = 'awat5ikwowtta-3mh2lcafqw3zhes.i16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwscq-4zge8f37mn0',
                indicator = '/rest/projects/8q6zgckec0l3o4gi/md/indicators?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc',
                dataset = '/rest/projects/8q6zgckec0l3o4gi/md/datasets?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc',
        )
        """

    def testActiveFilterAbstractType(self):
        """Test ActiveFilterAbstractType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
