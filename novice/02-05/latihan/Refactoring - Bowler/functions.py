def run(val1, val2, auto_param):
    logger.info("run")

    foo = FooClass(value=val2)
    return val1 + foo.increment()
