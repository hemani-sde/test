# inputs needed
'''
1. total rent 
2. total food order 
3. electricity units spend
4. charge per unit
5. total person

'''
# ouput
'''
1. total rent per person

'''
print("Hello welcome to rent calculator")
rent=int(input("Enter total rent amount: "))
food=int(input("Enter total food order amount: "))
electricity_units=int(input("Enter total electricity units spent: "))
charge_per_unit=int(input("Enter charge per unit: "))
total_elec_bill=electricity_units*charge_per_unit
total_person=int(input("Enter total number of persons: "))
total_bill=rent+food+total_elec_bill
rent_per_person=total_bill/total_person
print(f"Total rent per Person is : {rent_per_person}")