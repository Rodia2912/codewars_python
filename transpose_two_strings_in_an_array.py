def transpose_two_strings(arr):
    a, b = arr
    return "\n".join(
        f"{a[i] if i < len(a) else ' '} {b[i] if i < len(b) else ' '}"
        for i in range(max(len(a), len(b))))
    print(transpose_two_strings)