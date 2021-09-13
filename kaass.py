kaas = input('Is de kaas geel?')
if kaas == 'ja':
    gaten = input ('Zit er gaten in? ')
    if gaten == 'ja':
        duur = input('Is de kaas belachelijk duur')
        if duur == 'ja':
            print('Emmenthaler')
        elif duur == 'nee':
            print('Leerdammer')

    if gaten == 'nee':
        steen = input('Is de kaas hard als steen? ')
        if steen == 'ja':
            print('parmigiano Reggiano')
        elif steen == 'nee':
            print('Goude kaas')

if kaas == 'nee':
    schimmel = input('heeft de kaas blauwe schimmels?')
    if schimmel == 'ja':
        kaaskorst = input('Heeft de kaas een korst?')
        if kaaskorst == 'ja':
            print('Blue de rochbaron')
        elif kaaskorst == 'nee':
            print('Foume d Ambert')

    if schimmel == 'nee':
        korst = input('Heeft de kaas een korst? ')
        if korst == 'ja':
            print('Camembert')
        elif korst == 'nee':
            print('Mozzarella')
else:
    print('invalid')



