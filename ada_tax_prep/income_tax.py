TAX_BRACKETS_2020 = (
)

def calculate_tax_by_bracket(income, brackets):
    if income <= 0:
        return 0

    last_max = 0
    total_tax = 0
    for bracket in brackets:
        if income <= last_max:
            break

        rate = bracket["rate"]
        if "max" in bracket:
            bracket_max = bracket["max"]
            bracketted_income = min((income, bracket_max)) - last_max
            last_max = bracket_max
        else:
            bracketted_income = income - last_max

        total_tax += round(bracketted_income * rate / 100)

    return total_tax

def calculate_tax_2020(income):

    TAX_BRACKETS_2020 = (
    { "max": 9875, "rate": 10 },
    { "max": 40125, "rate": 12 },
    { "max": 85525, "rate": 22 },
    { "max": 163300, "rate": 24 },
    { "max": 207350, "rate": 32 },
    { "max": 518400, "rate": 35 },
    { "rate": 37 }
)


    return calculate_tax_by_bracket(income, TAX_BRACKETS_2020)
    
