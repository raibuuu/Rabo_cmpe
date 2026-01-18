from math import sqrt, pi
import sys
import time

def run_cli():
    print("==============================================================")
    print("3D SHAPE VOLUME CALCULATOR (CLI Mode)")
    print("==============================================================")
    print("Available Shapes:")
    print("1. Cuboid (Rectangular Prism)")
    print("2. Pyramid (Right Rectangular)")
    print("3. Cylinder")
    print("4. Sphere")
    print("5. Cone")
    print("6. Ellipsoid")
    print("7. Torus (Donut)")
    print("8. Hexagonal Prism")
    print("9. Exit")

    while True:
        try:
            choice = input("Select shape (1-9): ")
            if choice == "9":
                print("POWER OFF")
                time.sleep(1)
                break
            if choice not in ("1", "2", "3", "4", "5", "6", "7", "8"):
                print("Invalid choice! Please enter 1-9.")
                continue

            # Get unit
            unit = input("Enter unit (cm, m, inches, etc.): ")

            # Calculate based on choice
            if choice == "1":
                length = float(input(f"Enter Length ({unit}): "))
                width = float(input(f"Enter Width ({unit}): "))
                height = float(input(f"Enter Height ({unit}): "))
                volume = length * width * height
                shape_name = "Cuboid"

            elif choice == "2":
                length = float(input(f"Enter Length ({unit}): "))
                width = float(input(f"Enter Width ({unit}): "))
                height = float(input(f"Enter Height ({unit}): "))
                volume = (length * width * height) / 3
                shape_name = "Pyramid"

            elif choice == "3":
                radius = float(input(f"Enter Radius ({unit}): "))
                height = float(input(f"Enter Height ({unit}): "))
                volume = pi * (radius ** 2) * height
                shape_name = "Cylinder"

            elif choice == "4":
                radius = float(input(f"Enter Radius ({unit}): "))
                volume = (4 / 3) * pi * (radius ** 3)
                shape_name = "Sphere"

            elif choice == "5":
                radius = float(input(f"Enter Radius ({unit}): "))
                height = float(input(f"Enter Height ({unit}): "))
                volume = (pi * (radius ** 2) * height) / 3
                shape_name = "Cone"

            elif choice == "6":
                a = float(input(f"Enter a axis ({unit}): "))
                b = float(input(f"Enter b axis ({unit}): "))
                c = float(input(f"Enter c axis ({unit}): "))
                volume = (4 / 3) * pi * a * b * c
                shape_name = "Ellipsoid"

            elif choice == "7":
                major_r = float(input(f"Enter Major Radius ({unit}): "))
                print("Make sure that Major Radius > Minor Radius")
                minor_r = float(input(f"Enter Minor Radius ({unit}): "))
                volume = (2 * pi * major_r) * (pi * minor_r ** 2)
                shape_name = "Torus"

            elif choice == "8":
                edge = float(input(f"Enter Base edge ({unit}): "))
                height = float(input(f"Enter Height ({unit}): "))
                volume = (3 * sqrt(3) / 2) * (edge ** 2) * height
                shape_name = "Hexagonal Prism"

            print(f"✓ Volume of {shape_name}: {volume:.4f} {unit}³")
            print("==============================================================")

        except ValueError:
            print("Invalid input! Please enter valid numbers.")


def main():
    print("Volume Calculator")
    print("1. Open the Calculator")
    print("2. Exit")

    while True:
        choice = input("Select mode (1-2): ")
        if choice == "1":
            run_cli()
        elif choice == "2":
            print("POWER OFF")
            time.sleep(1)
            sys.exit()
        else:
            print("Invalid input! Please enter valid numbers.")


if __name__ == "__main__":
    main()
