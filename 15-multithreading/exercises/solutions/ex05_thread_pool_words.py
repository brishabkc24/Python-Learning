"""Use ThreadPoolExecutor.map to measure word lengths and submit to add up two lists of marks."""

from concurrent.futures import ThreadPoolExecutor

WORDS = ["python", "thread", "lock", "executor", "pool"]
MATHS_MARKS = [85, 92, 67, 78]
SCIENCE_MARKS = [88, 59, 73, 95]

with ThreadPoolExecutor(max_workers=2) as pool:
    for word, length in zip(WORDS, pool.map(len, WORDS)):
        print(f"{word} -> {length}")

    maths_future = pool.submit(sum, MATHS_MARKS)
    science_future = pool.submit(sum, SCIENCE_MARKS)
    print("Total maths marks:", maths_future.result())
    print("Total science marks:", science_future.result())
