# content of test_class_demo.py
class TestClassDemoInstance:
    def test_one(self):
        assert 0

    def test_two(self):
        assert 0


# --- HASILNYA ---

# (py39-nlp) C:\Users\DeLL\My Documents\github\zimera\novice\02-02\pytest>pytest -k TestClassDemoInstance -q
# FF                                                                                                               [100%]
# ====================================================== FAILURES =======================================================
# ___________________________________________ TestClassDemoInstance.test_one ____________________________________________

# self = <test_class_demo.TestClassDemoInstance object at 0x00000182BF78AAF0>

#     def test_one(self):
# >       assert 0
# E       assert 0

# test_class_demo.py:4: AssertionError
# ___________________________________________ TestClassDemoInstance.test_two ____________________________________________

# self = <test_class_demo.TestClassDemoInstance object at 0x00000182BF7904C0>

#     def test_two(self):
# >       assert 0
# E       assert 0

# test_class_demo.py:7: AssertionError
# =============================================== short test summary info ===============================================
# FAILED test_class_demo.py::TestClassDemoInstance::test_one - assert 0
# FAILED test_class_demo.py::TestClassDemoInstance::test_two - assert 0
# 2 failed, 4 deselected in 0.23s
