class Repulo:
#típus;év;utas;személyzet;utazósebesség;felszállótömeg;fesztáv
   def __init__(self,sor:str):
      adatok=sor.strip().split(';')
      self.tipus=adatok[0]
      self.ev=int(adatok[1])
      self.utas=adatok[2]  #180-200
      self.szemelyzet=adatok[3]  #2-5
      self.sebesseg=int(adatok[4])
      self.tomeg=int(adatok[5])
      self.fesztav=float(adatok[5].replace(',','.'))
      self.sebessegKategoria=""
      if self.sebesseg<500: self.sebessegKategoria="Alacsony sebességű"
      elif self.sebesseg<1000: self.sebessegKategoria="Szubszonikus"
      elif self.sebesseg<1200: self.sebessegKategoria="Transzszonikus"
      else: self.sebessegKategoria="Szuperszonikus"

repulok:list[Repulo]=[]

f=open('utasszallitok.txt','r',encoding='utf-8')
f.readline()
for sor in f:
   repulok.append(Repulo(sor))
f.close()

print(f'4. feladat: Adatsorok száma: {len(repulok)}')

boeingDb=0
for repulo in repulok:
#    if repulo.tipus.__contains__('Boeing'):
#       boeingDb+=1
     if 'Boeing' in repulo.tipus:
        boeingDb+=1
print(f'5. feladat: Boeing típusok száma: {boeingDb}')

maxUtasPoz=0
maxUtas=0
for i in range(len(repulok)):
   utasszam=int(repulok[i].utas.split('-')[-1]) #150-179-->179
   if utasszam>maxUtas:
      maxUtas=utasszam
      maxUtasPoz=i

print('6. feladat: A legtöbb utast szállító repülőgéptípus')
print(f'\tTípus: {repulok[maxUtasPoz].tipus}')
print(f'\tElső felszállás: {repulok[maxUtasPoz].ev}')
print(f'\tUtasok száma: {repulok[maxUtasPoz].utas}')
print(f'\tSzemélyzet: {repulok[maxUtasPoz].szemelyzet}')
print(f'\tUtazósebesség: {repulok[maxUtasPoz].sebesseg}')

stat={"Alacsony sebességű":0,
      "Szubszonikus":0,
      "Transzszonikus":0,
      "Szuperszonikus":0}

for repulo in repulok:
   if repulo.sebessegKategoria in stat.keys():
      stat[repulo.sebessegKategoria]+=1
#    else: 
#       stat[repulo.sebessegKategoria]=1    csak ha a listából vesszük a kulcsmezőket

print('7. feladat:\n\t',end='')
db=0
for key,value in stat.items():
   if value==0:
    print(f'{key}',end=' ')
    db+=1
if db==0:
   print('Minden sebességkategóriából van repülőgéptípus.')    






