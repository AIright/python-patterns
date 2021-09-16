import threading


class ChocolateFactory:
    _unique_instance: object = None
    lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        # in statically-typed OOP languages use private constructor + getInstance() class method
        if cls._unique_instance:  # if the instance exists then return immediately
            return cls._unique_instance

        with cls.lock:  # a thread safe creation of the instance
            if not cls._unique_instance:  # check if another thread has already created the instance
                cls._unique_instance = super(ChocolateFactory, cls).__new__(cls, *args, **kwargs)
        return cls._unique_instance

    def __init__(self):
        self.boiled = False
        self.empty = True

    def fill(self):
        if self.empty:
            self.empty = False
            self.boiled = False

    def drain(self):
        if not self.empty and self.boiled:
            self.empty = True

    def boil(self):
        if not self.empty and not self.boiled:
            self.boiled = True
