from forex_python.converter import CurrencyRates
cr = CurrencyRates()
from forex_python.converter import CurrencyCodes
cc = CurrencyCodes()

def prompt_processor(input_string):
    money_list = [value for value in input_string.split(" ")]

    if len(money_list) != 3:
        return "Nombre d'éléments invalide"

    amount = money_list[0]
    currency = money_list[1]
    convert = money_list[2]

    try:
        amount = float(amount)
    except ValueError:
        return "Valeur invalide"

    if not cc.get_currency_name(currency) or not cc.get_currency_name(convert):
        return "Devises invalide"

    taux_change = cr.get_rate(currency, convert)
    final = amount * taux_change
    return final

print("Convertisseur de monnaie :\n")

while True:
    prompt = input("==> ")
    output = prompt_processor(prompt)
    print(f"{output}\n")