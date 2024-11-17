# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.models.ip_v41 import IpV41

class TestIpV41(unittest.TestCase):
    """IpV41 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IpV41:
        """Test IpV41
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IpV41`
        """
        model = IpV41()
        if include_optional:
            return IpV41(
                ip = '192.168.0.1',
                netmask_cidr = 19,
                gateway = '1.1.1.1'
            )
        else:
            return IpV41(
                ip = '192.168.0.1',
                netmask_cidr = 19,
                gateway = '1.1.1.1',
        )
        """

    def testIpV41(self):
        """Test IpV41"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
