#n += 1 helps count the number of times that the message has been printed. Once the while loop has run 5 times, it will stop printing the message. If there was no n += 1 line, it would print the message indefinitely, as n would always be less than 5

print("Type in a message, and I'll display it ten times.")

message = input("Message: ")
print()
times = int(input("How many times? "))
print()

n = 0
while n < times:
    n += 1
    print(f"{n * 10}. {message}")
