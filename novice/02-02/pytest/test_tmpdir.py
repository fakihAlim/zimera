def test_needsfiles(tmpdir):
    print(tmpdir)
    assert 0

# --- HASILNYA ---

# (py39-nlp) C:\Users\DeLL\My Documents\github\zimera\novice\02-02\pytest>pytest -q test_tmpdir.py
# F                                                                                                                [100%]
# ====================================================== FAILURES =======================================================
# ___________________________________________________ test_needsfiles ___________________________________________________

# tmpdir = local('C:\\Users\\DeLL\\AppData\\Local\\Temp\\pytest-of-DeLL\\pytest-0\\test_needsfiles0')

#     def test_needsfiles(tmpdir):
#         print(tmpdir)
# >       assert 0
# E       assert 0

# test_tmpdir.py:3: AssertionError
# ------------------------------------------------ Captured stdout call -------------------------------------------------
# C:\Users\DeLL\AppData\Local\Temp\pytest-of-DeLL\pytest-0\test_needsfiles0
# =============================================== short test summary info ===============================================
# FAILED test_tmpdir.py::test_needsfiles - assert 0
# 1 failed in 0.20s