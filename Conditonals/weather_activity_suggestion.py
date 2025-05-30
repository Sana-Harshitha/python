weather_type =input("Please Enter Your Weather Conditon: ")
weather_type =weather_type.strip().lower()
if weather_type == "sunny":
    activity = "Go for a walk"
elif weather_type == "rainy":
    activity = "Read a book"
elif weather_type== "snowy":
    activity = "Build a snowman"

print(activity)