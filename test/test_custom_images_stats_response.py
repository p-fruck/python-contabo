# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.models.custom_images_stats_response import CustomImagesStatsResponse

class TestCustomImagesStatsResponse(unittest.TestCase):
    """CustomImagesStatsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomImagesStatsResponse:
        """Test CustomImagesStatsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomImagesStatsResponse`
        """
        model = CustomImagesStatsResponse()
        if include_optional:
            return CustomImagesStatsResponse(
                data = [
                    pfruck_contabo.models.custom_images_stats_response_data.CustomImagesStatsResponseData(
                        tenant_id = 'DE', 
                        customer_id = '54321', 
                        current_images_count = 4, 
                        total_size_mb = 102400, 
                        used_size_mb = 55000, 
                        free_size_mb = 47400, )
                    ],
                links = pfruck_contabo.models.self_links.SelfLinks(
                    self = '', )
            )
        else:
            return CustomImagesStatsResponse(
                data = [
                    pfruck_contabo.models.custom_images_stats_response_data.CustomImagesStatsResponseData(
                        tenant_id = 'DE', 
                        customer_id = '54321', 
                        current_images_count = 4, 
                        total_size_mb = 102400, 
                        used_size_mb = 55000, 
                        free_size_mb = 47400, )
                    ],
                links = pfruck_contabo.models.self_links.SelfLinks(
                    self = '', ),
        )
        """

    def testCustomImagesStatsResponse(self):
        """Test CustomImagesStatsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
