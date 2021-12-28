import pytest

def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()

# dilajankan dengan perintah pytest
# --- HASILNYA ---

# (py39-nlp) C:\Users\DeLL\My Documents\github\zimera\novice\02-02\pytest>pytest
# ================================================= test session starts =================================================
# platform win32 -- Python 3.9.7, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
# rootdir: C:\Users\DeLL\My Documents\github\zimera\novice\02-02\pytest
# plugins: anyio-2.2.0, hypothesis-6.32.1
# collected 2 items

# test_sample.py .                                                                                                 [ 50%]
# test_sysexit.py .                                                                                                [100%]

# ================================================== 2 passed in 0.05s ==================================================