applicant_age = int(input())
vision_test = input()
written_score = int(input())
driving_score = int(input())
medical_clearance = input()

# TODO: Your code here
if applicant_age >= 21:
    if vision_test == "Pass":
        if written_score >= 80:
            if driving_score >= 80:
                if medical_clearance == "Pass":
                    license_class = "Class A (Commercial)"
                else:
                    license_class = "Restricted License"
            else:
                license_class = "Restricted License"
        else:
            if driving_score >= 80:
                if medical_clearance == "Pass":
                    license_class = "Restricted License"
                else:
                    license_class = "Restricted License"
            else:
                license_class = "Restricted License"
            



elif applicant_age >= 18:
    if vision_test == "Pass":
        if written_score >= 80:
            if driving_score >= 80:
                if medical_clearance == "Pass":
                    license_class = "Class B (Regular)"
                else:
                    license_class = "Class B (Regular)"
            





print(license_class)