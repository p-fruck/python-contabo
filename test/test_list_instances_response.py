# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.models.list_instances_response import ListInstancesResponse

class TestListInstancesResponse(unittest.TestCase):
    """ListInstancesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListInstancesResponse:
        """Test ListInstancesResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListInstancesResponse`
        """
        model = ListInstancesResponse()
        if include_optional:
            return ListInstancesResponse(
                pagination = pfruck_contabo.models.pagination_meta.PaginationMeta(
                    size = 10, 
                    total_elements = 100, 
                    total_pages = 10, 
                    page = 1, ),
                data = [
                    pfruck_contabo.models.list_instances_response_data.ListInstancesResponseData(
                        tenant_id = 'DE', 
                        customer_id = '3f184ab8-a600-4e7c-8c9b-3413e21a3752', 
                        additional_ips = [
                            pfruck_contabo.models.additional_ip.AdditionalIp(
                                v4 = pfruck_contabo.models.ip_v4.IpV4(
                                    ip = '192.168.0.1', 
                                    netmask_cidr = 19, 
                                    gateway = '1.1.1.1', ), )
                            ], 
                        name = 'vmd12345', 
                        display_name = 'VPS', 
                        instance_id = 100, 
                        data_center = 'European Union 1', 
                        region = 'EU', 
                        region_name = 'European Union', 
                        product_id = 'V5', 
                        image_id = '9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d', 
                        ip_config = pfruck_contabo.models.ip_config.IpConfig(
                            v4 = pfruck_contabo.models.ip_v4.IpV4(
                                ip = '192.168.0.1', 
                                netmask_cidr = 19, 
                                gateway = '1.1.1.1', ), 
                            v6 = pfruck_contabo.models.ip_v6.IpV6(
                                ip = '1:2:3:4:5:6:7:8', 
                                netmask_cidr = 64, 
                                gateway = '1:2:3:4:5:6:7:8', ), ), 
                        mac_address = 'F2:65:50:F3:63:A1', 
                        ram_mb = 1024, 
                        cpu_cores = 4, 
                        os_type = 'Linux', 
                        disk_mb = 2048, 
                        ssh_keys = [123,125], 
                        created_date = '2021-06-03T06:27:12Z', 
                        cancel_date = 'Thu Jun 03 00:00:00 UTC 2021', 
                        status = 'provisioning', 
                        v_host_id = 73395, 
                        v_host_number = 1001, 
                        v_host_name = 'm1000', 
                        add_ons = [
                            pfruck_contabo.models.add_on_response.AddOnResponse(
                                id = 1431, 
                                quantity = 4, )
                            ], 
                        error_message = '', 
                        product_type = 'ssd', 
                        product_name = 'VPS M', 
                        default_user = 'root', )
                    ],
                links = pfruck_contabo.models.links.Links(
                    self = '', 
                    first = '', 
                    previous = '', 
                    next = '', 
                    last = '', )
            )
        else:
            return ListInstancesResponse(
                pagination = pfruck_contabo.models.pagination_meta.PaginationMeta(
                    size = 10, 
                    total_elements = 100, 
                    total_pages = 10, 
                    page = 1, ),
                data = [
                    pfruck_contabo.models.list_instances_response_data.ListInstancesResponseData(
                        tenant_id = 'DE', 
                        customer_id = '3f184ab8-a600-4e7c-8c9b-3413e21a3752', 
                        additional_ips = [
                            pfruck_contabo.models.additional_ip.AdditionalIp(
                                v4 = pfruck_contabo.models.ip_v4.IpV4(
                                    ip = '192.168.0.1', 
                                    netmask_cidr = 19, 
                                    gateway = '1.1.1.1', ), )
                            ], 
                        name = 'vmd12345', 
                        display_name = 'VPS', 
                        instance_id = 100, 
                        data_center = 'European Union 1', 
                        region = 'EU', 
                        region_name = 'European Union', 
                        product_id = 'V5', 
                        image_id = '9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d', 
                        ip_config = pfruck_contabo.models.ip_config.IpConfig(
                            v4 = pfruck_contabo.models.ip_v4.IpV4(
                                ip = '192.168.0.1', 
                                netmask_cidr = 19, 
                                gateway = '1.1.1.1', ), 
                            v6 = pfruck_contabo.models.ip_v6.IpV6(
                                ip = '1:2:3:4:5:6:7:8', 
                                netmask_cidr = 64, 
                                gateway = '1:2:3:4:5:6:7:8', ), ), 
                        mac_address = 'F2:65:50:F3:63:A1', 
                        ram_mb = 1024, 
                        cpu_cores = 4, 
                        os_type = 'Linux', 
                        disk_mb = 2048, 
                        ssh_keys = [123,125], 
                        created_date = '2021-06-03T06:27:12Z', 
                        cancel_date = 'Thu Jun 03 00:00:00 UTC 2021', 
                        status = 'provisioning', 
                        v_host_id = 73395, 
                        v_host_number = 1001, 
                        v_host_name = 'm1000', 
                        add_ons = [
                            pfruck_contabo.models.add_on_response.AddOnResponse(
                                id = 1431, 
                                quantity = 4, )
                            ], 
                        error_message = '', 
                        product_type = 'ssd', 
                        product_name = 'VPS M', 
                        default_user = 'root', )
                    ],
                links = pfruck_contabo.models.links.Links(
                    self = '', 
                    first = '', 
                    previous = '', 
                    next = '', 
                    last = '', ),
        )
        """

    def testListInstancesResponse(self):
        """Test ListInstancesResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
