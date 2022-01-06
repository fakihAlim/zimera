import logging

from src.functions import run


def test_run(caplog):
    assert run(1, 1, "default_value") == 3

    assert caplog.record_tuples == [
        ("src.functions", logging.INFO, "run"),
        ("src.classes", logging.INFO, "FooClass.run<value=1>"),
    ]
