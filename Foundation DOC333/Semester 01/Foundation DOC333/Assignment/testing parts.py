# the lists to store data for multiple students
stud_ids = []
nics = []
first_names = []
last_names = []
birth_dates = []
addresses = []
tele_nums = []
tut_groups = []
centers = []
attendance = []

num = 0  # to control the main menu loop
count = 0
choice = 0

while num < 1:
    print("\nIIT Campus")
    print("Main Menu")
    print("\n1) Enroll a new student")
    print("2) View details of a student")
    print("3) View details of all the students according to the branch")
    print("4) Update student details")
    print("5) Mark attendance")
    print("6) View attendance")
    print("7) Exit")

    choice = int(input("\nYour choice:- "))

    if choice == 1:
        print("\nIIT Campus")
        print("\nEnroll a New Student")

        # Validating and appending student_id
        while True:
            stud_id = input("\nEnter the Student ID (9 digits only):- ")
            if len(stud_id) == 9 and stud_id.isdigit():
                stud_ids.append(int(stud_id))  # converting to integer and appending to the list
                break
            else:
                print("Invalid input. Please enter exactly 9 digits")

        # Validating and appending NIC
        while True:
            nic = input("Enter the NIC (10 digits):- ")
            if len(nic) != 10 or not nic.isdigit():  # nic validation
                print("Invalid input. Please enter exactly 10 numeric characters.")
            else:
                nics.append(nic)  # append NIC to the list
                break

        # Validating and appending first name
        while True:
            first_name = input("First Name (max 10 characters):- ")
            if len(first_name) > 10:  # full name validation
                print("Invalid input. Please enter up to 10 characters.")
            else:
                first_names.append(first_name)  # append first name to the list
                break

        # Validating and appending last name
        while True:
            last_name = input("Last Name (max 15 characters):- ")
            if len(last_name) > 15:  # Last name validation
                print("Invalid input. Please enter up to 15 characters.")
            else:
                last_names.append(last_name)  # append last name to the list
                break

        # appending birt date
        birth_date = input("Birth Date (YYYY-MM-DD):- ")
        birth_dates.append(birth_date)  # Append birth date to the list

        # Validating and appending address
        while True:
            address = input("Address (max 15 characters):- ")
            if len(address) > 15:  # Address validation
                print("Invalid input. Please enter up to 15 characters.")
            else:
                addresses.append(address)  # append address to the list
                break

        # Validating and appending telephone number
        while True:
            tele_num = input("Phone Number (10 digits):- ")
            if len(tele_num) != 10 or not tele_num.isdigit():
                print("Invalid input. Please enter exactly 10 numeric characters.")
            else:
                tele_nums.append(tele_num)  # append telephone number to the list
                break

        # Validating and appending tutorial group
        while True:
            tut_group = input("Tutorial Group :- ")
            if len(tut_group) != 1:
                print("Invalid input. Please enter 1 character")
            else:
                tut_groups.append(tut_group)  # append tutorial group to the list
                break

        # Validating and appending center
        while True:
            center = input("Centre (Colombo, Kurunegala, or Galle):- ").lower()
            if center not in ["colombo", "kurunegala", "galle"]:
                print("Invalid input. Please enter a valid center: Colombo, Kurunegala, or Galle.")
            else:
                centers.append(center)  # append center to the list
                break

        # Saving the data
        while True:
            decision = input("\nDo you want to save your details (Yes/No)? ").lower()

            if decision == "yes":
                count += 1
                print("\nDetails are saved successfully")
                break
            elif decision == "no":
                # Deleting the data from the lists if not saved
                stud_ids.pop()
                nics.pop()
                first_names.pop()
                last_names.pop()
                birth_dates.pop()
                addresses.pop()
                tele_nums.pop()
                tut_groups.pop()
                centers.pop()
                print("\nDetails are deleted")
                break
            else:
                print("\nInvalid input.")
                break

    elif choice == 2:
        print("\nIIT Campus")
        print("Show Student Details")

        while True:
            # Prompt for the Student ID
            inpt_stud_id = int(input("\nStudent ID: "))

            # Validate the Student ID input
            if len(str(inpt_stud_id)) != 9:
                print("Please enter 9 digits")
            else:
                count = 0
                # Search for the Student ID in the list
                while count < len(stud_ids):
                    if stud_ids[count] == inpt_stud_id:
                        # Display Student Details
                        print("\nStudent Details:")
                        print("Student ID       - ",stud_ids[count])
                        print("NIC              - ",nics[count])
                        print("Phone Number     - ",tele_nums[count])
                        print("First Name       - ",first_names[count])
                        print("Last Name        - ",last_names[count])
                        print("Tutorial Group   - ",tut_groups[count])
                        print("Centre           - ",centers[count])
                        break
                    count = count + 1

                # if the loop completes without finding the Student ID
                if count == len(stud_ids):
                    print("\nThe student with this ID is not found.")

            # asking if the user wants to see another student's details
            decision = input("\nDo you want to view another student’s details (Yes/No)? ").lower()
            if decision == "yes":
                continue
            elif decision == "no":
                break
            else:
                print("Invalid input.")

    elif choice == 3: # view details of all the students according to the branch
        print("\nIIT Campus")
        print("View details of all the students")

        while True:
            # Prompt for the centre/branch
            branch = input("\nEnter the Branch (Colombo, Kurunegala, or Galle): ").lower()

            # Validating the branch input
            if branch not in ["colombo", "kurunegala", "galle"]:
                print("Invalid input. Enter a valid branch: Colombo, Kurunegala, or Galle.")
                continue

            # Display header for the branch
            print("\nIIT Campus")
            print("\nView details of all the students")
            print("\nBranch Name: ",branch.capitalize())
            print("\nNIC        Student ID   First Name    Last Name     Tutorial Group")
            print("-" * 70)

            found = False
            for i in range(len(centers)):
                if centers[i] == branch:
                    # displaying the details of the students in a tabular form
                    print(
                        f"{nics[i]:<10} {stud_ids[i]:<12} {first_names[i]:<13} {last_names[i]:<12} {tut_groups[i]:<10}")
                    found = True

            if not found:
                print("\nNo students found in this branch.")

            # After showing student details, now ask if user wants to update any student details
            decision = input("\nDo you want to update the details of any student (Yes/No)? ").lower()
            if decision == "yes":
                while True:
                    # the prompt for the student ID to update
                    update_stud_id = int(input("\nEnter the Student ID of the student to update: "))

                    # checking if the student ID exists in the branch
                    if update_stud_id in stud_ids:
                        index = stud_ids.index(update_stud_id)  # getting the index of the student
                        if centers[index] != branch:
                            print("\nThis student is not in the selected branch.")
                            continue

                        # Start updating fields, similar to enrolling a new student

                        # Validating and updating NIC
                        while True:
                            new_nic = input(f"NIC [{nics[index]}]: ").strip()
                            if len(new_nic) == 10 and new_nic.isdigit() or not new_nic:
                                if new_nic:
                                    nics[index] = new_nic
                                break
                            else:
                                print("Invalid input. Please enter exactly 10 digits.")

                        # Validating and updating First Name
                        while True:
                            new_first_name = input(f"First Name [{first_names[index]}]: ")
                            if len(new_first_name) <= 10 or not new_first_name:
                                if new_first_name:
                                    first_names[index] = new_first_name
                                break
                            else:
                                print("Invalid input. Please enter up to 10 characters.")

                        # Validating and updating Last Name
                        while True:
                            new_last_name = input(f"Last Name [{last_names[index]}]: ")
                            if len(new_last_name) <= 15 or not new_last_name:
                                if new_last_name:
                                    last_names[index] = new_last_name
                                break
                            else:
                                print("Invalid input. Please enter up to 15 characters.")

                        # Validating and updating Birth Date
                        new_birth_date = input(f"Birth Date [{birth_dates[index]}]: ")
                        if new_birth_date:
                            birth_dates[index] = new_birth_date

                        # Validating and updating Address
                        while True:
                            new_address = input(f"Permanent Address [{addresses[index]}]: ")
                            if len(new_address) <= 15 or not new_address:
                                if new_address:
                                    addresses[index] = new_address
                                break
                            else:
                                print("Invalid input. Please enter up to 15 characters.")

                        # Validating and updating Phone Number
                        while True:
                            new_phone_number = input(f"Phone Number [{tele_nums[index]}]: ")
                            if len(new_phone_number) == 10 and new_phone_number.isdigit() or not new_phone_number:
                                if new_phone_number:
                                    tele_nums[index] = new_phone_number
                                break
                            else:
                                print("Invalid input. Please enter exactly 10 digits.")

                        # Validating and updating Tutorial Group
                        while True:
                            new_tut_group = input(f"Tutorial Group [{tut_groups[index]}]: ").capitalize()
                            if len(new_tut_group) == 1 or not new_tut_group:
                                if new_tut_group:
                                    tut_groups[index] = new_tut_group
                                break
                            else:
                                print("Invalid input. .")

                        # Validating and updating Centre
                        while True:
                            new_center = input(f"Centre [{centers[index]}]: ").strip().lower()
                            if new_center in ["colombo", "kurunegala", "galle"] or not new_center:
                                if new_center:
                                    centers[index] = new_center
                                break
                            else:
                                print("Invalid input. Please enter a valid centre (Colombo, Kurunegala, or Galle).")

                        print("\nStudent details updated successfully!")
                        break
                    else:
                        print("\nThe student id is not in this branch.")
            elif decision == "no":
                break
            else:
                print("Invalid input.")
                break

    elif choice == 4: # update student detailes
        print("\nIIT Campus")
        print("Update Student Details")

        # Ask for the Student ID to update details
        while True:
            update_stud_id = input("\nEnter the Student ID to update details (9 digits only): ")

            # Validate the Student ID input
            if len(update_stud_id) == 9 and update_stud_id.isdigit():
                update_stud_id = int(update_stud_id)
                if update_stud_id in stud_ids:
                    # Get the index of the student to update
                    index = stud_ids.index(update_stud_id)
                    print("\nCurrent details of the student:")
                    print("Student ID       - ", stud_ids[index])
                    print("NIC              - ", nics[index])
                    print("First Name       - ", first_names[index])
                    print("Last Name        - ", last_names[index])
                    print("Birth Date       - ", birth_dates[index])
                    print("Address          - ", addresses[index])
                    print("Phone Number     - ", tele_nums[index])
                    print("Tutorial Group   - ", tut_groups[index])
                    print("Centre           - ", centers[index])

                    # Start the update process for each field

                    # Update NIC
                    while True:
                        new_nic = input(f"NIC (Current: {nics[index]}): ").strip()
                        if not new_nic or len(new_nic) == 10 and new_nic.isdigit():
                            nics[index] = new_nic if new_nic else nics[index]  # Update if entered
                            break
                        else:
                            print("Invalid NIC. It should be 10 digits.")

                    # Update First Name
                    while True:
                        new_first_name = input(f"First Name (Current: {first_names[index]}): ").strip()
                        if not new_first_name or len(new_first_name) <= 10:
                            first_names[index] = new_first_name if new_first_name else first_names[
                                index]  # Update if entered
                            break
                        else:
                            print("Invalid First Name. It should be up to 10 characters.")

                    # Update Last Name
                    while True:
                        new_last_name = input(f"Last Name (Current: {last_names[index]}): ").strip()
                        if not new_last_name or len(new_last_name) <= 15:
                            last_names[index] = new_last_name if new_last_name else last_names[
                                index]  # Update if entered
                            break
                        else:
                            print("Invalid Last Name. It should be up to 15 characters.")

                    # Update Birth Date
                    new_birth_date = input(f"Birth Date (Current: {birth_dates[index]}): ").strip()
                    if new_birth_date:
                        birth_dates[index] = new_birth_date

                    # Update Address
                    while True:
                        new_address = input(f"Address (Current: {addresses[index]}): ").strip()
                        if not new_address or len(new_address) <= 15:
                            addresses[index] = new_address if new_address else addresses[index]  # Update if entered
                            break
                        else:
                            print("Invalid Address. It should be up to 15 characters.")

                    # Update Phone Number
                    while True:
                        new_phone_number = input(f"Phone Number (Current: {tele_nums[index]}): ").strip()
                        if not new_phone_number or (len(new_phone_number) == 10 and new_phone_number.isdigit()):
                            tele_nums[index] = new_phone_number if new_phone_number else tele_nums[
                                index]  # Update if entered
                            break
                        else:
                            print("Invalid Phone Number. It should be 10 digits.")

                    # Update Tutorial Group
                    while True:
                        new_tut_group = input(f"Tutorial Group (Current: {tut_groups[index]}): ").strip()
                        if not new_tut_group or len(new_tut_group) == 1:
                            tut_groups[index] = new_tut_group if new_tut_group else tut_groups[
                                index]  # Update if entered
                            break
                        else:
                            print("Invalid Tutorial Group. It should be 1 character.")

                    # Update Centre
                    while True:
                        new_center = input(f"Centre (Current: {centers[index]}): ").strip().lower()
                        if not new_center or new_center in ["colombo", "kurunegala", "galle"]:
                            centers[index] = new_center if new_center else centers[index]  # Update if entered
                            break
                        else:
                            print("Invalid Centre. It should be Colombo, Kurunegala, or Galle.")

                    print("\nStudent details updated successfully!")
                    break
                else:
                    print("Student ID not found. Enter a valid Student ID.")
            else:
                print("Invalid Student ID.")

    elif choice == 5:
        # Initialize variables
        atten = []  # Attendance for this session
        attendance_entry = []  # Single attendance entry for saving
        count1 = 0  # Counter for iteration
        cen = ""
        tgrp = ""
        day = ""

        print("\n           IIT Campus")
        print("         Mark Attendance\n")

        # Input: Center and Tutorial Group
        cen = input("Centre          - ").strip()
        tgrp = input("Tutorial Group  - ").strip()

        # Input: Date
        while True:
            day = input("Date            - ").strip()
            try:
                # Validate date format
                datetime.strptime(day, "%d/%m/%Y")
                break
            except ValueError:
                print("Error: Date needs to be in dd/mm/yyyy format.")

        print("\nStudent ID       Present/Absent")

        # Iterate over student records and collect attendance
        while count1 < count:  # Assuming 'count' is the total number of students
            if cen == centre[count1] and tgrp == tgroup[count1]:
                print(f"{sid[count1]:<15}", end="")
                while True:
                    status = input("").strip().upper()
                    if status in ["P", "A"]:  # Valid input: Present or Absent
                        atten.append({
                            "student_id": sid[count1],
                            "status": "Present" if status == "P" else "Absent"
                        })
                        break
                    else:
                        print("Invalid input. Enter 'P' for Present or 'A' for Absent.")
            count1 += 1

        # Save Attendance
        while True:
            des = input("\nDo you want to save the details (Yes/No)? ").strip().capitalize()
            if des == "Yes":
                attendance_entry.append({
                    "date": day,
                    "center": cen,
                    "tutorial_group": tgrp,
                    "records": atten
                })
                attendance.append(attendance_entry)  # Assuming 'attendance' is a global list
                print("\nAttendance saved successfully!")
                break
            elif des == "No":
                print("\nAttendance not saved.")
                break
            else:
                print("Invalid input. Please enter 'Yes' or 'No'.")

    elif choice == 6:
        inpid = 0
        fromd = 0
        tod = 0
        count1 = 0
        count2 = 0
        fromcount = 0
        tocount = 0

        print("")
        print("           IIT Campus")
        print("         View Attendance ")
        print("")

        while True:
            inpid = int(input("Student ID        - "))
            if len(str(inpid)) != 9:
                print("9 Digits Required.")
            else:
                break
        while True:
            fromd = str(input("From(dd/mm/yyyy)  - "))
            if len(fromd) != 10:
                print("Date needs to be in dd/mm/yyyy format")
            else:
                break
        while True:
            tod = str(input("To(dd/mm/yyyy)   - "))
            if len(fromd) != 10:
                print("Date needs to be in dd/mm/yyyy format")
            else:
                break

        while count1 < dcount:
            if attendance[count1][0] == fromd:
                fromcount = count1
                count1 += 1
            elif attendance[count1][0] == tod:
                tocount = count1
                count1 += 1
            else:
                count1 += 1

        print("Date                 Present/Absent")

        count1 = 0
        count2 = 0

        while count1 < dcount:
            count2 = 0
            while count2 < count:
                if sid[count2] == inpid and count1 >= fromcount and count1 <= tocount:

                    print(attendance[count1][0], end="               ")
                    print(attendance[count1][1][count2])
                    count2 += 1
                else:
                    count2 += 1
            count1 += 1