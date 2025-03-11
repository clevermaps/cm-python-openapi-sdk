# coding: utf-8

"""
    clevermaps-client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cm_python_openapi_sdk.models.category_dto import CategoryDTO

class TestCategoryDTO(unittest.TestCase):
    """CategoryDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CategoryDTO:
        """Test CategoryDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CategoryDTO`
        """
        model = CategoryDTO()
        if include_optional:
            return CategoryDTO(
                dataset = '/rest/projects/8q6zgckec0l3o4gi/md/datasets?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc',
                markers = [
                    cm_python_openapi_sdk.models.marker_link_dto.MarkerLinkDTO(
                        marker = '/rest/projects/8q6zgckec0l3o4gi/md/markers?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc', 
                        visible = True, 
                        add_on_expand = True, )
                    ],
                linked_layers = [
                    cm_python_openapi_sdk.models.linked_layer_dto.LinkedLayerDTO(
                        dataset = '/rest/projects/8q6zgckec0l3o4gi/md/datasets?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc', 
                        style = 'awat5ikwowtta-3mh2lcafqw3zhes', 
                        visible = True, )
                    ]
            )
        else:
            return CategoryDTO(
                dataset = '/rest/projects/8q6zgckec0l3o4gi/md/datasets?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc',
                markers = [
                    cm_python_openapi_sdk.models.marker_link_dto.MarkerLinkDTO(
                        marker = '/rest/projects/8q6zgckec0l3o4gi/md/markers?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc', 
                        visible = True, 
                        add_on_expand = True, )
                    ],
        )
        """

    def testCategoryDTO(self):
        """Test CategoryDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
