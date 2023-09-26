def generate_dict(n):
    return {x: x*x for x in range(1, n+1)}
n = 5
result = generate_dict(n)
print(result)