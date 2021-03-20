import json

from emw_serializer import JsonSerializer, Serializer


def test_list_json():
    a = [True, 5.5, 5, None, 'hello']
    s = JsonSerializer()
    r = s.serialize(a)
    assert r == '[true, 5.5, 5, null, "hello"]'


def test_list():
    a = [True, 5.5, 5, None, 'hello']
    s = Serializer()
    r = s.serialize(a)
    assert r == [True, 5.5, 5, None, 'hello']


def test_set_json():
    a = {True, 5.5, 5, None, 'hello'}
    s = JsonSerializer()
    r = s.serialize(a)
    # sets are unordered, and, it turns out, not deterministic
    # TODO bit of a bodge
    r = json.loads(r)
    r = sorted([str(x) for x in r])
    assert r == ['5', '5.5', 'None', 'True', 'hello']


def test_set():
    a = {True, 5.5, 5, None, 'hello'}
    s = Serializer()
    r = s.serialize(a)
    # sets are unordered, and, it turns out, not deterministic
    # TODO bit of a bodge
    r = sorted([str(x) for x in r])
    assert r == ['5', '5.5', 'None', 'True', 'hello']
