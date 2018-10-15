name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches  高度
weight = 180 # lbs 重量
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
#英寸转换厘米 1英寸=2.54厘米
height_cm = height * round(2.54,1) #四舍五入,参数2取多少位小数
#磅转换千克，1磅=0.4535924千克
weight_kg = weight * round(0.4535924, 3)

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"He's {height_cm} CM.")
print(f"He's {weight_kg} KG.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair." )
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
