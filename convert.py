from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes

cr = CurrencyRates()
cc = CurrencyCodes()

devise_afrique = [
    "Rand sud-africain: ZAR",
]

devise_ameriques = [
    "Dollar américain: USD",
    "Dollar canadien: CAD",
    "Peso mexicain: MXN",
    "Real brésilien: BRL",
]

devise_asie = [
    "Baht thaïlandais: THB",
    "Dollar de Hong Kong: HKD",
    "Dolar singapourien: SGD",
    "Livre turque: TRY",
    "Peso philippin: PHP",
    "Ringgit malaisien: MYR",
    "Roupie indienne: INR",
    "Roupie indonésienne: IDR",
    "Shekel israélien: ILS",
    "Won de la Corée du Sud: KRW",
    "Yen japonais: JPY",
    "Yuan Renminbi chinois: CNY",
]

devise_europe = [
    "Couronne danoise: DKK",
    "Couronne islandaise: ISK",
    "Couronne norvégienne: NOK",
    "Couronne suédoise: SEK",
    "Couronne thcèque: CZK",
    "Euro: EUR",
    "Forint hongrois: HUF",
    "Franc suisse: CHF",
    "Kuna croate: HRK",
    "Leu roumain: RON",
    "Lev bulgare: BGN",
    "Livre sterling: GBP",
    "Rouble russe: RUB",
    "Zloty polonais: PLN",
]

devise_oceanie = [
    "Dollar australien: AUD",
    "Dollar néo-zélandais: NZD",
]


def converter(input_string):
    if input_string == "exit" or input_string == "quit":
        return "Quitting..."
        
    if input_string == "help":
        return (
            "[taux] [devise départ] [devise cible]\n"
            "`list` pour avoir une liste des devises\n"
            "Certaines conversions ne pourrait pas marcher car il n'y pas de "
            "données disponibles.\n"
            "`exit` ou `quit` pour quitter le programme."
        )
    money_list = [value for value in input_string.split(" ")]

    if input_string == "list":
        return "options: afrique, ameriques, asie, europe, oceanie\n"
        return ""
    if input_string == "list afrique":
        for devise in devise_afrique:
            print(devise)
        return ""
    if input_string == "list ameriques":
        for devise in devise_ameriques:
            print(devise)
        return ""
    if input_string == "list asie":
        for devise in devise_asie:
            print(devise)
        return ""
    if input_string == "list europe":
        for devise in devise_europe:
            print(devise)
        return ""
    if input_string == "list oceanie":
        for devise in devise_oceanie:
            print(devise)
        return ""

    if len(money_list) != 3:
        return "Entrée invalide\n"

    amount = money_list[0]
    currency = money_list[1]
    convert = money_list[2]

    try:
        amount = float(amount)
    except ValueError:
        return "Valeur invalide\n"
    
    try:
        if not cc.get_currency_name(currency) or not cc.get_currency_name(convert):
            return "Devises invalide\n"

        symbol = cc.get_symbol(convert)

        final = cr.convert(currency, convert, amount)
        return f"{round(final, 2)} {symbol}\n"
    except Exception as e:
        return f"Conversion impossible\n"


print("Convertisseur de monnaie :\n")

while True:
    prompt = input("==> ")
    output = converter(prompt)
    print(f"{output}")
    if output == "Quitting...":
        break
