while True:
    bp_input = input("Enter blood pressure readings (mmHg): ")
    if bp_input == "":
        print("Thank you and keep monitoring your blood pressure.")
        break
    else:
        bp_list = bp_input.split("/")
        systolic = int(bp_list[0])
        diastolic = int(bp_list[1])
        if systolic < 90 or diastolic < 60:
            print("Your blood pressure is low.")
        elif systolic >= 90 and systolic <= 119 and diastolic >= 60 and diastolic <= 79:
            print("Your blood pressure is normal.")
        elif systolic >= 120 and systolic <= 129 and diastolic >= 80 and diastolic <= 84:
            print("You have Elevated blood pressure.")
        elif systolic >= 130 and systolic <= 139 or diastolic >= 85 and diastolic <= 89:
            print("You have Stage 1 Hypertension.")
        elif systolic >= 140 or diastolic >= 90:
            print("You have Stage 2 Hypertension.")
