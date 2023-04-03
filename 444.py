import time


def time_it(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"Time elapsed: {end_time - start_time:.6f} seconds")
    return result


def test_time_it():
    def func():
        time.sleep(1)
        return "Done"

    assert time_it(func) == "Done"


test_time_it()
