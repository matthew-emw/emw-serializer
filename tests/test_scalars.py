from emw_serializer import JsonSerializer, Serializer


def test_bool_json():
    a = True
    s = JsonSerializer()
    r = s.serialize(a)
    assert r == 'true'


def test_bool():
    a = True
    s = Serializer()
    r = s.serialize(a)
    assert r is True


def test_float_json():
    a = 5.5
    s = JsonSerializer()
    r = s.serialize(a)
    assert r == '5.5'


def test_float():
    a = 5.5
    s = Serializer()
    r = s.serialize(a)
    assert r == 5.5


def test_int_json():
    a = 5
    s = JsonSerializer()
    r = s.serialize(a)
    assert r == '5'


def test_int():
    a = 5
    s = Serializer()
    r = s.serialize(a)
    assert r == 5


def test_string_json():
    a = 'hello'
    s = JsonSerializer()
    r = s.serialize(a)
    assert r == '"hello"'


def test_string():
    a = 'hello'
    s = Serializer()
    r = s.serialize(a)
    assert r == 'hello'
