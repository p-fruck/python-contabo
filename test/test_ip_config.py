"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pfruck_contabo
from pfruck_contabo.model.ip_v4 import IpV4
from pfruck_contabo.model.ip_v6 import IpV6
globals()['IpV4'] = IpV4
globals()['IpV6'] = IpV6
from pfruck_contabo.model.ip_config import IpConfig


class TestIpConfig(unittest.TestCase):
    """IpConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIpConfig(self):
        """Test IpConfig"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IpConfig()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
