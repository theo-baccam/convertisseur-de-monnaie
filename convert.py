from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes

cr = CurrencyRates()
cc = CurrencyCodes()

currency_list = {
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


def save(history_list):
    with open("history.txt", "a") as file:
        for item in history_list:
            file.write(f"{item}\n")


def command_quit():
    return "Saving and quitting...\n"


def command_help():
    return (
        "[taux] [devise départ] [devise cible]\n"
        "`list` pour avoir une liste des devises\n"
        "`exit` ou `quit` pour quitter le programme.\n"
        "Certaines conversions ne pourrait pas marcher car il n'y pas de "
        "données disponibles.\n"
    )


def command_hist():
    with open("history.txt", "r") as file:
        history_file = file.readlines()
        for item in history_file:
            clean_item = item.replace("\r", "").replace("\n", "")
            print(clean_item)
    return ""


def command_list(input_list):
    if len(input_list) == 1:
        return "`list [option]`: afrique, ameriques, asie, europe, oceanie\n"
    if input_list[1] in currency_list:
        for item in currency_list[input_list[-1]]:
            print(item)
        return ""
    else:
        return "Région non existante\n"


def command_convert(command_input):
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


def command_invalid(in_lst):
    command_list = " ".join(in_lst)
    return (
        f"'{command_list}' n'est pas une commande valide.\n"
        f"Tapez `help` pour voir les commandes disponibles.\n"
    )


print("Convertisseur de monnaie (tapez `help`):\n")

while True:
    prompt = input("==> ")
    processed_input = [word for word in prompt.split(" ")]
    if processed_input[0] == "quit" or processed_input[0] == "exit":
        output = command_quit()
        print(output)
        save(history)
        break
    elif processed_input[0] == "help":
        output = command_help()
        print(output)
    elif processed_input[0] == "hist":
        output = command_hist()
        print(output)
    elif processed_input[0] == "list":
        output = command_list(processed_input)
        print(output)
    elif len(processed_input) == 3 and processed_input[0].replace(".", "", 1).isdigit():
        output = command_convert(processed_input)
        print(output)
    else:
        output = command_invalid(processed_input)
        print(output)
