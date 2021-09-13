Kaas = ('Is de kaas geel? ')
gaten = ('Zit er gaten in? ')
schimmel = ('Heeft de kaas blauwe schimmels? ')
kaaskorts = ('Heeft de kaas een korst? ')
korst = ('Heeft de kaas een korst? ')
duur =  ('Is de kaas belachelijk duur? ')
steen = ('Is de kaas hard als steen? ')

E = ('Emmenthaler')
L = ('Leerdammer')
P = ('Pamigiano Reggiano')
G = ('Goudse kaas')
B = ('Blue de rochbaron')
F = ('Foume dambert')
C = ('Camembert')
M = ('Mozzarella')

antwoord1 = input(Kaas)
if antwoord1 == 'ja':

    antwoord2 = input(gaten)
    if antwoord2 == 'ja':
            antwoord6 = input(duur)
    else: 
        antwoord7 = input(steen)
        if antwoord7 == 'ja':
            print(P)
        else:
            print(G)
    if  antwoord6 == 'ja':
        print(E)
    else:
        print(L)

