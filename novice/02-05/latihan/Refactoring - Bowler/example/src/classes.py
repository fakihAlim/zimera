import logging

logger = logging.getLogger(__name__)


class FooClass:
    def __init__(self, value):
        self.value = value

    def increment(self, auto_param):
        logger.info(f"FooClass.run<value={self.value}>")
        return self.value + 1
