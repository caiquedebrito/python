cell = ('Smartphone LG K71', 1599, 'Sansung Galaxy M21s', 1329, 'Xiaomi Redmi 9', 949, 'Sansung Galaxy M31', 1740, 'LG K41S', 796, 'Motorola One Fusion', 1348, 'Asus ZenFone Max Shot', 999, 'Moto G9 Power', 1540, 'Xiaomi Poco X3', 1640)
print('='*60)
print(f'{"#Celulares#":^55}')
print('='*60)
for c in range(0,len(cell),2):
		print(f'{cell[c]:.<50} R${cell[c+1]:5}')
print('='*60)