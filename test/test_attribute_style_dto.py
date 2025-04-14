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

from cm_python_openapi_sdk.models.attribute_style_dto import AttributeStyleDTO

class TestAttributeStyleDTO(unittest.TestCase):
    """AttributeStyleDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AttributeStyleDTO:
        """Test AttributeStyleDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AttributeStyleDTO`
        """
        model = AttributeStyleDTO()
        if include_optional:
            return AttributeStyleDTO(
                id = '',
                name = 'awat5ikwowtta-3mh2lcafqw3zhes',
                type = 'dataset',
                title = '0',
                description = '',
                content = {fallbackCategory={style={fillColor=purple, fillOpacity=0.8008281904610115, outlineWidth=1.4658129805029452, size=5.962133916683182, fillHexColor=fillHexColor, outlineColor=purple, outlineHexColor=outlineHexColor, outlineOpacity=6.027456183070403}, title=title}, property=property, categories=[{style={fillColor=purple, fillOpacity=0.8008281904610115, outlineWidth=1.4658129805029452, size=5.962133916683182, fillHexColor=fillHexColor, outlineColor=purple, outlineHexColor=outlineHexColor, outlineOpacity=6.027456183070403}, title=title, value=}, {style={fillColor=purple, fillOpacity=0.8008281904610115, outlineWidth=1.4658129805029452, size=5.962133916683182, fillHexColor=fillHexColor, outlineColor=purple, outlineHexColor=outlineHexColor, outlineOpacity=6.027456183070403}, title=title, value=}]}
            )
        else:
            return AttributeStyleDTO(
                name = 'awat5ikwowtta-3mh2lcafqw3zhes',
                content = {fallbackCategory={style={fillColor=purple, fillOpacity=0.8008281904610115, outlineWidth=1.4658129805029452, size=5.962133916683182, fillHexColor=fillHexColor, outlineColor=purple, outlineHexColor=outlineHexColor, outlineOpacity=6.027456183070403}, title=title}, property=property, categories=[{style={fillColor=purple, fillOpacity=0.8008281904610115, outlineWidth=1.4658129805029452, size=5.962133916683182, fillHexColor=fillHexColor, outlineColor=purple, outlineHexColor=outlineHexColor, outlineOpacity=6.027456183070403}, title=title, value=}, {style={fillColor=purple, fillOpacity=0.8008281904610115, outlineWidth=1.4658129805029452, size=5.962133916683182, fillHexColor=fillHexColor, outlineColor=purple, outlineHexColor=outlineHexColor, outlineOpacity=6.027456183070403}, title=title, value=}]},
        )
        """

    def testAttributeStyleDTO(self):
        """Test AttributeStyleDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
