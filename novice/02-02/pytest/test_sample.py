def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


# --- HASILNYA ---

# (py39-nlp) C:\Users\DeLL\My Documents\github\zimera\novice\02-02\pytest>pytest test_sample.py
# ================================================= test session starts =================================================
# platform win32 -- Python 3.9.7, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
# rootdir: C:\Users\DeLL\My Documents\github\zimera\novice\02-02\pytest
# plugins: anyio-2.2.0, hypothesis-6.32.1
# collected 1 item

# test_sample.py .                                                                                                 [100%]

# ================================================== 1 passed in 0.03s ==================================================
