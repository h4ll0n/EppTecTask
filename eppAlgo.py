# Algoritmus trideni seznamu podle pravidel

# Funkce pro aplikaci pravidel
def apply_rules(item):
    account_number = str(item["account_number"])
    interest_rate = item["interest_rate"]
    if account_number.startswith("1") and interest_rate >= 0.05:
        return True
    else:
        return False


# Funkce pro trideni seznamu
def sort_list(lst):
    sorted_list = []
    for item in lst:
        if apply_rules(item):
            sorted_list.append(item)
    return sorted_list

# Seznam k trideni
input_list = [
    {"account_number": 1234567890, "balance": 10000, "interest_rate": 0.05},
    {"account_number": 9876543210, "balance": 5000, "interest_rate": 0.03},
    {"account_number": 2468135790, "balance": 15000, "interest_rate": 0.06},
    {"account_number": 1357924680, "balance": 20000, "interest_rate": 0.04},
    {"account_number": 9876543210, "balance": 8000, "interest_rate": 0.02},
    {"account_number": 8642097531, "balance": 12000, "interest_rate": 0.07},
    {"account_number": 2468013579, "balance": 30000, "interest_rate": 0.05},
    {"account_number": 1234567890, "balance": 10000, "interest_rate": 0.03},
    {"account_number": 9876543210, "balance": 5000, "interest_rate": 0.06},
    {"account_number": 2468135790, "balance": 15000, "interest_rate": 0.04},
    {"account_number": 1357924680, "balance": 20000, "interest_rate": 0.02},
    {"account_number": 9876543210, "balance": 8000, "interest_rate": 0.07},
    {"account_number": 8642097531, "balance": 12000, "interest_rate": 0.05},
    {"account_number": 2468013579, "balance": 30000, "interest_rate": 0.03},
    {"account_number": 1234567890, "balance": 10000, "interest_rate": 0.06},
    {"account_number": 9876543210, "balance": 5000, "interest_rate": 0.04},
    {"account_number": 2468135790, "balance": 15000, "interest_rate": 0.02},
    {"account_number": 1357924680, "balance": 20000, "interest_rate": 0.07},
    {"account_number": 9876543210, "balance": 8000, "interest_rate": 0.05},
    {"account_number": 8642097531, "balance": 12000, "interest_rate": 0.03},
    {"account_number": 2468013579, "balance": 30000, "interest_rate": 0.06},
]
sorted_result = sort_list(input_list)
print("Seznam po třídění:", sorted_result)
