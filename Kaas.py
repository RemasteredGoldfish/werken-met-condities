kaas = input('Is de kaas geel? ')
if  kaas == 'ja':
    gaten = input('Zit er gaten in? ')
else:
    schimmel = input('Heeft de kaas blauwe schimmels? ')

if  schimmel == 'ja':
    korst = input('Heeft de kaas een korst? ')
else:
    kaaskorst = input('Heeft de kaas een korst? ')

if  korst == 'ja':
    print('Bleu de Rochbaron')
else:
    print('Foume D Ambert')

if  gaten == 'ja':
    duur = input('Is de kaas belachelijk duur? ')
else:
    steen = input('Is de kaas hard als steen? ')

if  steen == 'ja':
    print('Pamigiano Reggiano')
else:
    print('Goude kaas')

if  duur == 'ja':
    print('Emmenthaler')
else:
    print('Leerdammer')

if  kaaskorst == 'ja':
    print('Camembert')
else:
    print('Mozzarella')