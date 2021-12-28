class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")

# --- HASILNYA ---

# (py39-nlp) C:\Users\DeLL\My Documents\github\zimera\novice\02-02\pytest>pytest -q test_class.py
# .F                                                                                                               [100%]
# ====================================================== FAILURES =======================================================
# _________________________________________________ TestClass.test_two __________________________________________________

# self = <test_class.TestClass object at 0x000002C518A04A00>

#     def test_two(self):
#         x = "hello"
# >       assert hasattr(x, "check")
# E       AssertionError: assert False
# E        +  where False = hasattr('hello', 'check')

# test_class.py:8: AssertionError
# =============================================== short test summary info ===============================================
# FAILED test_class.py::TestClass::test_two - AssertionError: assert False
# 1 failed, 1 passed in 0.17s