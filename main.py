reseau = reseau_amont.ReseauAmont(0, 0, 0, [20000, 'V'], [(500 * M.pow(10, 6)), 'VA'])
transfo = transformateur.Transformateur(0, 0, 0, [410, 'V'], 15, [1000, 'VA'], 0)

liaisons = liaison.Liaison(0, 'cuivre', 0, 50, [False, ''], [True, 'htb'], 2000) 
machine = machine_tournante.MachineTounante(0, 0, 0, [20000, 'V'], [M.pow(10, 6), 'VA'], 15)

#print(reseau.get_impedance() * 0.2)

somme_des_reactances = reseau.get_reactance() + liaisons.get_reactance()
somme_des_resistances = reseau.get_resistance() + liaisons.get_resistance()
##
zcc = M.sqrt(M.pow(somme_des_resistances, 2) + M.pow(somme_des_reactances, 2))
icc = reseau.tension['valeur'] / (M.sqrt(3) * zcc)
#
print("icc=" ,icc)
print("zcc=" ,zcc)


