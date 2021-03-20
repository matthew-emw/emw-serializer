from emw_serializer import JsonSerializer


class Gakk:
    def __init__(self):
        self.a = 'a'
        self.b = 5


serializer = JsonSerializer()
thing_to_serialize = Gakk()
json = serializer.serialize(thing_to_serialize)
print(json)
