# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.models.list_private_network_response import ListPrivateNetworkResponse

class TestListPrivateNetworkResponse(unittest.TestCase):
    """ListPrivateNetworkResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListPrivateNetworkResponse:
        """Test ListPrivateNetworkResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListPrivateNetworkResponse`
        """
        model = ListPrivateNetworkResponse()
        if include_optional:
            return ListPrivateNetworkResponse(
                pagination = pfruck_contabo.models.pagination_meta.PaginationMeta(
                    size = 10, 
                    total_elements = 100, 
                    total_pages = 10, 
                    page = 1, ),
                data = [
                    pfruck_contabo.models.list_private_network_response_data.ListPrivateNetworkResponseData(
                        tenant_id = 'DE', 
                        customer_id = '54321', 
                        private_network_id = 12345, 
                        data_center = 'European Union 1', 
                        region = 'EU', 
                        region_name = 'European Union', 
                        name = 'myPrivateNetwork', 
                        description = 'myPrivateNetwork Description', 
                        cidr = '10.0.0.0/22', 
                        available_ips = 1022, 
                        created_date = '2021-06-03T06:27:12Z', 
                        instances = [
                            pfruck_contabo.models.instances.Instances(
                                instance_id = 100, 
                                display_name = 'Instance', 
                                name = 'vmd12345', 
                                product_id = 'V1', 
                                private_ip_config = pfruck_contabo.models.private_ip_config.PrivateIpConfig(
                                    v4 = [
                                        pfruck_contabo.models.ip_v4.IpV4(
                                            ip = '192.168.0.1', 
                                            netmask_cidr = 19, 
                                            gateway = '1.1.1.1', )
                                        ], ), 
                                ip_config = pfruck_contabo.models.ip_config.IpConfig(
                                    v4 = pfruck_contabo.models.ip_v4.IpV4(
                                        ip = '192.168.0.1', 
                                        netmask_cidr = 19, 
                                        gateway = '1.1.1.1', ), 
                                    v6 = pfruck_contabo.models.ip_v6.IpV6(
                                        ip = '1:2:3:4:5:6:7:8', 
                                        netmask_cidr = 64, 
                                        gateway = '1:2:3:4:5:6:7:8', ), ), 
                                status = 'ok', 
                                error_message = '', )
                            ], )
                    ],
                links = pfruck_contabo.models.links.Links(
                    self = '', 
                    first = '', 
                    previous = '', 
                    next = '', 
                    last = '', )
            )
        else:
            return ListPrivateNetworkResponse(
                pagination = pfruck_contabo.models.pagination_meta.PaginationMeta(
                    size = 10, 
                    total_elements = 100, 
                    total_pages = 10, 
                    page = 1, ),
                data = [
                    pfruck_contabo.models.list_private_network_response_data.ListPrivateNetworkResponseData(
                        tenant_id = 'DE', 
                        customer_id = '54321', 
                        private_network_id = 12345, 
                        data_center = 'European Union 1', 
                        region = 'EU', 
                        region_name = 'European Union', 
                        name = 'myPrivateNetwork', 
                        description = 'myPrivateNetwork Description', 
                        cidr = '10.0.0.0/22', 
                        available_ips = 1022, 
                        created_date = '2021-06-03T06:27:12Z', 
                        instances = [
                            pfruck_contabo.models.instances.Instances(
                                instance_id = 100, 
                                display_name = 'Instance', 
                                name = 'vmd12345', 
                                product_id = 'V1', 
                                private_ip_config = pfruck_contabo.models.private_ip_config.PrivateIpConfig(
                                    v4 = [
                                        pfruck_contabo.models.ip_v4.IpV4(
                                            ip = '192.168.0.1', 
                                            netmask_cidr = 19, 
                                            gateway = '1.1.1.1', )
                                        ], ), 
                                ip_config = pfruck_contabo.models.ip_config.IpConfig(
                                    v4 = pfruck_contabo.models.ip_v4.IpV4(
                                        ip = '192.168.0.1', 
                                        netmask_cidr = 19, 
                                        gateway = '1.1.1.1', ), 
                                    v6 = pfruck_contabo.models.ip_v6.IpV6(
                                        ip = '1:2:3:4:5:6:7:8', 
                                        netmask_cidr = 64, 
                                        gateway = '1:2:3:4:5:6:7:8', ), ), 
                                status = 'ok', 
                                error_message = '', )
                            ], )
                    ],
                links = pfruck_contabo.models.links.Links(
                    self = '', 
                    first = '', 
                    previous = '', 
                    next = '', 
                    last = '', ),
        )
        """

    def testListPrivateNetworkResponse(self):
        """Test ListPrivateNetworkResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
