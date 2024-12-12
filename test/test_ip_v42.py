# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.models.ip_v42 import IpV42

class TestIpV42(unittest.TestCase):
    """IpV42 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IpV42:
        """Test IpV42
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IpV42`
        """
        model = IpV42()
        if include_optional:
            return IpV42(
                ip = '192.168.0.1',
                netmask_cidr = 19,
                gateway = '1.1.1.1'
            )
        else:
            return IpV42(
                ip = '192.168.0.1',
                netmask_cidr = 19,
                gateway = '1.1.1.1',
        )
        """

    def testIpV42(self):
        """Test IpV42"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()