def you_pay(spending, is_monday):
    if spending < 51:
        return spending * 0.9
    elif is_monday and spending >= 51:
        new_spending = spending - 10
    else:
        new_spending = spending

    if 50 < new_spending <= 100:
        return new_spending * 0.8
    else:
        return new_spending * 0.6
