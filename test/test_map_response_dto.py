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

from cm_python_openapi_sdk.models.map_response_dto import MapResponseDTO

class TestMapResponseDTO(unittest.TestCase):
    """MapResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MapResponseDTO:
        """Test MapResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MapResponseDTO`
        """
        model = MapResponseDTO()
        if include_optional:
            return MapResponseDTO(
                id = '',
                name = 'awat5ikwowtta-3mh2lcafqw3zhes',
                type = 'dataset',
                title = '0',
                description = '',
                content = {contextMenu={items=[{type=googleSatellite}, {type=googleSatellite}]}, baseLayer={menu=true, type=mapbox, accessToken=accessToken, url=url}, options={maxZoom=5, center={lng=6.027456183070403, lat=0.8008281904610115}, minZoom=0, zoom=1}, layers=[{indicator=inherit, baseStyle={fillColor=purple, fillOpacity=0.8008281904610115, outlineWidth=1.4658129805029452, size=5.962133916683182, fillHexColor=fillHexColor, outlineColor=purple, outlineHexColor=outlineHexColor, outlineOpacity=6.027456183070403}, visible=true, name=name, showIndicatorValueLabels=true, datasets=[{visualization=dotmap, attributeStyles=[{attributeStyle=attributeStyle}, {attributeStyle=attributeStyle}], dataset=dataset}, {visualization=dotmap, attributeStyles=[{attributeStyle=attributeStyle}, {attributeStyle=attributeStyle}], dataset=dataset}], clusterPoints=true, defaultDataset=defaultDataset, defaultVisualization=dotmap, keepFiltered=true}, {indicator=inherit, baseStyle={fillColor=purple, fillOpacity=0.8008281904610115, outlineWidth=1.4658129805029452, size=5.962133916683182, fillHexColor=fillHexColor, outlineColor=purple, outlineHexColor=outlineHexColor, outlineOpacity=6.027456183070403}, visible=true, name=name, showIndicatorValueLabels=true, datasets=[{visualization=dotmap, attributeStyles=[{attributeStyle=attributeStyle}, {attributeStyle=attributeStyle}], dataset=dataset}, {visualization=dotmap, attributeStyles=[{attributeStyle=attributeStyle}, {attributeStyle=attributeStyle}], dataset=dataset}], clusterPoints=true, defaultDataset=defaultDataset, defaultVisualization=dotmap, keepFiltered=true}]},
                links = [
                    None
                    ],
                page = {number=1, size=0, totalPages=6, totalElements=},
                access_info = {createdAt=createdAt, createdBy=createdBy, modifiedAt=modifiedAt, modifiedBy=modifiedBy},
                version = 56
            )
        else:
            return MapResponseDTO(
                name = 'awat5ikwowtta-3mh2lcafqw3zhes',
                content = {contextMenu={items=[{type=googleSatellite}, {type=googleSatellite}]}, baseLayer={menu=true, type=mapbox, accessToken=accessToken, url=url}, options={maxZoom=5, center={lng=6.027456183070403, lat=0.8008281904610115}, minZoom=0, zoom=1}, layers=[{indicator=inherit, baseStyle={fillColor=purple, fillOpacity=0.8008281904610115, outlineWidth=1.4658129805029452, size=5.962133916683182, fillHexColor=fillHexColor, outlineColor=purple, outlineHexColor=outlineHexColor, outlineOpacity=6.027456183070403}, visible=true, name=name, showIndicatorValueLabels=true, datasets=[{visualization=dotmap, attributeStyles=[{attributeStyle=attributeStyle}, {attributeStyle=attributeStyle}], dataset=dataset}, {visualization=dotmap, attributeStyles=[{attributeStyle=attributeStyle}, {attributeStyle=attributeStyle}], dataset=dataset}], clusterPoints=true, defaultDataset=defaultDataset, defaultVisualization=dotmap, keepFiltered=true}, {indicator=inherit, baseStyle={fillColor=purple, fillOpacity=0.8008281904610115, outlineWidth=1.4658129805029452, size=5.962133916683182, fillHexColor=fillHexColor, outlineColor=purple, outlineHexColor=outlineHexColor, outlineOpacity=6.027456183070403}, visible=true, name=name, showIndicatorValueLabels=true, datasets=[{visualization=dotmap, attributeStyles=[{attributeStyle=attributeStyle}, {attributeStyle=attributeStyle}], dataset=dataset}, {visualization=dotmap, attributeStyles=[{attributeStyle=attributeStyle}, {attributeStyle=attributeStyle}], dataset=dataset}], clusterPoints=true, defaultDataset=defaultDataset, defaultVisualization=dotmap, keepFiltered=true}]},
        )
        """

    def testMapResponseDTO(self):
        """Test MapResponseDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
