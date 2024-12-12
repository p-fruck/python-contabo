# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.models.find_vip_response import FindVipResponse

class TestFindVipResponse(unittest.TestCase):
    """FindVipResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FindVipResponse:
        """Test FindVipResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FindVipResponse`
        """
        model = FindVipResponse()
        if include_optional:
            return FindVipResponse(
                data = [
                    pfruck_contabo.models.vip_response.VipResponse(
                        tenant_id = 'DE', 
                        customer_id = '1234', 
                        vip_id = 'a846c6cc-731c-45dc-b653-bc8232e88d9c', 
                        data_center = 'European Union (Germany) 3', 
                        region = 'European Union (Germany)', 
                        resource_id = '101234', 
                        resource_type = 'instances', 
                        resource_name = 'vmi100101', 
                        resource_display_name = 'My Instance 12', 
                        ip_version = 'v4', 
                        type = 'additional', 
                        v4 = pfruck_contabo.models.ip_v4.IpV4(
                            ip = '195.123.123.1', 
                            gateway = '255.255.255.1', 
                            netmask_cidr = 24, 
                            broadcast = '195.123.123.255', 
                            net = '195.123.123.0/24', ), )
                    ],
                links = pfruck_contabo.models.self_links.SelfLinks(
                    self = '', )
            )
        else:
            return FindVipResponse(
                data = [
                    pfruck_contabo.models.vip_response.VipResponse(
                        tenant_id = 'DE', 
                        customer_id = '1234', 
                        vip_id = 'a846c6cc-731c-45dc-b653-bc8232e88d9c', 
                        data_center = 'European Union (Germany) 3', 
                        region = 'European Union (Germany)', 
                        resource_id = '101234', 
                        resource_type = 'instances', 
                        resource_name = 'vmi100101', 
                        resource_display_name = 'My Instance 12', 
                        ip_version = 'v4', 
                        type = 'additional', 
                        v4 = pfruck_contabo.models.ip_v4.IpV4(
                            ip = '195.123.123.1', 
                            gateway = '255.255.255.1', 
                            netmask_cidr = 24, 
                            broadcast = '195.123.123.255', 
                            net = '195.123.123.0/24', ), )
                    ],
                links = pfruck_contabo.models.self_links.SelfLinks(
                    self = '', ),
        )
        """

    def testFindVipResponse(self):
        """Test FindVipResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
