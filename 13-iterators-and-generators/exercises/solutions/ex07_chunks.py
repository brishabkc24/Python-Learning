"""Write chunks(items, size), a generator that yields lists of size items from any iterable."""


def chunks(items, size):
    chunk = []
    for item in items:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:                   # the last group may be shorter
        yield chunk


for group in chunks(range(1, 11), 3):
    print(group)
