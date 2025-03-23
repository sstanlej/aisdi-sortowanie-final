
import argparse
import sys
import matplotlib.pyplot as plt

from utils import load_words_from_file, test_sort_implementations
from sort_methods import bubble_sort, selection_sort, quick_sort, merge_sort, insertion_sort

parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, help="Path to file with input data")
parser.add_argument("--tests", action="store_true", help="Run sorting algorithms tests")
args = parser.parse_args()

sys.setrecursionlimit(100000)

path = args.path

to_sort = load_words_from_file(path)

functions = (
    ('Bubble sort', bubble_sort),
    ('Selection sort', selection_sort),
    ('Quick sort', quick_sort),
    ('Merge sort', merge_sort),
    ('Insertion sort', insertion_sort)
)

if args.tests:
    tests_result, message = test_sort_implementations(to_sort[:1000], [bubble_sort, selection_sort, quick_sort])
    print("[OK] Tests passed" if tests_result else f"[ERROR] Tests failed: {message}")
    if not tests_result:
        sys.exit()

for name, sort_function in functions:
    x_axis = []
    y_axis = []
    for limit in range(0, 25001, 1000):
        _, time = sort_function(to_sort[:limit])
        x_axis.append(limit)
        y_axis.append(time)
    plt.plot(x_axis, y_axis, marker='o', label=name)

plt.legend()
plt.xlabel("Number of elements")
plt.ylabel("Time [s]")

plt.savefig('output.png')
