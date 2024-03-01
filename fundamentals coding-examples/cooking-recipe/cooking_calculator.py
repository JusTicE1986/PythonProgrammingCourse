

def cooking_time(start, duration):
    end_time = (start + duration) % 24
    return f"take the meal out of the oven at {end_time} o'clock"

def cooking_time(start, duration, meal):
    end_time = (start + duration) % 24
    return f"take the {meal} out of the oven at {end_time} o'clock"