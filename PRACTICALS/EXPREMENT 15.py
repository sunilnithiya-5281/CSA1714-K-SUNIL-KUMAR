def decide_to_go_outside(is_sunny, is_raining, temperature):
    if is_raining:
        return "Stay inside: It's raining! 🌧️"
    else:
        if is_sunny:
            if temperature > 25:
                return "Go outside: Perfect sunny weather! ☀️"
            else:
                return "Go outside, but bring a jacket: Sunny, but a bit cool. 🧥"
        else:
            return "Stay inside: It's cloudy and gloomy. ☁️"

print(decide_to_go_outside(is_sunny=True, is_raining=False, temperature=28))
print(decide_to_go_outside(is_sunny=False, is_raining=True, temperature=20))
