from __future__ import absolute_import, print_function

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from pyros_interfaces_mock import populate_instance, StatusMsg
from pyros_interfaces_mock import statusecho_topic, MockSystem


class TestMockTopic(object):
    """
    Main test fixture holding all tests
    Subclasses can override setup / teardown to test different environments
    """

    # Class fixture ( once each )
    @classmethod
    def setup_class(cls):
        cls.system = MockSystem()

    @classmethod
    def teardown_class(cls):
        pass

    def test_echo_status(self):
        msg = populate_instance({
            'error': 'BAD_ERROR',
            'code': 7,
            'message': 'A bad Error happened'
        }, StatusMsg('ERROR', 42, 'details'))
        assert isinstance(msg, StatusMsg)
        echo_topic_pub = self.system.create_publisher('random_topic', statusecho_topic)
        echo_topic_sub = self.system.create_subscriber('random_topic', statusecho_topic)
        assert echo_topic_pub.publish(msg)
        recv = echo_topic_sub.get()
        print(recv)
        assert recv.error == 'BAD_ERROR'
        assert recv.code == 7
        assert recv.message == 'A bad Error happened'


# Just in case we run this directly
if __name__ == '__main__':
    import pytest
    pytest.main([
        '-s', __file__,
])
