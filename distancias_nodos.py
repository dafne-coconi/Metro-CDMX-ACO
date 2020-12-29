import numpy as np

Nodos=[2,8,9,11,13,14,20,23,30,31,35,40,42,44,48,52,55,57,59,60,62,68,71,88]
Lineas_metro={1:[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
              2:[21,22,23,24,25,36,27,28,29,30,31,32,33,11,34,35,36,37,38],
              3:[39,40,41,42,43,44,30,45,8,46,47,48,49,50,51],
              4:[52,53,54,55,56,57,13,58,59,60],
              5:[61,62,63,42,64,65,55,66,67,68,69,70,20],
              6:[71,72,73,74,75,76,62,77,40,78,52],
              7:[71,79,80,81,23,82,83,84,85,2,86,87],
              8:[88,31,89,9,90,91,35,92,60,93],
              9:[2,94,95,48,96,35,59,97,98,99,100,20],
              10:[20,101,102,103,104],
              11:[105,44,88,106,107,57,14,108,109,68,110,111,112,113,114,115,116,117,118,119]}

Matriz_01=np.load('Distancias_todos_completa.npy')
cant_n=len(Nodos)
M_distancia = np.zeros([cant_n,cant_n])

s=1
while s==1:
    suma=0
    nodo1=int(input('ingresa el 1er nodo: '))
    nodo2=int(input('ingresa el 2do nodo: '))
    for i in range(11):
        if (nodo1 in Lineas_metro[i+1] and nodo2 in Lineas_metro[i+1]):
            linea = i+1
    if Lineas_metro[linea].index(nodo1)<Lineas_metro[linea].index(nodo2):
        pos_enlinea = Lineas_metro[linea].index(nodo1)
        estacion=nodo1
        fin = nodo2
    else:
        pos_enlinea = Lineas_metro[linea].index(nodo2)
        estacion=nodo2
        fin = nodo1
    while estacion!=fin:
        suma += Matriz_01[Lineas_metro[linea][pos_enlinea],Lineas_metro[linea][pos_enlinea+1]]
        estacion=Lineas_metro[linea][pos_enlinea+1]
        pos_enlinea += 1
    M_distancia[Nodos.index(nodo1),Nodos.index(nodo2)]=suma
    s=int(input('Deseas otro nodo? Si:1 No:0 '))
    
M_dis=M_distancia+M_distancia.T
np.save('Distancias_nodos',M_dis) 

#        1:["Observatorio","Tacubaya","Juanacatlan","Chapultepec","Sevilla","Insurgentes","Cuauhtemoc","Balderas",
#           "Salto del Agua","Isabel la Católica","Pino Suárez","Merced","Candelaria","San Lázaro","Moctezuma",
#           "Balbuena","Blvd. Pto Aereo","Gomez Farias","Zaragoza","Patitlán"],
#        2:["Cuatro Caminos","Panteones","Tacuba","Cuitláhuac","Popotla","Colegio Militar","Normal","San Cosme",
#           "Revolución","Hidalgo","Bellas Artes","Allende","Zócalo","Pino Suárez","San Antonio Abad","Chabacano",
#           "Viaducto","Xola","Villa de Cortés"],
#        3:["Indios Verdes","Deportivo 18 de Marzo","Potrero","La Raza","Tlatelolco","Guerrero","Hidalgo","Juárez",
#           "Balderas","Niños Héroes/Poder Judicial CDMX","Hospital General","Centro Médico","Etiopía / Plaza de la Transparencia",
#           "Eugenia","División del Norte"],
#        4:["Martín Carrera","Talismán","Bondojito","Consulado","Canal del Norte","Morelos","Candelaria","Fray Servando",
#           "Jamaica","Santa Anita"],
#        5:["Politecnico","Instituto del Petroleo","Autobuses Norte","La Raza","Misterios","Valle Gomez","Consulado",
#           "Eduardo Molina","Aragon","Oceania","Terminal Aerea","Hangares","Patitlan"],
#        6:["El Rosario","Tezozomoc","Azcapotzalco","Ferrería","Norte 45","Vallejo","Instituto del Petróleo","Lindavista",
#           "Deportivo 18 de Marzo","La Villa-Basílica","Martín Carrera"],
#        7:["El Rosario","Aquiles Serdán","Camarones","Refinería","Tacuba","San Joaquín","Polanco","Auditorio","Constituyentes",
#           "Tacubaya","San Pedro de los Pinos","San Antonio"],
#        8:["Garibaldi","Bellas Artes","San Juan de Letran","Salto del Agua","Doctores","Obrera","Chabacano","La Viga",
#           "Santa Anita","Coyuya"],
#        9:["Tacubaya","Patriotismo","Chilpancingo","Centro Medico","Lazaro Cardenas","Chabacano","Jamaica","Mixiuhca",
#           "Velodromo","Ciudad Deportiva","Puebla","Patitlán"],
#        10:["Pantitlan","Agricola Oriental","Canal de San Juan","Tepalcates","Guelatao"],
#        11:["Buenavista","Guerrero","Garibaldi","Lagunilla","Tepito","Morelos","San Lazaro","R. Flores Magon","R. Rubio",
#             "Oceania","Deportivo Oceania","Bosque Aragon","Villa de Aragon","Nezahualcoyotl","Impulsora","Rio de los Remedios",
#             "M. Muzquiz","Ecatepec","Olimpica","Plaza Aragon"]}

#Nodos=["Tacubaya","Balderas","Salto del Agua","Pino Suarez","Candelaria"]
       #,"San Lázaro","Pantitlán",
#       "Tacuba","Hidalgo","Bellas Artes","Chabacano",
#       "Deportivo 18 de Marzo","La Raza","Guerrero","Centro Médico",
#       "Martin Carrera", "Consulado","Morelos","Jamaica","Santa Anita",
#       "Instituto del Petróleo","Oceanía",
#       "El Rosario",
#       "Garibaldi"]
        