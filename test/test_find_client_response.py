# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.models.find_client_response import FindClientResponse

class TestFindClientResponse(unittest.TestCase):
    """FindClientResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FindClientResponse:
        """Test FindClientResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FindClientResponse`
        """
        model = FindClientResponse()
        if include_optional:
            return FindClientResponse(
                data = [
                    pfruck_contabo.models.client_response.ClientResponse(
                        tenant_id = 'DE', 
                        customer_id = '54321', 
                        id = '6cdf5968-f9fe-4192-97c2-f349e813c5e8', 
                        client_id = 'DE-54321', 
                        secret = '7271e905-239e-4d15-a8c5-527743a58390', )
                    ],
                links = pfruck_contabo.models.self_links.SelfLinks(
                    self = '', )
            )
        else:
            return FindClientResponse(
                data = [
                    pfruck_contabo.models.client_response.ClientResponse(
                        tenant_id = 'DE', 
                        customer_id = '54321', 
                        id = '6cdf5968-f9fe-4192-97c2-f349e813c5e8', 
                        client_id = 'DE-54321', 
                        secret = '7271e905-239e-4d15-a8c5-527743a58390', )
                    ],
                links = pfruck_contabo.models.self_links.SelfLinks(
                    self = '', ),
        )
        """

    def testFindClientResponse(self):
        """Test FindClientResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
