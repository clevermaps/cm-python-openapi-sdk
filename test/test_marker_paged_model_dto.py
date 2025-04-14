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

from cm_python_openapi_sdk.models.marker_paged_model_dto import MarkerPagedModelDTO

class TestMarkerPagedModelDTO(unittest.TestCase):
    """MarkerPagedModelDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MarkerPagedModelDTO:
        """Test MarkerPagedModelDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MarkerPagedModelDTO`
        """
        model = MarkerPagedModelDTO()
        if include_optional:
            return MarkerPagedModelDTO(
                content = [
                    {name=name, description=description, id=id, type=dataset, title=title, content={propertyFilters=[{propertyName=propertyName, value=, operator=eq}, {propertyName=propertyName, value=, operator=eq}], style=style}}
                    ],
                links = [
                    None
                    ],
                page = {number=1, size=0, totalPages=6, totalElements=}
            )
        else:
            return MarkerPagedModelDTO(
        )
        """

    def testMarkerPagedModelDTO(self):
        """Test MarkerPagedModelDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
