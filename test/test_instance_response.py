"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pfruck_contabo
from pfruck_contabo.model.add_on_response import AddOnResponse
from pfruck_contabo.model.additional_ip import AdditionalIp
from pfruck_contabo.model.instance_status import InstanceStatus
from pfruck_contabo.model.ip_config import IpConfig
globals()['AddOnResponse'] = AddOnResponse
globals()['AdditionalIp'] = AdditionalIp
globals()['InstanceStatus'] = InstanceStatus
globals()['IpConfig'] = IpConfig
from pfruck_contabo.model.instance_response import InstanceResponse


class TestInstanceResponse(unittest.TestCase):
    """InstanceResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInstanceResponse(self):
        """Test InstanceResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = InstanceResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
