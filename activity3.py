print("Exam Eligibility...")
attendence= int(input("Enter Attendece:"))
medical_cause=input9("Enter yes/no for medical cause")
if attendence>75:
    print("Eligible  for exam")
else:
    if medical_cause=="yes":
        print("Eligible for exam")
    else:
        print("Not Eligible for Exam")
    