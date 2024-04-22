# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.models.instances import Instances

class TestInstances(unittest.TestCase):
    """Instances unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Instances:
        """Test Instances
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Instances`
        """
        model = Instances()
        if include_optional:
            return Instances(
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
                error_message = ''
            )
        else:
            return Instances(
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
        )
        """

    def testInstances(self):
        """Test Instances"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
