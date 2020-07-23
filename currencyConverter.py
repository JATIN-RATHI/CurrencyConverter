# Link :---> https://www.x-rates.com/table/?from=INR&amount=1
if __name__ == '__main__':
    with open('currencyDATA') as f:
        lines = f.readlines()
    dict = {}
    for line in lines:
        parsed = line.split("\t")
        dict[parsed[0]] = parsed[1]


    print("Choose any one to convert Indian currency into : \n1: Argentine Peso\n2: Australian Dollar\n3: Bahraini "
          "Dinar\n4: Botswana Pula\n5: Brazilian Real\n6: British Pound\n7: Bruneian Dollar\n8: Bulgarian Lev\n9: "
          "Canadian Dolla\n10: Chilean Peso\n11: Chinese Yuan Renminbi\n12: Colombian Peso\n13: Croatian Kuna\n14: "
          "Czech Koruna\n15: Danish Krone\n16: Emirati Dirham\n17: Euro\n18: Hong Kong Dollar\n19: Hungarian "
          "Forint\n20: Icelandic Krona\n21: Indonesian Rupiah\n22: Iranian Rial\n23: Israeli Shekel\n24: Japanese "
          "Yen\n25: Kazakhstani Tenge\n26: Kuwaiti Dinar\n27: Libyan Dinar\n28: Malaysian Ringgit\n29: Mauritian "
          "Rupee\n30: Mexican Peso\n31: Nepalese Rupee\n32: New Zealand Dollar\n33: Norwegian Krone\n34: Omani "
          "Rial\n35: Pakistani Rupee\n36: Philippine Peso\n37: Polish Zloty\n38: Qatari Riyal\n39: Romanian New "
          "Leu\n40: Russian Ruble\n41: Saudi Arabian Riyal\n42: Singapore Dollar\n43: South African Rand	\n44: "
          "South Korean Won\n45: Sri Lankan Rupee\n46: Swedish Krona\n47: Swiss Franc\n48: Taiwan New Dollar\n49: "
          "Thai Baht\n50: Trinidadian Dollar\n51: Turkish Lira\n52: US Dollar\n53: Venezuelan Bolivar")
    
    choose = int(input("Enter your choice : ")) - 1
    name = dict.keys()
    key_list = list(name)
    currency_name = key_list[choose]
    amt = dict.values()
    value_list = list(amt)
    currency_value = value_list[choose]
    amount = int(input("Enter amount to be converted: "))
    total = amount * float(currency_value)
    print(f"{amount} Indian Rupee =   {total} {currency_name} ")


