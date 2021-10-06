print('Circusdirecteur voor Circus HotelDeBotel')

dressuur = input('Heeft u meer dan 4 jaar praktijk ervaring met dieren-dressuur? ')
if dressuur == 'ja':

    jongleren = input('Heeft u meer dan 5 jaar ervaring met jongleren? ')
    if jongleren == 'ja':

        acrobatiek = input('Heeft u meer dan 3 jaar praktijkervaring met acrobatiek? ')
        if acrobatiek == 'ja':
            print('u voldoet aan het eerste deel van het sollicitatie')
else:
    print('u voldoet niet aan het eisen van het sollicitatie ')
if (dressuur, jongleren, acrobatiek,) == 'ja': 
    print('')
else:

    mbo = input('Bent u bezig van een MBO-4 diploma? ')
    if mbo == 'ja':
        rijbewijs = input('Bent u bezig van een gelid vrachtwagen rijbewijs? ')
        if rijbewijs == 'ja':
            hoed = input('Bent u bezit van een hoge hoed? ')
            if hoed == 'ja':
                print('u voldoet aan het tweede deel van het sollicitatie')
    else:
        print('u voldoet niet aan het tweede deel van het sollicitatie')
        snor = input('Bent u een man met een snor breder dan 10cm? ')
        if snor == 'ja':
            print('')
        elif snor == 'nee':
            print('of misschien bent u een vrouw?')
            Krullen = input('Bent u een vrouw met rood krulhaar langer dan 20cm? ')
            if Krullen == 'ja':
                print('')
            else:
                print('U bent geen man met en 10cm brede snor of een vrouw met rood krullende haar langer dan 20cm ')

                langer = input('bent u langer dan 150cm?')
                if langer == 'ja':
                    zwaarder = input('bent u zwaarder dan 90kg? ')
                    if zwaarder == 'ja':
                        print('u voldoet aan het derde deel van het vragenlijst')
                else:
                    print('u voldoet niet aan het derde deel van het vragenlijst')
                    certificaat = input('heeft u een certificaat met "overleven met gevaarlijk personeel?" ')
                    if certificaat == 'ja':
                        print('gefelicteerd u voldoet aan het eisen van dit vacaturen')
                    else:
                        print('u voldoet niet aan het eisen het spijt me') 