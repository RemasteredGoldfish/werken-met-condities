# pizza calculator

#pizza small =5$
#pizza medium =8$
#pizza large =13$

print ('-----------------------')
print ('small pizza    $5')
print ('medium pizza   $8')
print ('large pizza    $13')
print ('-----------------------')


pizza = input('Welke size pizza wil je?')
aantalpizza = int(input ('hoeveel pizza wil je?'))
pizzasmall = 5
pizzamedium = 8
pizzalarge = 13

if pizza == 'small':
   resultsmall = ('dat wordt dan $') + str(aantalpizza * pizzasmall)
   print (resultsmall)
if pizza == 'medium':
   resultmedium = ('dat wordt dan $') + str(aantalpizza * pizzamedium )
   print (resultmedium)
if pizza == 'large':
   resultlarge = ('dat wordt dan $') + str(aantalpizza * pizzalarge)
   print (resultlarge)
