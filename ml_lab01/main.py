#Assignment1
print('Elene')

#Assignment2
def main():
    # Input two numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2

    if num2 != 0:
        division = num1 / num2
    else:
        division = "Undefined (division by zero)"

    print("Addition:", addition)
    print("Subtraction:", subtraction)
    print("Multiplication:", multiplication)
    print("Division:", division)


main()

#Assignment3
import math

def main():
    radius = float(input("Enter the radius of the circle: "))

    area = math.pi * radius ** 2

    print("The area of the circle with radius", radius, "is:", area)

if __name__ == "__main__":
    main()


#Assignment 4

def minutes_to_seconds(minutes):
    return minutes * 60

# Input
minutes = int(input("Enter the number of minutes: "))

# Convert minutes to seconds
seconds = minutes_to_seconds(minutes)

# Output
print(f"{minutes} minutes is equal to {seconds} seconds.")



#Assignment5
def print_ip_addresses(network):
    network_address, subnet_mask = network.split('/')
    subnet_mask = int(subnet_mask)
    ip_octets = network_address.split('.')
    host_bits = 32 - subnet_mask
    num_addresses = 2 ** host_bits

    print(f"IP addresses within {network}:")

    for i in range(num_addresses):
        last_octet = int(ip_octets[3]) + i
        print(f"{ip_octets[0]}.{ip_octets[1]}.{ip_octets[2]}.{last_octet}")

if __name__ == "__main__":
    network = "192.168.0.3/24"
    print_ip_addresses(network)


