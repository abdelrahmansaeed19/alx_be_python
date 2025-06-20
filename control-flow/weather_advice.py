NotStringInputError = True

while NotStringInputError:
    try:
        weather = input("What's the weather like today? (sunny/rainy/cold):").strip().lower()
        if not isinstance(weather, str):
            raise ValueError("Input must be a string.")
        NotStringInputError = False
    except ValueError as e:
        print(e)
# This code prompts the user to enter the current weather and provides advice based on the input.
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
# This code provides advice based on the weather condition entered by the user.