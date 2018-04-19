import pickle

from pyros_common import exceptions


def test_pyros_exception_methods():

    exc = exceptions.PyrosException(42, "foo")

    assert str(exc).startswith("An Exception PyrosException(42, 'foo') was thrown in Pyros process")
    assert repr(exc) == "PyrosException(42, 'foo')"


def test_pyros_exception_pickle():
    exc = exceptions.PyrosException(42, "foo")

    pbuf = pickle.dumps(exc)
    pexc = pickle.loads(pbuf)

    assert str(pexc).startswith("An Exception PyrosException(42, 'foo') was thrown in Pyros process")
    assert repr(pexc) == "PyrosException(42, 'foo')"


class PyrosTestExcept(exceptions.PyrosException):
    def __init__(self, myarg1, myarg2):
        self.myarg1 = myarg1
        self.myarg2 = myarg2
        super(PyrosTestExcept, self).__init__(myarg1, myarg2)

    @property
    def message(self):
        return "TestException message {0} and {1}".format(self.myarg1, self.myarg2)


def test_derived_pyros_exception_methods():

    exc = PyrosTestExcept(42, 'bar')
    assert str(exc) == "TestException message 42 and bar"
    assert repr(exc) == "PyrosTestExcept(42, 'bar')"


def test_derived_pyros_exception_pickle():

    exc = PyrosTestExcept(42, 'bar')

    pbuf = pickle.dumps(exc)
    pexc = pickle.loads(pbuf)

    assert str(pexc) == "TestException message 42 and bar"
    assert repr(pexc) == "PyrosTestExcept(42, 'bar')"
