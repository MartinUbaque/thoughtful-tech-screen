# Sorting function for Thoughtful's automation factory robotic arm
# Arguments: Package dimensions and mass
# Returns: Sort package according to the stack where it should go: STANDARD, SPECIAL, REJECTED
def sort(width, height, length, mass):
    # Argument validation
    # Each case is expressed independently for user-friendly error messages
    try:
        width= float(width)
    except ValueError:
        raise ValueError("Width must be a number")
    try:
        height= float(height)
    except ValueError:
        raise ValueError("Height must be a number")
    try:
        length= float(length)
    except ValueError:
        raise ValueError("Length must be a number")
    try:
        mass= float(mass)
    except ValueError:
        raise ValueError("Mass must be a number")
    if width<=0:
        raise ValueError("Width must be greater than 0")
    if height<=0:
        raise ValueError("Height must be greater than 0")
    if length<=0:
        raise ValueError("Length must be greater than 0")
    if mass<=0:
        raise ValueError("Mass must be greater than 0")
    # Sorting logic. Each condition adds 1 to the package_value
    # 
    package_value= 0
    if width*height*length>=1000000 or width>=150 or height>=150 or length>=150:
        # Package is bulky, +1
        package_value+= 1
    if mass>=20:
        # Package is heavy, +1
        package_value+= 1
    if package_value==0:
        # Package value is 0, so neither bulky nor heavy
        return "STANDARD"
    elif package_value==1:
        # Package value is 1, so it is either bulky or heavy
        return "SPECIAL"
    elif package_value==2:
        # Package value is 2, so it is both bulky and heavy
        return "REJECTED"
    

if __name__ == "__main__":
    try:
        print("Please enter the package dimensions and mass:")
        w = input("Width: ")
        h = input("Height: ")
        l = input("Length: ")
        m = input("Mass: ")
        result = sort(w, h, l, m)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")