import pytest
from vector import Vector


@pytest.fixture
def vector_obj1():
    return Vector(1, 2, 3)


@pytest.fixture
def vector_obj2():
    return Vector(1, 2, 3)


@pytest.fixture
def vector_obj3():
    return Vector(2, 4, 5)


def test_vector_creation(vector_obj1):
    assert vector_obj1.x == 1
    assert vector_obj1.y == 2
    assert vector_obj1.z == 3


def test_equal_vectors(vector_obj1, vector_obj2, vector_obj3):
    assert vector_obj1 == vector_obj2
    assert vector_obj1 != vector_obj3


def test_addition_vectors(vector_obj1, vector_obj2):
    assert vector_obj1 + vector_obj2 == Vector(2, 4, 6)


def test_sub_vectors():
    v1 = Vector(2, 3, 4)
    v2 = Vector(1, 2, 3)
    assert v1 - v2 == Vector(1, 1, 1)


def test_mul_vectors(vector_obj1):
    result1 = vector_obj1 * 2
    result2 = 2 * vector_obj1
    assert result1 == Vector(2, 4, 6)
    assert result2 == Vector(2, 4, 6)


def test_len_vector(vector_obj1):
    assert len(vector_obj1) == 6


def test_neg_vector(vector_obj1):
    assert -vector_obj1 == Vector(-1, -2, -3)


def test_bool_vector(vector_obj1):
    v2 = Vector(0, 0, 0)
    assert bool(vector_obj1)
    assert not bool(v2)
