def area(x):
    area = 3.14159 * x**2
    return area

def main():
    num = float(input())
    a = area(num)
    print(f"A={a:.4f}")

main()