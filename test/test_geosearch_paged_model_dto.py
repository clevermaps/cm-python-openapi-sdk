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

from cm_python_openapi_sdk.models.geosearch_paged_model_dto import GeosearchPagedModelDTO

class TestGeosearchPagedModelDTO(unittest.TestCase):
    """GeosearchPagedModelDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GeosearchPagedModelDTO:
        """Test GeosearchPagedModelDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GeosearchPagedModelDTO`
        """
        model = GeosearchPagedModelDTO()
        if include_optional:
            return GeosearchPagedModelDTO(
                links = [
                    None
                    ],
                content = [
                    {highlight={subtitle=subtitle, title=title}, boundingBox={minY=5.962133916683182, minX=1.4658129805029452, maxY=2.3021358869347655, maxX=5.637376656633329}, placeType=region, subtitle=subtitle, position={lng=6.027456183070403, lat=0.8008281904610115}, title=title}
                    ],
                page = {number=1, size=0, totalPages=6, totalElements=}
            )
        else:
            return GeosearchPagedModelDTO(
        )
        """

    def testGeosearchPagedModelDTO(self):
        """Test GeosearchPagedModelDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
