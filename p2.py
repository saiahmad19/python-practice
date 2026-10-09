def outer():
    def inner():
        print("hello from inner")
    return inner

result = outer
thing = result()
thing()