print("Enter the number of KMs")
dist_kms = input()
print(f"Convering {dist_kms} kilometers to miles")

dist_kms_flt = float(dist_kms)
dist_miles = dist_kms_flt/1.6

print(f"Distance in miles is {dist_miles} miles")

dist_miles_rnd = round(dist_miles,2)
print(f"Distance in miles rounded to two decimal places is {dist_miles_rnd} miles")
