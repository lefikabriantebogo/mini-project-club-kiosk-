def club_kiosk():
    print("=== Welcome to the Club Kiosk ===")
    pin = "1234"
    attempts = 3


    while attempts > 0:
        entered_pin = input("Enter your PIN: ")
        if entered_pin == pin:
            print("Access granted!")
            break
        else:
            attempts -= 1
            print(f"Wrong PIN. {attempts} attempt(s) left.")
    else:
        print("Too many wrong attempts. Access denied.")
        return


    while True:
        print("\n--- Main Menu ---")
        print("1. Check Membership")
        print("2. Enter Class Grades")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            member = input("Are you a member? (yes/no): ").strip().lower()
            if member == "yes":
                print("Membership confirmed")
            else:
                print("Sorry, membership required")

        elif choice == "2":

            print("\n=== Class Gradebook ===")
            try:
                num_students = int(input("How many students are in the class? "))
            except ValueError:
                print("Invalid number. Returning to menu.")
                continue

            passed = 0
            failed = 0

            for i in range(num_students):
                name = input(f"\nEnter name of student {i+1}: ")


                while True:
                    try:
                        marks = int(input(f"Enter marks for {name} (0-100): "))
                        if 0 <= marks <= 100:
                            break
                        else:
                            print("Marks must be between 0 and 100.")
                    except ValueError:
                        print("Invalid input! Please enter a number.")


                if marks >= 70:
                    grade = "Distinction"
                    passed += 1
                elif marks >= 50:
                    grade = "Pass"
                    passed += 1
                else:
                    grade = "Fail"
                    failed += 1

                print(f"{name} scored {marks} → {grade}")


            print("\n=== Class Report ===")
            print(f"Total students: {num_students}")
            print(f"Passed: {passed}")
            print(f"Failed: {failed}")

        elif choice == "3":
            print("Exiting kiosk. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

club_kiosk()
