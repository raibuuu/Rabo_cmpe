from math import sqrt, pi

print("=" * 50)
print("3D SHAPE VOLUME CALCULATOR")
print("=" * 50)
print("Select operation.")
print("1. Cuboid (Rectangular Prism)")
print("2. Pyramid (Right Rectangular)")
print("3. Cylinder")
print("4. Sphere")
print("5. Cone")
print("6. Ellipsoid")
print("7. Torus (Donut)")
print("8. Hexagonal Prism")
print("9. Exit")
print("=" * 50)

while True:
    choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ")
    print("-" * 30)

    if choice == "9":
        print("Goodbye!")
        break

    # Get unit input
    if choice in ("1", "2", "3", "4", "5", "6", "7", "8"):
        unit = input("Enter unit (cm, m, inches, ft, mm, etc.): ").strip()
        print("-" * 30)

    if choice == "1":
        num1 = float(input(f"Enter Length ({unit}): "))
        num2 = float(input(f"Enter Width ({unit}): "))
        num3 = float(input(f"Enter Height ({unit}): "))
        volume = num1 * num2 * num3
        print(f"The volume of the Cuboid is: {volume:.2f} {unit}³")

    elif choice == "2":
        num1 = float(input(f"Enter Length ({unit}): "))
        num2 = float(input(f"Enter Width ({unit}): "))
        num3 = float(input(f"Enter Height ({unit}): "))
        volume = (num1 * num2 * num3) / 3
        print(f"The volume of the Pyramid is: {volume:.2f} {unit}³")

    elif choice == "3":
        R = float(input(f"Enter the radius ({unit}): "))
        H = float(input(f"Enter the height ({unit}): "))
        volume = pi * (R ** 2) * H
        print(f"The volume of the Cylinder is: {volume:.2f} {unit}³")

    elif choice == "4":
        R = float(input(f"Enter the radius ({unit}): "))
        volume = (4 / 3) * pi * (R ** 3)
        print(f"The volume of the Sphere is: {volume:.2f} {unit}³")

    elif choice == "5":
        R = float(input(f"Enter the radius ({unit}): "))
        H = float(input(f"Enter the height ({unit}): "))
        volume = (pi * (R ** 2) * H) / 3
        print(f"The volume of the Cone is: {volume:.2f} {unit}³")

    elif choice == "6":
        Axs = float(input(f"a axis ({unit}): "))
        Bxs = float(input(f"b axis ({unit}): "))
        Cxs = float(input(f"c axis ({unit}): "))
        volume = (4 / 3) * pi * Axs * Bxs * Cxs
        print(f"The volume of the Ellipsoid is: {volume:.2f} {unit}³")

    elif choice == "7":
        R = float(input(f"Enter the Major Radius ({unit}): "))
        print("Make sure that Major Radius > Minor Radius")
        r = float(input(f"Enter the Minor Radius ({unit}): "))
        volume = (2 * pi * R) * (pi * r ** 2)
        print(f"The volume of the Torus is: {volume:.2f} {unit}³")

    elif choice == "8":
        a = float(input(f"Enter the Base edge ({unit}): "))
        h = float(input(f"Enter the Height ({unit}): "))
        volume = (3 * sqrt(3) / 2) * (a ** 2) * h
        print(f"The volume of the Hexagonal Prism is: {volume:.2f} {unit}³")

    else:
        print("Invalid Input! Please enter 1-8 or 9 to exit.")

    print("=" * 50)