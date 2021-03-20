from enum import Enum

from emw_serializer import JsonSerializer


class MyEnum(Enum):
    Good = "Good"
    Bad = "Bad"


class ObjectProperties:
    def __init__(self):
        self.a = True
        self.b = 5.5
        self.c = 5
        self.d = None
        self.e = 'hello'
        self.f = ''
        self.g = MyEnum.Good


class ClassProperties:
    a = True
    b = 5.5
    c = 5
    d = None
    e = 'hello'
    f = ''
    g = MyEnum.Good

    def __init__(self):
        pass


class Method:
    def __init__(self):
        self.a = 5

    def a_method(self):
        return 7


class InheritanceObjectProperties(ObjectProperties):
    def __init__(self):
        super().__init__()


class InheritanceClassProperties(ClassProperties):
    def __init__(self):
        super().__init__()


class InheritanceMethod(Method):
    def __init__(self):
        super().__init__()


class PropertyDecorator:
    def __init__(self):
        self.__nope = 'nope'

    @property
    def nope(self):
        return self.__nope


class PropertyFunction:
    def __init__(self):
        self.__nope = 'nope'

    def get_nope(self):
        return self.__nope

    nope = property(get_nope)


class Nested:
    def __init__(self):
        self.a = 5
        self.b = ObjectProperties()
        self.c = [1, 'hello']


def test_object_properties_json():
    a = ObjectProperties()
    s = JsonSerializer()
    r = s.serialize(a)
    assert r == '{"a": true, "b": 5.5, "c": 5, "d": null, "e": "hello", "f": "", "g": "Good"}'


def test_class_properties_json():
    a = ClassProperties()
    s = JsonSerializer()
    r = s.serialize(a)
    assert r == '{"a": true, "b": 5.5, "c": 5, "d": null, "e": "hello", "f": "", "g": "Good"}'


def test_method_json():
    a = Method()
    s = JsonSerializer()
    r = s.serialize(a)
    assert r == '{"a": 5}'


def test_inheritance_object_properties_json():
    a = InheritanceObjectProperties()
    s = JsonSerializer()
    r = s.serialize(a)
    assert r == '{"a": true, "b": 5.5, "c": 5, "d": null, "e": "hello", "f": "", "g": "Good"}'


def test_inheritance_class_properties_json():
    a = InheritanceClassProperties()
    s = JsonSerializer()
    r = s.serialize(a)
    assert r == '{"a": true, "b": 5.5, "c": 5, "d": null, "e": "hello", "f": "", "g": "Good"}'


def test_inheritance_method_json():
    a = InheritanceMethod()
    s = JsonSerializer()
    r = s.serialize(a)
    assert r == '{"a": 5}'


def test_property_decorator_json():
    a = PropertyDecorator()
    s = JsonSerializer()
    r = s.serialize(a)
    assert r == '{"nope": "nope"}'


def test_property_function_json():
    a = PropertyFunction()
    s = JsonSerializer()
    r = s.serialize(a)
    assert r == '{"nope": "nope"}'


def test_nested_json():
    a = Nested()
    s = JsonSerializer()
    r = s.serialize(a)
    assert r == '{"a": 5, "b": {"a": true, "b": 5.5, "c": 5, "d": null, "e": "hello", "f": "", "g": "Good"}, "c": [1, "hello"]}'
