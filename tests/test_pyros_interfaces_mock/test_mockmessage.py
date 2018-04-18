from __future__ import absolute_import, print_function

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from pyros_interfaces_mock import extract_values, populate_instance, FieldTypeMismatchException, NonexistentFieldException, StatusMsg

import pytest

def test_populate_msg_bool_true():
    msg = populate_instance(True, bool())
    print("msg is of type {0}".format(type(msg)))
    assert isinstance(msg, bool)
    assert msg


def test_populate_msg_bool_false():
    msg = populate_instance(False, bool())
    print("msg is of type {0}".format(type(msg)))
    assert isinstance(msg, bool)
    assert not msg


def test_populate_msg_int_to_int():
    msg = populate_instance(42, int())
    print("msg is of type {0}".format(type(msg)))
    assert isinstance(msg, int)
    assert msg == 42


def test_populate_msg_int_to_float():
    msg = populate_instance(42, float())
    print("msg is of type {0}".format(type(msg)))
    assert isinstance(msg, float)
    assert msg == 42.0


def test_populate_msg_float():
    msg = populate_instance(3.1415, float())
    print("msg is of type {0}".format(type(msg)))
    assert isinstance(msg, float)
    assert msg == 3.1415


def test_populate_msg_float_to_int_error():
    with pytest.raises(FieldTypeMismatchException):
        populate_instance(3.1415, int())


if sys.version_info >= (3, 0):
    def test_populate_msg_bytes_to_bytes():
        msg = populate_instance(b'forty two', bytes())
        print("msg is of type {0}".format(type(msg)))
        assert isinstance(msg, bytes)
        assert msg == b'forty two'


def test_populate_msg_str_to_str():
    msg = populate_instance(r'forty two', str())
    print("msg is of type {0}".format(type(msg)))
    assert isinstance(msg, str)
    assert msg == r'forty two'


if sys.version_info < (3, 0):
    def test_populate_msg_str_to_unicode():
        msg = populate_instance(r'forty two', unicode())
        print("msg is of type {0}".format(type(msg)))
        assert isinstance(msg, unicode)
        assert msg == u'forty two'


    def test_populate_msg_unicode_to_unicode():
        msg = populate_instance(u'forty two', unicode())
        print("msg is of type {0}".format(type(msg)))
        assert isinstance(msg, unicode)
        assert msg == u'forty two'

if sys.version_info < (3,0):
    def test_populate_msg_unicode_to_str_error():
        with pytest.raises(FieldTypeMismatchException):
            populate_instance(u'forty two', str())
else:  # python3
    def test_populate_msg_str_to_bytes_error():
        with pytest.raises(FieldTypeMismatchException):
            populate_instance(u'forty two', bytes())


def test_populate_msg_list():
    msg = populate_instance([False, 42, 3.1415, r'fortytwo', u'forty two'], list())
    print("msg is of type {0}".format(type(msg)))
    assert isinstance(msg, list)
    assert msg == [False, 42, 3.1415, r'fortytwo', u'forty two']


def test_populate_msg_list_to_tuple_error():
    with pytest.raises(FieldTypeMismatchException):
        populate_instance([False, 42, 3.1415, r'fortytwo', u'forty two'], tuple())


def test_populate_msg_tuple_to_tuple():
    msg = populate_instance((False, 42, 3.1415, r'fortytwo', u'forty two'), tuple())
    print("msg is of type {0}".format(type(msg)))
    assert isinstance(msg, tuple)
    assert msg == (False, 42, 3.1415, r'fortytwo', u'forty two')


def test_populate_msg_tuple_to_list():
    msg = populate_instance((False, 42, 3.1415, r'fortytwo', u'forty two'), list())
    print("msg is of type {0}".format(type(msg)))
    assert isinstance(msg, list)
    assert msg == [False, 42, 3.1415, r'fortytwo', u'forty two']


def test_populate_msg_dict_to_status():
    msg = populate_instance(
        {"error": True, "code": 7, "message": "Actual Error"},
        StatusMsg(error=False, code=42, message="Not an error")
    )
    print("msg is of type {0}".format(type(msg)))
    assert isinstance(msg, StatusMsg)
    assert msg.error
    assert msg.code == 7
    assert msg.message == "Actual Error"


def test_populate_msg_dict_to_status_error():

    with pytest.raises(NonexistentFieldException):
        msg = populate_instance(
            {"error": True, "code": 7, "message": "Actual Error", "non-existent": "field"},
            StatusMsg(error=False, code=42, message="Not an error")
        )


    ###### EXTRACT #######

def test_extract_msg_bool_true():
    msg = populate_instance(True, bool())
    data = extract_values(msg)
    assert isinstance(data, bool)
    assert data


def test_extract_msg_bool_false():
    msg = populate_instance(False, bool())
    data = extract_values(msg)
    assert isinstance(data, bool)
    assert not data


def test_extract_msg_int_to_int():
    msg = populate_instance(42, int())
    data = extract_values(msg)
    assert isinstance(data, int)
    assert data == 42


def test_extract_msg_int_to_float():
    msg = populate_instance(42, float())
    data = extract_values(msg)
    assert isinstance(data, float)
    assert data == 42.0


def test_extract_msg_float():
    msg = populate_instance(3.1415, float())
    data = extract_values(msg)
    assert isinstance(data, float)
    assert data == 3.1415


if sys.version_info >= (3, 0):
    def test_extract_msg_bytes_to_bytes():
        msg = populate_instance(b'forty two', bytes())
        data = extract_values(msg)
        assert isinstance(data, bytes)
        assert data == b'forty two'


def test_extract_msg_str_to_str():
    msg = populate_instance(r'forty two', str())
    data = extract_values(msg)
    assert isinstance(data, str)
    assert data == r'forty two'


if sys.version_info < (3, 0):
    def test_extract_msg_str_to_unicode():
        msg = populate_instance(r'forty two', unicode())
        data = extract_values(msg)
        assert isinstance(data, unicode)
        assert data == u'forty two'


    def test_extract_msg_unicode_to_unicode():
        msg = populate_instance(u'forty two', unicode())
        data = extract_values(msg)
        assert isinstance(data, unicode)
        assert data == u'forty two'


def test_extract_msg_list():
    msg = populate_instance([False, 42, 3.1415, r'fortytwo', u'forty two'], list())
    data = extract_values(msg)
    assert isinstance(data, list)
    assert data == [False, 42, 3.1415, r'fortytwo', u'forty two']


def test_extract_msg_tuple_to_tuple():
    msg = populate_instance((False, 42, 3.1415, r'fortytwo', u'forty two'), tuple())
    data = extract_values(msg)
    assert isinstance(data, tuple)
    assert data == (False, 42, 3.1415, r'fortytwo', u'forty two')


def test_extract_msg_tuple_to_list():
    msg = populate_instance((False, 42, 3.1415, r'fortytwo', u'forty two'), list())
    data = extract_values(msg)
    assert isinstance(msg, list)
    assert msg == [False, 42, 3.1415, r'fortytwo', u'forty two']


def test_extract_msg_dict_to_status():
    msg = populate_instance(
        {"error": True, "code": 7, "message": "Actual Error"},
        StatusMsg(error=False, code=42, message="Not an error")
    )
    data = extract_values(msg)
    assert isinstance(data, StatusMsg)
    assert data.error
    assert data.code == 7
    assert data.message == "Actual Error"

# Just in case we run this directly
if __name__ == '__main__':
    import pytest
    pytest.main([
        '-s', __file__,
])
