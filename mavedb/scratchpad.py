import inspect


def print_args_kwargs(func):
    def wrapper(*args, **kwargs):
        # A way to fetch default kwargs in a wrapped function
        signature = inspect.signature(func)
        kwargs_nuovo = {
            k: v.default for k, v in signature.parameters.items() if v.default is not inspect.Parameter.empty
        }
        print(kwargs)
        print(kwargs_nuovo)
        return func(*args, **kwargs)

    return wrapper


@print_args_kwargs
def say_hi(text="hi"):
    return text


say_hi()
