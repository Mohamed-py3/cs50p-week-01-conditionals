expression = input("Expression: ").strip()
x_str, op, z_str = expression.split(" ")

x = int(x_str)
z = int(z_str)

if op == "+":
    result = x + z
elif op == "-":
    result = x - z
elif op == "*":
    result = x * z
elif op == "/":
    result = x / z

print(f"{result:.1f}")