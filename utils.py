
import gc
import time


def load_words_from_file(path, number_of_words=None):
    _result = []
    with open(path, 'r') as file:
        for line in file:
            for word in line.split():
                if number_of_words is not None and len(_result) >= number_of_words:
                    return _result
                _result.append(word)
    return _result

def measure_sorting_time(func):
    def wrapper(to_sort):
        _list = to_sort.copy()

        gc_old = gc.isenabled()
        gc.disable()
        timer_start = time.process_time()
        wrapped_result = func(_list)
        timer_stop = time.process_time()
        if gc_old:
            gc.enable()
        return wrapped_result, timer_stop - timer_start
    wrapper.__name__ = func.__name__
    return wrapper


def test_sort_implementations(test_data, functions):
    """ All functions should have same result, equal to built-in Python sorted() method.
    """

    _test_data = (
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [],
        [1, 1, 1, 1],
        [1],
        [1, -1],
        test_data,
    )

    is_positive = True
    message = None
    for data in _test_data:
        expected_result = sorted(data)
        for function in functions:
            result, _ = function(data)
            if expected_result != result:
                is_positive = False
                message = f'{function.__name__} failed.'
    return is_positive, message
    