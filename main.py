def twice(func):
    def new_func(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return new_func


@twice
def print_name(your_name: str) -> bool:
    print('Hi,', your_name)
    return True


print_name('denis')
