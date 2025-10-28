monthly_income = int(input())
employment_status = input()
credit_rating = input()
employment_years = int(input())

# TODO: Your code here
if monthly_income >= 3000:
    if employment_status == "permanent":
        if credit_rating == "excellent":
            if employment_years >= 2:
                approval_status = "Approved"
            else:
                approval_status = "Conditionally Approved"
        else:
            if employment_years >= 2:
                approval_status = "Conditionally Approved"
            else:
                approval_status = "Rejected"

    elif employment_status == "contract":
        if credit_rating == "excellent":
            if employment_years >= 2:
                approval_status = "Conditionally Approved"
            else:
                approval_status = "Rejected"
        elif credit_rating == "good":
            if employment_years >= 1:
                approval_status = "Approved"
            else:
                approval_status = "Rejected"

    elif employment_status == "temporary":
        if credit_rating == "excellent":
            if employment_years >= 2:
                approval_status = "Conditionally Approved"
            else:
                approval_status = "Rejected"
        elif credit_rating == "good":
            if employment_years >= 1:
                approval_status = "Conditionally Approved"
            else:
                approval_status = "Rejected"
        else:
            approval_status = "Rejected"

else:
    if employment_status == "permanent":
        if credit_rating == "excellent":
            if employment_years >= 2:
                approval_status = "Conditionally Approved"
            else:
                approval_status = "Rejected"
        else:
            approval_status = "Rejected"

    elif employment_status == "contract":
        if credit_rating == "excellent":
            if employment_years >= 2:
                approval_status = "Conditionally Approved"
            else:
                approval_status = "Rejected"
        else:
            approval_status = "Rejected"

    elif employment_status == "temporary":
        if credit_rating == "excellent":
            if employment_years >= 2:
                approval_status = "Conditionally Approved"
            else:
                approval_status = "Rejected"
        elif credit_rating == "good":
            if employment_years >= 1:
                approval_status = "Conditionally Approved"
            else:
                approval_status = "Rejected"
        else:
            approval_status = "Rejected"

print(approval_status)