# format method


num_to_transform = '0'
print("\n== Number Transformation ==")
print("1. Input a number")
print("2. Display float number with two digits after decimal")
print("3. Display float number with more than two digits after decimal")
print("4. Display number with decimal in thousand/hundred place")
print("5. Display number as binary")
print("6. Display number as octo")
print("7. Display number as hexa deximal")
print("8. Display number as scientific number")
print("E. Exit")
choice = input("choice: ")

while choice != 'e' and choice != 'E':
    if choice != '1' and num_to_transform == '0':
        print("\n[ Input a number first ]")
    else:
        if choice == '1':
            num_to_transform = input("\nInput a number: ")
            if num_to_transform.isdigit():
                print("\n[ number updated ]")
            else:
                print("\n[ Input has to be a digit ]")
        elif choice == '2':
            num_two = float(num_to_transform)
            print("\nThe number: {:.2f}".format(num_two))
        elif choice == '3':
            num_three = float(num_to_transform)
            print("\nThe number: {:.3f}".format(num_three))
            print("The number: {:.5f}".format(num_three))
        elif choice == '4':
            num_four = int(num_to_transform)
            print("\nThe number: {:,}".format(num_four))
        elif choice == '5':
            num_five = int(num_to_transform)
            print("\nThe number: {:b}".format(num_five))
        elif choice == '6':
            num_six = int(num_to_transform)
            print("\nThe number: {:o}".format(num_six))
        elif choice == '7':
            num_seven = int(num_to_transform)
            print("The number: {:x}".format(num_seven))
        elif choice == '8':
            num_eight = int(num_to_transform)
            print("\nThe number: {:e}".format(num_eight))
        else:
            print("\n[ Invalid choice ]")

    print("\n== Number Transformation ==")
    print("1. Input a number")
    print("2. Display float number with two digits after decimal")
    print("3. Display float number with more than two digits after decimal")
    print("4. Display number with decimal in thousand/hundred place")
    print("5. Display number as binary")
    print("6. Display number as octo")
    print("7. Display number as hexa deximal")
    print("8. Display number as scientific number")
    print("E. Exit")
    choice = input("choice: ")

if choice == 'e' or choice == 'E':
    print("\n== Exit Program ==")