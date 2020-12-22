def reverse_string(text):
    st = []
    for char in text:
        st.append(char)
    result = []

    while st:
        ch = st.pop()
        result.append(ch)
    return "".join(result)


print(reverse_string(input()))
