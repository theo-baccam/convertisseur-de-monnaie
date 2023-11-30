from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes

cr = CurrencyRates()
cc = CurrencyCodes()

devise_list = {
    "afrique": [
        "Rand sud-africain: ZAR",
    ],
    "ameriques": [
        "Dollar américain: USD",
        "Dollar canadien: CAD",
        "Peso mexicain: MXN",
        "Real brésilien: BRL",
    ],
    "asie": [
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
    ],
    "europe": [
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
    ],
    "oceanie": [
        "Dollar australien: AUD",
        "Dollar néo-zélandais: NZD",
    ],
}

history = []


def save(history):
    for item in history:
        with open("history.txt", "a") as file:
            file.write(f"{item}\n")


def commands(input_string):
    command = [word for word in input_string.split(" ")]

    if command[0] == "exit" or command[0] == "quit":
        save(history)
        return "Saving and quitting..."

    elif command[0] == "help":
        return (
            "[taux] [devise départ] [devise cible]\n"
            "`list` pour avoir une liste des devises\n"
            "`exit` ou `quit` pour quitter le programme.\n"
            "Certaines conversions ne pourrait pas marcher car il n'y pas de "
            "données disponibles.\n"
        )

    elif command[0] == "hist":
        with open("history.txt", "r") as file:
            history_file = file.readlines()
            for item in history_file:
                clean_item = item.replace("\r", "").replace("\n", "")
                print(clean_item)
        return ""

    elif command[0] == "list":
        if len(command) == 1:
            return "Options: afrique, ameriques, asie, europe, oceanie\n"
        if command[1] in devise_list:
            for item in devise_list[command[-1]]:
                print(item)
            return ""
        else:
            return "Région non existante\n"

    elif len(command) == 3 and command[0].replace(".", "", 1).isdigit():
        amount = command[0]
        currency = command[1]
        convert = command[2]
        return (amount, currency, convert)

    else:
        return (
            f"'{input_string}' est une commande invalide.\n"
            f"Tapez `help` pour voir les commandes disponibles.\n"
        )


def converter(command_input):
    amount = command_input[0]
    currency = command_input[1]
    convert = command_input[2]

    try:
        amount = float(amount)
    except ValueError:
        return "Valeur invalide\n"
    try:
        if not cc.get_currency_name(currency) or not cc.get_currency_name(convert):
            return "Devises invalide\n"

        symbol = cc.get_symbol(convert)

        final = cr.convert(currency, convert, amount)
        history.append(f"{amount} {currency} => {round(final, 2)} {convert}")
        return f"{round(final, 2)} {symbol}\n"
    except Exception as e:
        return f"Conversion impossible\n"


print("Convertisseur de monnaie (tapez `help`):\n")

while True:
    prompt = input("==> ")
    output = commands(prompt)
    if len(output) == 3:
        result = converter(output)
        print(f"{result}")
    else:
        print(f"{output}")
        if output == "Saving and quitting...":
            break
