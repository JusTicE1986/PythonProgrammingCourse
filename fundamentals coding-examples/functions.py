import datetime

word = "testcase"
def dollarizer(word): return word.replace('s', '$')
print(dollarizer(word))
def eurizer(word): return word.replace('e', "€")
print(eurizer(word))
def replacer(word, char1, char2): return word.replace(char1, char2)
print(replacer(word, "t", "T"))
def poundizer(word): return word.replace('l', "£")
print(poundizer(word))
def wonky_text(word):
    word = word
    if "s" in word:
        word = dollarizer(word)
    if "e" in word:
        word = eurizer(word)
    if "l" in word:
        word = poundizer(word)
    return word
print(wonky_text(word))

def celcius_to_fahrenheit(celsius):
    fahrenheit = int(celsius) * 9/5 +32
    return fahrenheit
print(celcius_to_fahrenheit(30))
def age_in_days(age):
    return age * 365
print(age_in_days(37))
def simple_interest(principal_amount, rate_of_interest, time_in_years):
    Simple_interest = principal_amount * rate_of_interest * time_in_years
    return Simple_interest
print(simple_interest(100, 0.6, 2))
def plan_finances(principal_amount, rate_of_interest, time_in_years, final_amount):
    interest = simple_interest(principal_amount, rate_of_interest, time_in_years)
    if interest >= final_amount:
        return True, interest
    else:
        return False, interest
print(plan_finances(100, 0.6, 2, 110))

