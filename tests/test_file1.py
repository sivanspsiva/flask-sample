from typing import Dict

from app import add, multi, diff
import pytest


@pytest.fixture()
def data() -> Dict:
    user = "siva"
    return {"user": user}


@pytest.fixture
def first_entry():
    return "a"


@pytest.fixture
def order(first_entry):
    return []


@pytest.fixture(autouse=True)
def append_first(order, first_entry):
    return order.append(first_entry)


def test_string_only(order, first_entry):
    print(order)
    print([first_entry])
    assert order == [first_entry]


def test_string_and_int(order, first_entry):
    order.append(2)
    assert order == [first_entry, 2]


class TestMathOperations:

    def test_add(self, data):
        if data["user"] == "siva":
            res = add(5)
            assert res == 7
        else:
            assert False

    def test_multi(self):
        res = multi(5)
        assert res == 15

    def test_diff(self):
        res = diff(5)
        assert res == 3
