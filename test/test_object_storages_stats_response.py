# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.models.object_storages_stats_response import ObjectStoragesStatsResponse

class TestObjectStoragesStatsResponse(unittest.TestCase):
    """ObjectStoragesStatsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ObjectStoragesStatsResponse:
        """Test ObjectStoragesStatsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ObjectStoragesStatsResponse`
        """
        model = ObjectStoragesStatsResponse()
        if include_optional:
            return ObjectStoragesStatsResponse(
                data = [
                    pfruck_contabo.models.object_storages_stats_response_data.ObjectStoragesStatsResponseData(
                        tenant_id = 'DE', 
                        customer_id = '54321', 
                        used_space_tb = 4, 
                        used_space_percentage = 100, 
                        number_of_objects = 2, )
                    ],
                links = pfruck_contabo.models.self_links.SelfLinks(
                    self = '', )
            )
        else:
            return ObjectStoragesStatsResponse(
                data = [
                    pfruck_contabo.models.object_storages_stats_response_data.ObjectStoragesStatsResponseData(
                        tenant_id = 'DE', 
                        customer_id = '54321', 
                        used_space_tb = 4, 
                        used_space_percentage = 100, 
                        number_of_objects = 2, )
                    ],
                links = pfruck_contabo.models.self_links.SelfLinks(
                    self = '', ),
        )
        """

    def testObjectStoragesStatsResponse(self):
        """Test ObjectStoragesStatsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
