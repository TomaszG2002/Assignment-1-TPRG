'''
TPRG 2131 Fall 2024 Assignment 1, 
October 16th, 2024
Tomasz Giedrojc
100793058
This is my own work 

'''

import math  # Importing the math module to access mathematical constants and functions

# Function to calculate the area of a rectangle
def rectangle_area(length, width, show_equation=False):
    """Calculate the area of a rectangle (in m²)."""
    area = round(length * width, 1)  # Area formula: length * width, rounded to 1 decimal place
    if show_equation:
        print(f"{length} * {width} = {area} (length * width = area)")  # Print detailed equation if enabled
    else:
        print(f"{length} * {width} = {area}")  # Print just the result
    return area

# Function to calculate the area of a circle
def circle_area(radius, show_equation=False):
    """Calculate the area of a circle (in m²)."""
    area = round(math.pi * radius ** 2, 1)  # Area formula: π * r², rounded to 1 decimal place
    if show_equation:
        print(f"π * {radius}² = {area} (π * radius² = area)")  # Print detailed equation if enabled
    else:
        print(f"π * {radius}² = {area}")  # Print just the result
    return area

# Function to calculate the volume of a cylinder
def cylinder_volume(radius, height, show_equation=False):
    """Calculate the volume of a cylinder (in m³)."""
    volume = round(math.pi * radius ** 2 * height, 1)  # Volume formula: π * r² * h, rounded to 1 decimal place
    if show_equation:
        print(f"π * {radius}² * {height} = {volume} (π * radius² * height = volume)")  # Print detailed equation if enabled
    else:
        print(f"π * {radius}² * {height} = {volume}")  # Print just the result
    return volume

# Function to calculate the volume of a sphere
def sphere_volume(radius, show_equation=False):
    """Calculate the volume of a sphere (in m³)."""
    volume = round((4/3) * math.pi * radius ** 3, 1)  # Volume formula: (4/3) * π * r³, rounded to 1 decimal place
    if show_equation:
        print(f"(4/3) * π * {radius}³ = {volume} ((4/3) * π * radius³ = volume)")  # Print detailed equation if enabled
    else:
        print(f"(4/3) * π * {radius}³ = {volume}")  # Print just the result
    return volume

# Function to calculate the area of a triangle
def triangle_area(base, height, show_equation=False):
    """Calculate the area of a triangle (in m²)."""
    area = round(0.5 * base * height, 1)  # Area formula: 0.5 * base * height, rounded to 1 decimal place
    if show_equation:
        print(f"0.5 * {base} * {height} = {area} (0.5 * base * height = area)")  # Print detailed equation if enabled
    else:
        print(f"0.5 * {base} * {height} = {area}")  # Print just the result
    return area

# Function to display the introduction message
def show_intro():
    """Display the introductory message and available views."""
    print("A/V calculator")  # A/V refers to Area/Volume
    print("Enter V/v to change the calculated view")  # Option to switch to 'calculated view' (detailed equations shown)
    print("Enter D/d for default view")  # Option to switch to 'default view' (results only)

# Function to display the default menu for area/volume calculations
def default_menu():
    """Display the default calculation options."""
    print()
    print("1. Rectangle Area calculation (m²)")
    print("2. Circle Area calculation (m²)")
    print("3. Cylinder Volume calculation (m³)")
    print("4. Sphere Volume calculation (m³)")
    print("5. Triangle Area calculation (m²)")
    print()

# Main control loop for the program
def main():
    """Main loop to handle user input and control the flow of the program."""
    view = None  # No view selected initially (user will choose)
    show_equation = True  # Default is to show the equation (calculated view)

    while True:  # Loop continuously until user decides to exit
        if view is None:  # If no view is selected, show the intro menu
            show_intro()  # Display the intro message
            choice = input("Enter Q/q to quit: ").strip().lower()  # Ask for user input and convert to lowercase
            if choice == 'q':  # If user enters 'q', exit the loop
                print("Exiting the calculator. Goodbye!")
                break
            elif choice == 'v':  # If user selects 'v', enable calculated view (show equations)
                print("Switching to calculated view.")
                show_equation = True
                view = "calculated"
            elif choice == 'd':  # If user selects 'd', enable default view (only show results)
                print("Switching to default view.")
                show_equation = False
                view = "default"
            else:
                print("Invalid input. Please try again.")  # Handle invalid input
        else:
            default_menu()  # Show the default menu for shape selection
            choice = input("Select an option (or B/b to go back): ").strip().lower()

            if choice == 'q':  # If user selects 'q', exit the program
                print("Exiting the calculator. Goodbye!")
                break
            elif choice == '1':  # Rectangle area calculation
                rectangle_calculation(show_equation)
            elif choice == '2':  # Circle area calculation
                circle_calculation(show_equation)
            elif choice == '3':  # Cylinder volume calculation
                cylinder_calculation(show_equation)
            elif choice == '4':  # Sphere volume calculation
                sphere_calculation(show_equation)
            elif choice == '5':  # Triangle area calculation
                triangle_calculation(show_equation)
            elif choice == 'b':  # Go back to the intro menu
                view = None
            else:
                print("Invalid input. Please try again.")  # Handle invalid menu selections

# Function to handle rectangle area calculation
def rectangle_calculation(show_equation=False):
    """Perform the rectangle area calculation by prompting user input."""
    try:
        length = float(input("Enter the length of the rectangle (in meters): ").strip())  # Get length input
        width = float(input("Enter the width of the rectangle (in meters): ").strip())  # Get width input
    except ValueError:  # Handle invalid (non-numeric) input
        print("Invalid input. Please enter numeric values.")
        return
    rectangle_area(length, width, show_equation)  # Call the rectangle_area function

# Function to handle circle area calculation
def circle_calculation(show_equation=False):
    """Perform the circle area calculation by prompting user input."""
    try:
        radius = float(input("Enter the radius of the circle (in meters): ").strip())  # Get radius input
    except ValueError:  # Handle invalid (non-numeric) input
        print("Invalid input. Please enter a numeric value.")
        return
    circle_area(radius, show_equation)  # Call the circle_area function

# Function to handle cylinder volume calculation
def cylinder_calculation(show_equation=False):
    """Perform the cylinder volume calculation by prompting user input."""
    try:
        radius = float(input("Enter the radius of the cylinder (in meters): ").strip())  # Get radius input
        height = float(input("Enter the height of the cylinder (in meters): ").strip())  # Get height input
    except ValueError:  # Handle invalid (non-numeric) input
        print("Invalid input. Please enter numeric values.")
        return
    cylinder_volume(radius, height, show_equation)  # Call the cylinder_volume function

# Function to handle sphere volume calculation
def sphere_calculation(show_equation=False):
    """Perform the sphere volume calculation by prompting user input."""
    try:
        radius = float(input("Enter the radius of the sphere (in meters): ").strip())  # Get radius input
    except ValueError:  # Handle invalid (non-numeric) input
        print("Invalid input. Please enter a numeric value.")
        return
    sphere_volume(radius, show_equation)  # Call the sphere_volume function

# Function to handle triangle area calculation
def triangle_calculation(show_equation=False):
    """Perform the triangle area calculation by prompting user input."""
    try:
        base = float(input("Enter the base of the triangle (in meters): ").strip())  # Get base input
        height = float(input("Enter the height of the triangle (in meters): ").strip())  # Get height input
    except ValueError:  # Handle invalid (non-numeric) input
        print("Invalid input. Please enter numeric values.")
        return
    triangle_area(base, height, show_equation)  # Call the triangle_area function

# Main entry point of the program
if __name__ == "__main__":
    main()  # Run the main loop when the program is executed
