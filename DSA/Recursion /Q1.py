#counting in reverse
def reverse(n):
    if n==0:
        return
    else:
        print(n)
        return reverse(n-1)
reverse(5)
