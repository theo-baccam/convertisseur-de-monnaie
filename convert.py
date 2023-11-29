from forex_python.converter import CurrencyRates
cr = CurrencyRates()
from forex_python.converter import CurrencyCodes
cc = CurrencyCodes()

def prompt_processor(input_string):
    if input_string == "help":
        return(
            "[taux] [devise départ] [devise cible]\n"
            "`list` pour avoir une liste des devises\n"
            "Certaines conversions ne pourrait pas marcher car il n'y pas de "
            "données disponibles."
        )
        return ("[taux] [devise départ] [devise cible]\n"
        "'list' pour avoir une liste des devises'")
    money_list = [value for value in input_string.split(" ")]

    if input_string == "list":
        return (
            "Baht thaïlandais: THB\n"
            "Couronne danoise: DKK\n"
            "Couronne islandaise: ISK\n"
            "Couronne norvégienne: NOK\n"
            "Couronne suédoise: SEK\n"
            "Couronne thcèque: CZK\n"
            "Dollar américain: USD\n"
            "Dollar australien: AUD\n"
            "Dollar canadien: CAD\n"
            "Dollar de Hong Kong: HKD\n"
            "Dollar néo-zélandais: NZD\n"
            "Dolar singapourien: SGD\n"
            "Euro: EUR\n"
            "Forint hongrois: HUF\n"
            "Franc suisse: CHF\n"
            "Kuna croate: HRK\n"
            "Leu roumain: RON\n"
            "Lev bulgare: BGN\n"
            "Livre sterling: GBP\n"
            "Livre turque: TRY\n"
            "Peso mexicain: MXN\n"
            "Peso philippin: PHP\n"
            "Rand sud-africain: ZAR\n"
            "Real brésilien: BRL\n"
            "Ringgit malaisien: MYR\n"
            "Rouble russe: RUB\n"
            "Roupie indienne: INR\n"
            "Roupie indonésienne: IDR\n"
            "Shekel israélien: ILS\n"
            "Won de la Corée du Sud: KRW\n"
            "Yen japonais: JPY\n"
            "Yuan Renminbi chinois: CNY\n"
            "Zloty polonais: PLN"
        )

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

    final = f"{cr.convert(currency, convert, amount)} {convert}"
    return final

print("Convertisseur de monnaie :\n")

while True:
    prompt = input("==> ")
    output = prompt_processor(prompt)
    print(f"{output}\n")