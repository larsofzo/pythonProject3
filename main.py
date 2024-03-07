import serial
# Prompt the user to enter a number
Arduino = serial.Serial('COM5', 9600, timeout=4)
user_input = ""
while(user_input !="q"):
    user_input = input("choose led color on: ")
    # Send the number to Arduino
    Arduino.write(f"{user_input}\n".encode())
    print(f"Sent {user_input} seconds to Arduino. Waiting for response...")

    response = Arduino.readline().decode()
    print("Arduino Response:", response)

Arduino.close()