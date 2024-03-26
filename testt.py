def calculate_tip(bill_amount, service_quality, number_of_people):
    # Calculate tip per person
    tip_per_person = (bill_amount * (service_quality / 100)) / number_of_people
    return tip_per_person

# Test Case 1
bill1 = 500
service_quality1 = 5
number_of_people1 = 2
tip1 = calculate_tip(bill1, service_quality1, number_of_people1)
print("Test Case 1 - Tip:", tip1)

# Test Case 2
bill2 = 1000
service_quality2 = 3
number_of_people2 = 5
tip2 = calculate_tip(bill2, service_quality2, number_of_people2)
print("Test Case 2 - Tip:",tip2)
