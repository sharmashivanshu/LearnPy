class Log:
    __instance = None

    @classmethod
    def get_log_instance(cls):
        if not cls.__instance:
            cls.__instance = Log()
        return cls.__instance


if __name__ == "__main__":
    l = Log()
    print(l)

    lo = Log()
    print(lo)
