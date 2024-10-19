car_value = 10000
purchase_year = 2011
car_age = 8
driver_age = 23
electric = True
emissions_passed = True

renewal_fee = 20
if purchase_year <= 2012:
    renewal_fee += car_value * 0.01

if electric:
    renewal_fee += 200

if not emissions_passed and not (electric or (driver_age >= 65 and car_age >= 10)):
    print("You must pass an emissions test first.")
else:
    print(f"Your renewal fee is ${round(renewal_fee)}.")
