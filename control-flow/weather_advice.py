def main():
    # Ask user for the weather
    weather = input("What's the weather like today? (sunny/rainy/cold): ")
    
    # Determine appropriate response based on weather
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Bring an umbrella and wear waterproof shoes.")
    elif weather == "cold":
        print("Bundle up with a coat, hat, and gloves.")
    else:
        print("Sorry, I don't have advice for that weather.")
