# Menu-Driven File Operations
# ● Write data to a file
# ● Read data from a file
# ● Append data to a file
# ● Handle invalid user input and file errors using exception handling

while True:
    print("Menu (choose the number):")
    print("1.Write data to a file")
    print("2.Read data from a file")
    print("3.Append data to a file")
    print("4.Exit")
    choice = input("Enter your choice (1-4): ")
    try:
        if choice == '1':
            data = input("Enter data to write to the file: ")
            with open('Lab3/qst5.txt', 'w') as file:
                file.write(data)
            print("Data written successfully.")

        elif choice == '2':
            with open('Lab3/qst5.txt', 'r') as file:
                contents = file.read()
                print("File contents:")
                print(contents)

        elif choice == '3':
            data = input("Enter data to append to the file: ")
            with open('qst5.txt', 'a') as file:
                file.write(data)            
            print("Data appended successfully.")

        elif choice == '4':
            print("Exiting the program.")
            break

    except FileNotFoundError:
        print("File not found.")

    except Exception as e:
        print(f"An error occurred:{e}")