class FrenchLocalizer:

    def __init__(self):
        self.translation = {"car": "voiture", "bike": "bicyclette", "cycle": "cyclette"}

    def localize(self, msg):
        return self.translation.get(msg)


class SpanishLocalizer:
    def __init__(self):
        self.translation = {"car": "coche", "bike": "bicicleta", "cycle": "ciclo"}

    def localize(self, msg):
        return self.translation.get(msg)


class English:

    def localize(self, msg):
        return msg


def factory(language):
    localizers = {
        "English": English,
        "Spanish": SpanishLocalizer,
        "French": FrenchLocalizer
    }
    return localizers[language]()


if __name__ == "__main__":
    f = factory("French")
    e = factory("English")
    s = factory("Spanish")

    message = ["car", "bike", "cycle"]

    for msg in message:
        print(f.localize(msg=msg))
        print(e.localize(msg=msg))
        print(s.localize(msg=msg))


