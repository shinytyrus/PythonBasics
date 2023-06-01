from basics import basics_integers_and_floats


# content of test_sample.py
def func(x):
    if x == 3:
        return x
    else:
        return x + 1


def test_answer():
    assert func(3) == 5


def test_answer_two():
    assert basics_integers_and_floats.add_to(3) == 4
