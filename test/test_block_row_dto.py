# coding: utf-8

"""
    clevermaps-client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.block_row_dto import BlockRowDTO

class TestBlockRowDTO(unittest.TestCase):
    """BlockRowDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BlockRowDTO:
        """Test BlockRowDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BlockRowDTO`
        """
        model = BlockRowDTO()
        if include_optional:
            return BlockRowDTO(
                type = 'blockRow',
                blocks = [
                    openapi_client.models.indicator_link_dto.IndicatorLinkDTO(
                        type = 'indicator', 
                        title = '', 
                        indicator = '/rest/projects/8q6zgckec0l3o4gi/md/indicators?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc', 
                        indicator_drill = '/rest/projects/8q6zgckec0l3o4gi/md/indicatorDrills?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc', 
                        layout = 'primary', 
                        collapsed = True, 
                        block_rows = [
                            null
                            ], )
                    ]
            )
        else:
            return BlockRowDTO(
                type = 'blockRow',
                blocks = [
                    openapi_client.models.indicator_link_dto.IndicatorLinkDTO(
                        type = 'indicator', 
                        title = '', 
                        indicator = '/rest/projects/8q6zgckec0l3o4gi/md/indicators?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc', 
                        indicator_drill = '/rest/projects/8q6zgckec0l3o4gi/md/indicatorDrills?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc', 
                        layout = 'primary', 
                        collapsed = True, 
                        block_rows = [
                            null
                            ], )
                    ],
        )
        """

    def testBlockRowDTO(self):
        """Test BlockRowDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
