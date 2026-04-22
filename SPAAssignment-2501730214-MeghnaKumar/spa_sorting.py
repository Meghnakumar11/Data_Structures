import time
import random
import copy
import sys


# Sorting Algorithms
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # stable
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

    return arr


# Timing Function
def measure_time(sort_func, arr):
    arr_copy = copy.deepcopy(arr)

    start = time.perf_counter()

    if sort_func == quick_sort:
        quick_sort(arr_copy, 0, len(arr_copy) - 1)
    else:
        arr_copy = sort_func(arr_copy)

    end = time.perf_counter()

    return round((end - start) * 1000, 4)  # ms


# Dataset Generator
def generate_datasets(sizes, seed=42):
    datasets = {}
    random.seed(seed)

    for n in sizes:
        rand_list = [random.randint(1, 100000) for _ in range(n)]

        datasets[n] = {
            'random': rand_list,
            'sorted': sorted(rand_list),
            'reverse': sorted(rand_list, reverse=True)
        }

    return datasets


# Run Experiments
def run_experiments(datasets, sizes, file):
    input_types = ['random', 'sorted', 'reverse']

    header = f"{'Size':>7} | {'Input Type':>12} | {'Insertion Sort (ms)':>20} | {'Merge Sort (ms)':>16} | {'Quick Sort (ms)':>16}"
    divider = "-" * len(header)

    print(divider)
    print(header)
    print(divider)

    file.write(divider + "\n")
    file.write(header + "\n")
    file.write(divider + "\n")

    for n in sizes:
        for itype in input_types:
            arr = datasets[n][itype]

            t_ins = measure_time(insertion_sort, arr)
            t_merge = measure_time(merge_sort, arr)
            t_quick = measure_time(quick_sort, arr)

            row = f"{n:>7} | {itype:>12} | {t_ins:>20} | {t_merge:>16} | {t_quick:>16}"

            print(row)
            file.write(row + "\n")

    print(divider)
    file.write(divider + "\n")


# Main Execution
if __name__ == "__main__":
    sys.setrecursionlimit(50000)

    with open("output.txt", "w") as file:

    
        # Correctness Check
        print("=" * 60)
        print("CORRECTNESS VERIFICATION")
        print("=" * 60)

        file.write("=" * 60 + "\n")
        file.write("CORRECTNESS VERIFICATION\n")
        file.write("=" * 60 + "\n")

        test_input = [5, 2, 9, 1, 5, 6]
        expected = [1, 2, 5, 5, 6, 9]

        ins_result = insertion_sort(list(test_input))
        merge_result = merge_sort(list(test_input))
        qs_arr = list(test_input)
        quick_sort(qs_arr, 0, len(qs_arr) - 1)

        results_text = (
            f"\nInput:          {test_input}\n"
            f"Expected:       {expected}\n"
            f"Insertion Sort: {ins_result}  {'PASS' if ins_result == expected else 'FAIL'}\n"
            f"Merge Sort:     {merge_result}  {'PASS' if merge_result == expected else 'FAIL'}\n"
            f"Quick Sort:     {qs_arr}  {'PASS' if qs_arr == expected else 'FAIL'}\n"
        )

        print(results_text)
        file.write(results_text + "\n")

     
        # Performance Measurement
        print("=" * 60)
        print("PERFORMANCE MEASUREMENT (times in milliseconds)")
        print("=" * 60 + "\n")

        file.write("=" * 60 + "\n")
        file.write("PERFORMANCE MEASUREMENT (times in milliseconds)\n")
        file.write("=" * 60 + "\n\n")

        sizes = [1000, 5000, 10000]
        datasets = generate_datasets(sizes)

        run_experiments(datasets, sizes, file)

    print("\nExecution complete. Results saved in output.txt")