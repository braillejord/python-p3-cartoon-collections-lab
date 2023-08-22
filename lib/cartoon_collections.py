def roll_call_dwarves(names):
    for index, name in enumerate(names):
        print(f"{index + 1}. {name}")


def summon_captain_planet(calls):
    return [call.capitalize() + "!" for call in calls]


def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True

    return False


def find_the_cheese(foods):
    if "cheddar" in foods:
        return "cheddar"
    elif "gouda" in foods:
        return "gouda"
    elif "camembert" in foods:
        return "camembert"

    return None


# solution branch code: search through foods *and* cheeses

# cheeses = ["cheddar', "gouda", "camembert"]

# for food in foods:
#     if food in cheeses:
#         return foods

# return None
