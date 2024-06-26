# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.models.ip_v6 import IpV6

class TestIpV6(unittest.TestCase):
    """IpV6 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IpV6:
        """Test IpV6
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IpV6`
        """
        model = IpV6()
        if include_optional:
            return IpV6(
                ip = '1:2:3:4:5:6:7:8',
                netmask_cidr = 64,
                gateway = '1:2:3:4:5:6:7:8'
            )
        else:
            return IpV6(
                ip = '1:2:3:4:5:6:7:8',
                netmask_cidr = 64,
                gateway = '1:2:3:4:5:6:7:8',
        )
        """

    def testIpV6(self):
        """Test IpV6"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
