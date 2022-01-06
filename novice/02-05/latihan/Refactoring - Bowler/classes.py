class FooClass:
    def __init__(self, value):
        self.value = value

    def increament(self):
        logger.info(f"FooClass.run<value={self.value}>")
        return self.value + 1
