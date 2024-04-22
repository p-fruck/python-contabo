# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.models.find_object_storage_response import FindObjectStorageResponse

class TestFindObjectStorageResponse(unittest.TestCase):
    """FindObjectStorageResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FindObjectStorageResponse:
        """Test FindObjectStorageResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FindObjectStorageResponse`
        """
        model = FindObjectStorageResponse()
        if include_optional:
            return FindObjectStorageResponse(
                data = [
                    pfruck_contabo.models.object_storage_response.ObjectStorageResponse(
                        tenant_id = 'DE', 
                        customer_id = '54321', 
                        object_storage_id = 'b943b25a-c8b5-4570-9135-4bbaa7615b81', 
                        created_date = '2021-06-02T12:32:03.363Z', 
                        cancel_date = 'Wed Jun 02 00:00:00 UTC 2021', 
                        auto_scaling = null, 
                        data_center = 'EU', 
                        total_purchased_space_tb = 6.25, 
                        s3_url = 'eu1-s3.contabo.com', 
                        s3_tenant_id = '2cd2e5e1444a41b0bed16c6410ecaa84', 
                        status = 'READY', 
                        region = 'European Union', 
                        display_name = 'Object storage 1', )
                    ],
                links = pfruck_contabo.models.self_links.SelfLinks(
                    self = '', )
            )
        else:
            return FindObjectStorageResponse(
                data = [
                    pfruck_contabo.models.object_storage_response.ObjectStorageResponse(
                        tenant_id = 'DE', 
                        customer_id = '54321', 
                        object_storage_id = 'b943b25a-c8b5-4570-9135-4bbaa7615b81', 
                        created_date = '2021-06-02T12:32:03.363Z', 
                        cancel_date = 'Wed Jun 02 00:00:00 UTC 2021', 
                        auto_scaling = null, 
                        data_center = 'EU', 
                        total_purchased_space_tb = 6.25, 
                        s3_url = 'eu1-s3.contabo.com', 
                        s3_tenant_id = '2cd2e5e1444a41b0bed16c6410ecaa84', 
                        status = 'READY', 
                        region = 'European Union', 
                        display_name = 'Object storage 1', )
                    ],
                links = pfruck_contabo.models.self_links.SelfLinks(
                    self = '', ),
        )
        """

    def testFindObjectStorageResponse(self):
        """Test FindObjectStorageResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
