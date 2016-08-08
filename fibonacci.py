def memoize(function):
    memo = {}
    def wrapper(args):
        if args in memo:
            return memo[args]
        else:
            rv = function(args)
            memo[args] = rv
            return rv
    return wrapper
    
@memoize
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)