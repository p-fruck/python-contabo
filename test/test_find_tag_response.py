# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.models.find_tag_response import FindTagResponse

class TestFindTagResponse(unittest.TestCase):
    """FindTagResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FindTagResponse:
        """Test FindTagResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FindTagResponse`
        """
        model = FindTagResponse()
        if include_optional:
            return FindTagResponse(
                data = [
                    pfruck_contabo.models.tag_response.TagResponse(
                        tenant_id = 'DE', 
                        customer_id = '54321', 
                        tag_id = 12345, 
                        name = 'Web-Server', 
                        color = '#0A78C3', )
                    ],
                links = pfruck_contabo.models.self_links.SelfLinks(
                    self = '', )
            )
        else:
            return FindTagResponse(
                data = [
                    pfruck_contabo.models.tag_response.TagResponse(
                        tenant_id = 'DE', 
                        customer_id = '54321', 
                        tag_id = 12345, 
                        name = 'Web-Server', 
                        color = '#0A78C3', )
                    ],
                links = pfruck_contabo.models.self_links.SelfLinks(
                    self = '', ),
        )
        """

    def testFindTagResponse(self):
        """Test FindTagResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
