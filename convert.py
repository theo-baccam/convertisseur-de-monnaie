from forex_python.converter import CurrencyRates
cr = CurrencyRates()
from forex_python.converter import CurrencyCodes
cc = CurrencyCodes()

devise_list = [
            "Baht thaïlandais: THB",
            "Couronne danoise: DKK",
            "Couronne islandaise: ISK",
            "Couronne norvégienne: NOK",
            "Couronne suédoise: SEK",
            "Couronne thcèque: CZK",
            "Dollar américain: USD",
            "Dollar australien: AUD",
            "Dollar canadien: CAD",
            "Dollar de Hong Kong: HKD",
            "Dollar néo-zélandais: NZD",
            "Dolar singapourien: SGD",
            "Euro: EUR",
            "Forint hongrois: HUF",
            "Franc suisse: CHF",
            "Kuna croate: HRK",
            "Leu roumain: RON",
            "Lev bulgare: BGN",
            "Livre sterling: GBP",
            "Livre turque: TRY",
            "Peso mexicain: MXN",
            "Peso philippin: PHP",
            "Rand sud-africain: ZAR",
            "Real brésilien: BRL",
            "Ringgit malaisien: MYR",
            "Rouble russe: RUB",
            "Roupie indienne: INR",
            "Roupie indonésienne: IDR",
            "Shekel israélien: ILS",
            "Won de la Corée du Sud: KRW",
            "Yen japonais: JPY",
            "Yuan Renminbi chinois: CNY",
            "Zloty polonais: PLN"
]

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
        for devise in devise_list:
            print(f"{devise}")
        return ""

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

    final = f"{cr.convert(currency, convert, amount)} {convert}\n"
    return final

print("Convertisseur de monnaie :\n")

while True:
    prompt = input("==> ")
    output = prompt_processor(prompt)
    print(f"{output}")