from functools import lru_cache


@lru_cache(maxsize=3)
def add(a, b):
    return a + b


print(add(1, 2))  # Calculates and caches result
print(add(1, 2))  # Retrieves result from cache
