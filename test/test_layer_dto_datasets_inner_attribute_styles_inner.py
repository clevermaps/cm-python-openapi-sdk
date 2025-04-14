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

from cm_python_openapi_sdk.models.layer_dto_datasets_inner_attribute_styles_inner import LayerDTODatasetsInnerAttributeStylesInner

class TestLayerDTODatasetsInnerAttributeStylesInner(unittest.TestCase):
    """LayerDTODatasetsInnerAttributeStylesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LayerDTODatasetsInnerAttributeStylesInner:
        """Test LayerDTODatasetsInnerAttributeStylesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LayerDTODatasetsInnerAttributeStylesInner`
        """
        model = LayerDTODatasetsInnerAttributeStylesInner()
        if include_optional:
            return LayerDTODatasetsInnerAttributeStylesInner(
                attribute_style = '/rest/projects/8q6zgckec0l3o4gi/md/attributeStyles?name=lcafqw3zheseh16mckwqaot6282x4vh6wt7cgd04d0gu12zwv6v61pi05te5cj19uo1-vud_-tc_vbqgp4vj0u4t9xwduicwsc'
            )
        else:
            return LayerDTODatasetsInnerAttributeStylesInner(
        )
        """

    def testLayerDTODatasetsInnerAttributeStylesInner(self):
        """Test LayerDTODatasetsInnerAttributeStylesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
