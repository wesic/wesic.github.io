"""
Calculate the weight of the goat using dimenstions:
"""

heart_girth = float(input("Enter the goat Heart Girth Dimention in inch: "))
body_length = float(input("Enter the body length of the goat: "))

weight_in_lbs = ((heart_girth * heart_girth * body_length)/300)
# weight_in_kgs    = round(weight_in_lbs * 0.45359237 , 2) # 0.453592
weight_in_kgs = round(weight_in_lbs / 2.215 , 2) # mine
# weight_in_kgs = round(weight_in_lbs / 2.205 , 2) # from google

print(f"Goat weight is {weight_in_kgs} kg. ")
meat_in_weight = weight_in_kgs
in_cost = round(meat_in_weight* 350 , 2)
print(f"Raw goat market value: Rs.{in_cost}/-")
