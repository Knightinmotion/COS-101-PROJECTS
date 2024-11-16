print("COS 101 assignment! ")


print("velocity")

def calculate_velocity (displacement, time):
    if time == 0:
        return "Time cannot be zero."
    velocity = displacement / time
    return velocity


def main():
    try:
        displacement = float(input("Enter the displacement (in meters): "))
        time = float(input("Enter the time (in seconds): "))

        velocity = calculate_velocity(displacement, time)

        if isinstance(velocity, str):
            print(velocity)
        else:
            print(f"The velocity is {velocity} in meters per second.")

    except ValueError:
        print("Please enter valid numbers for displacement and time.")


if __name__ == "__main__":
    main()

print("speed ")

def calculate_speed(distance, time):
    """Calculate speed (s = d / t)"""
    if time <= 0:
        raise ValueError("Time must be greater than zero.")
    return distance / time

def main():
    try:
        # Get user input
        distance = float(input("Enter the distance traveled (in meters): "))
        time = float(input("Enter the time taken (in seconds): "))

        # Calculate speed
        speed = calculate_speed(distance, time)

        # Display the result
        print(f"The speed is {speed:.2f} meters per second (m/s).")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

print("momentum ")

def calculate_momentum(mass, velocity):
    """Calculate momentum (p = m * v)"""
    return mass * velocity

def main():
    try:
        # Get user input
        mass = float(input("Enter the mass (in kilograms): "))
        velocity = float(input("Enter the velocity (in meters per second): "))

        # Calculate momentum
        momentum = calculate_momentum(mass, velocity)

        # Display the result
        print(f"The momentum is {momentum:.2f} kg*m/s.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

print("pressure ")

def calculate_pressure(force, area):
    """Calculate pressure (P = F / A)"""
    if area <= 0:
        raise ValueError("Area must be greater than zero.")
    return force / area

def main():
    try:
        # Get user input
        force = float(input("Enter the force applied (in Newtons): "))
        area = float(input("Enter the area over which the force is applied (in square meters): "))

        # Calculate pressure
        pressure = calculate_pressure(force, area)

        # Display the result
        print(f"The pressure is {pressure:.2f} Pascals (Pa).")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

print("impulse ")

def calculate_impulse(force, time):
    """Calculate impulse (J = F * Δt)"""
    return force * time

def main():
    try:
        # Get user input
        force = float(input("Enter the force applied (in Newtons): "))
        time = float(input("Enter the time duration (in seconds): "))

        # Calculate impulse
        impulse = calculate_impulse(force, time)

        # Display the result
        print(f"The impulse is {impulse:.2f} Newton/seconds (Ns).")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
