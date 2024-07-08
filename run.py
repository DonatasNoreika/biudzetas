from biudzetas import Biudzetas

biudzetas = Biudzetas()

while True:
    veiksmas = int(input("1 - įvesti pajamas, 2 - įvesti išlaidas, 3 - peržiūrėti, 4 - balansas, 0 - išeiti: "))
    if veiksmas == 1:
        biudzetas.prideti_pajamas()
    if veiksmas == 2:
        biudzetas.prideti_islaidas()
    if veiksmas == 3:
        biudzetas.atspaudinti_zurnala()
    if veiksmas == 4:
        biudzetas.atspausdinti_balansa()
    if veiksmas == 0:
        break