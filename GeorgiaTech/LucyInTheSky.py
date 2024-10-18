cut = "Emerald"
clarity = "VS"
color = "E"
carat = 1.1
budget = 200
preferred_cuts = ["Emerald", "Cushion", "Princess", "Oval"]
base_cost = 100

color_adj = 0.98 ** (ord(color) - ord("D"))
clarity_scale = ["I", "SI", "VS", "VVS", "IF", "F"]
clarity_adj = 2 ** clarity_scale.index(clarity)
price = base_cost * color_adj * clarity_adj * carat

if price < budget and cut in preferred_cuts:
    print("I'll take it!")
else:
    print("No thanks")
#################################
#sample solution given:
if cut in preferred_cuts:

    cost = 100

    percent_off = (ord(color) - ord("D")) * 0.02

    cost *= 1 - percent_off
    if not clarity == "I":
        cost *= 2

        if not clarity == "SI":
            cost *= 2
            if not clarity == "VS":
                cost *= 2

                if not clarity == "VVS":
                    cost *= 2

                    if not clarity == "IF":
                        cost *= 2
    cost *= carat

    if cost <= budget:
        print("I'll take it!")

    else:
        print("No thanks")

else:
    print("No thanks")
