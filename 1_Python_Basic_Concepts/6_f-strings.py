# String formatting can be done in python using the format method.

txt = "For only {price:.2f} dollars!"
print(txt.format(price=49))


# f-strings in python - used to format the string. It evaluates at runtime

val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")