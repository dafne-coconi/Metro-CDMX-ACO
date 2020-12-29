from tkinter import *
from tkinter import ttk
import numpy as np
 
global M_tau
Lista_estaciones_alf=["Agricola Oriental","Allende","Aquiles Serdan","Aragon","Auditorio","Autobuses Norte","Azcapotzalco",
    "Balbuena","Balderas","Bosque Aragon","Bellas Artes","Blvd. Pto. Aereo","Bondojito","Buenavista","Camarones",
    "Canal del Norte","Canal de San Juan","Candelaria","Centro Medico","Chabacano","Chapultepec","Chilpancingo",
    "Ciudad Deportiva","Colegio Militar","Constituyentes","Consulado","Coyuya","Cuatro Caminos","Cuauhtemoc","Cuitlahuac",
    "Deportivo 18 de Marzo","Deportivo Oceania","Division del Norte","Doctores","Ecatepec","Eduardo Molina","El Rosario",
    "Etiopia","Eugenia","Ferreria","Fray Servando","Garibaldi","Gomez Farias","Guelatao","Guerrero","Hangares","Hidalgo",
    "Hospital General","Impulsora","Indios Verdes","Instituto del Petroleo","Insurgentes","Isabel la Catolica","Jamaica",
    "Juanacatlan","Juarez","Lagunilla","La Raza","La Viga","La Villa-Basilica","Lazaro Cardenas","Lindavista","Martin Carrera",
    "Merced","Misterios","Mixiuhca","M. Muzquiz","Moctezuma","Morelos","Nezahualcoyotl","Niños Heroes","Normal","Norte 45",
    "Obrera","Observatorio","Oceania","Olimpica","Panteones","Patitlan","Patriotismo","Pino Suarez","Plaza Aragon","Polanco",
    "Politecnico","Popotla","Potrero","Puebla","Refineria","Revolucion","R. Flores Magon","Rio de los Remedios","R. Rubio",
    "Salto del Agua","San Antonio","San Antonio Abad","San Cosme","San Joaquin","San Juan de Letran","San Pedro de los Pinos",
    "San Lazaro","Santa Anita","Sevilla","Tacuba","Tacubaya","Talisman","Tepalcates","Tepito","Terminal Aerea","Tezozomoc",
    "Tlatelolco","Valle Gomez","Vallejo","Velodromo","Viaducto","Villa de Aragon","Villa de Cortes","Xola","Zaragoza","Zocalo"]
       
raiz=Tk()
raiz.title ("Metro CDMX")
raiz.resizable(0,0)
raiz.iconbitmap("metro_logotipo.ico")  
raiz.config(bg="orange")

def boton_buscar():
    global M_tau
    txtrespuesta.delete('1.0', END)
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
    
    Lista_estaciones=["Observatorio","Tacubaya","Juanacatlan","Chapultepec","Sevilla","Insurgentes","Cuauhtemoc","Balderas","Salto del Agua",
        "Isabel la Catolica","Pino Suarez","Merced","Candelaria","San Lazaro","Moctezuma","Balbuena","Blvd. Pto. Aereo","Gomez Farias","Zaragoza",
        "Patitlan","Cuatro Caminos","Panteones","Tacuba","Cuitlahuac","Popotla","Colegio Militar","Normal","San Cosme","Revolucion","Hidalgo",
        "Bellas Artes","Allende","Zocalo","San Antonio Abad","Chabacano","Viaducto","Xola","Villa de Cortes","Indios Verdes","Deportivo 18 de Marzo",
        "Potrero","La Raza","Tlatelolco","Guerrero","Juarez","Niños Heroes","Hospital General","Centro Medico","Etiopia","Eugenia","Division del Norte",
        "Martin Carrera","Talisman","Bondojito","Consulado","Canal del Norte","Morelos","Fray Servando","Jamaica","Santa Anita","Politecnico",
        "Instituto del Petroleo","Autobuses Norte","Misterios","Valle Gomez","Eduardo Molina","Aragon","Oceania","Terminal Aerea","Hangares",
        "El Rosario","Tezozomoc","Azcapotzalco","Ferreria","Norte 45","Vallejo","Lindavista","La Villa-Basilica","Aquiles Serdan","Camarones","Refineria",
        "San Joaquin","Polanco","Auditorio","Constituyentes","San Pedro de los Pinos","San Antonio","Garibaldi","San Juan de Letran","Doctores","Obrera",
        "La Viga","Coyuya","Patriotismo","Chilpancingo","Lazaro Cardenas","Mixiuhca","Velodromo","Ciudad Deportiva","Puebla","Agricola Oriental",
        "Canal de San Juan","Tepalcates","Guelatao","Buenavista","Lagunilla","Tepito","R. Flores Magon","R. Rubio","Deportivo Oceania","Bosque Aragon",
        "Villa de Aragon","Nezahualcoyotl","Impulsora","Rio de los Remedios","M. Muzquiz","Ecatepec","Olimpica","Plaza Aragon"]
    
    Matriz_01=np.load('Distancias_todos_completa.npy')
    Matriz_nodos=np.zeros([26,26])
    Matriz_nodos[0:24,0:24]=np.load('Distancias_nodos.npy')
    
    inicio=cuadroinicio.get()
    fin=cuadrofin.get()
    Lista_estaciones.index(fin)+1
    
    
    
    if (fin in Lista_estaciones) and (inicio in Lista_estaciones):
        num_inicio=Lista_estaciones.index(inicio)+1
        num_fin=Lista_estaciones.index(fin)+1

        misma_linea=0        
        for i in range(11):
            if (num_inicio in Lineas_metro[i+1] and num_fin in Lineas_metro[i+1]):
                linea=i+1
                misma_linea=1
                break
        if misma_linea==1 and inicio!=fin:
            if linea==10:
                print("Viaja en la línea A del metro")
                txtrespuesta.insert(INSERT,"Viaja en la línea A del metro")
                txtrespuesta.insert(END,"")
            elif linea==11:
                print("Viaja en la línea B del metro")
                txtrespuesta.insert(INSERT,"Viaja en la línea B del metro")
                txtrespuesta.insert(END,"")
            else:
                print("Viaja en la línea ",linea," del metro")
                txtrespuesta.insert(INSERT,"Viaja en la línea "+str(linea)+" del metro")
                txtrespuesta.insert(END,"")
        elif misma_linea==1 and inicio==fin:
            print("Estás donde quieres estar")
            txtrespuesta.insert(INSERT,"Estás donde quieres estar")
            txtrespuesta.insert(END,"")
        else:
            # INICIAA ##########################################
            valor2=0
            if not(num_inicio in Nodos):
                Nodos.append(num_inicio)
                for i in range(11):
                    if num_inicio in Lineas_metro[i+1]:
                        linea_ac=i+1
                        break
                nodos_enlinea=[]
                for i in range(len(Lineas_metro[linea_ac])):
                    if Lineas_metro[linea_ac][i] in Nodos:
                        nodos_enlinea.append(i)
                d_1=0
                d_0=0
                pos_inicio=Lineas_metro[linea_ac].index(num_inicio)
                if nodos_enlinea[0]<pos_inicio:
                    valor2+=1
                    for j in range(pos_inicio,0,-1):
                        nn=Lineas_metro[linea_ac][j]
                        nn0=Lineas_metro[linea_ac][j-1]
                        d_0 += Matriz_01[nn,nn0]
                        if nn0 in Nodos:
                            dali=Nodos.index(nn0)
                            Matriz_nodos[len(Nodos)-1,dali]=d_0
                            Matriz_nodos[dali,len(Nodos)-1]=d_0
                            break
                if nodos_enlinea[-1]>pos_inicio:
                    valor2+=1
                    for j in range(pos_inicio,len(Lineas_metro[linea_ac])-1):
                        nn=Lineas_metro[linea_ac][j]
                        nn0=Lineas_metro[linea_ac][j+1]
                        d_1 += Matriz_01[nn,nn0]
                        if nn0 in Nodos:
                            dali=Nodos.index(nn0)
                            Matriz_nodos[len(Nodos)-1,dali]=d_1
                            Matriz_nodos[dali,len(Nodos)-1]=d_1
                            break
            
            if valor2==1:
                ver_inicio=num_inicio
                num_inicio=nn0 
                Nodos.pop()
                Matriz_nodos[len(Nodos),Nodos.index(nn0)]=0
                Matriz_nodos[Nodos.index(nn0),len(Nodos)]=0           
            
            valor2=0
            if not(num_fin in Nodos):
                Nodos.append(num_fin)
                for i in range(11):
                    if num_fin in Lineas_metro[i+1]:
                        linea_ac=i+1
                        break
                nodos_enlinea=[]
                for i in range(len(Lineas_metro[linea_ac])):
                    if Lineas_metro[linea_ac][i] in Nodos:
                        nodos_enlinea.append(i)
                d_1=0
                d_0=0
                pos_inicio=Lineas_metro[linea_ac].index(num_fin)
                if nodos_enlinea[0]<pos_inicio:
                    valor2+=1
                    for j in range(pos_inicio,1,-1):
                        nn=Lineas_metro[linea_ac][j]
                        nn0=Lineas_metro[linea_ac][j-1]
                        d_0 += Matriz_01[nn,nn0]
                        if nn0 in Nodos:
                            dali=Nodos.index(nn0)
                            Matriz_nodos[len(Nodos)-1,dali]=d_0
                            Matriz_nodos[dali,len(Nodos)-1]=d_0
                            break
                if nodos_enlinea[-1]>pos_inicio:
                    valor2+=1
                    for j in range(pos_inicio,len(Lineas_metro[linea_ac])-1):
                        nn=Lineas_metro[linea_ac][j]
                        nn0=Lineas_metro[linea_ac][j+1]
                        d_1 += Matriz_01[nn,nn0]
                        if nn0 in Nodos:
                            dali=Nodos.index(nn0)
                            Matriz_nodos[len(Nodos)-1,dali]=d_1
                            Matriz_nodos[dali,len(Nodos)-1]=d_1
                            break
            if valor2==1:
                ver_fin=num_fin
                num_fin=nn0
                Nodos.pop()
                Matriz_nodos[len(Nodos),Nodos.index(nn0)]=0
                Matriz_nodos[Nodos.index(nn0),len(Nodos)]=0                       
##############################################################################            
            cant_n=len(Nodos)                  
            M_dist=Matriz_nodos
            M_tau=np.zeros([cant_n,cant_n]) # Matriz de tau (feromonas)     
            
            M_tau=np.where(M_dist==0,M_dist,0.1)
            extra=np.where(M_dist!=0)
            num_con = extra[0].shape #número de conexiones
            
            alpha=1
            beta=2
            num_ants=cant_n+7
            
            
            N=0
            dist_op=np.sum(M_dist)
            RUTA_op=[]
            RUTAS_OP=[]          
#############################################################################
            for cambio_tau in range(5):
                rep=7
                for repeticiones in range(rep):
                    RUTAS=[]
                    DISTANCIAS=np.array([])
                    for i in range(num_ants): # NUMERO DE HORMIGAS
                        M_dist2=np.copy(M_dist)
                        ruta=np.array([num_inicio])
                        eleccion=Nodos.index(num_inicio)
                        contador = 0
                        dist = 0
                        while Nodos[eleccion]!=num_fin:
                            suma=0
                            Pxy=np.array([])
                            sum_Pxy=np.array([])
                            num_0 = Nodos.index(ruta[contador])
                            conexion=np.where(M_dist2[:,num_0]!=0) #qué otros nodos se conectan al actual
                            M_dist2=np.copy(M_dist)
                            for i in conexion[0]:
                                suma+=((1/M_dist[i,num_0])**beta)*(M_tau[i,num_0]**alpha)
                            contador2=0
                            for i in conexion[0]:        
                                Pxy=np.append(Pxy,((M_tau[i,num_0]**alpha)*((1/M_dist[i,num_0])**beta))/(suma))
                                if contador2==0:
                                    sum_Pxy=np.append(sum_Pxy,Pxy[contador2])
                                else:
                                    sum_Pxy=np.append(sum_Pxy,Pxy[contador2]+sum_Pxy[contador2-1]) #La suma de probabilidades
                                contador2+=1
                            num_rand = float(np.random.rand(1))
                            P_elegida = np.min(np.where(sum_Pxy>num_rand))
                            eleccion = conexion[0][P_elegida]
                            ruta=np.append(ruta,Nodos[eleccion])
                            dist+=M_dist[eleccion,num_0]
                            M_dist2[eleccion,num_0]=0
                            M_dist2[num_0,eleccion]=0
                            contador+=1
                            
                        RUTAS.append(ruta)
                        DISTANCIAS=np.append(DISTANCIAS,dist)
                    if dist_op>np.min(DISTANCIAS):
                        dist_op=np.min(DISTANCIAS)
                        RUTA_op=RUTAS[np.argmin(DISTANCIAS)]
                    RUTAS_OP.append(RUTAS[np.argmin(DISTANCIAS)])
                    # ACTUALIZACIÓN DE FEROMONAS
                rho=0.5
                NEW_Mtau=np.zeros([cant_n,cant_n])
                for i in range(num_con[0]): 
                    delta_tau=0
                    pp1=extra[0][i]
                    pp2=extra[1][i]
                    P1=Nodos[pp1]
                    P2=Nodos[pp2]
                    for j in range(rep): #para la SUMA
                        A = np.where(RUTAS_OP[j]==P1) 
                        B = np.where(RUTAS_OP[j]==P2)
                        aa = A[0].shape
                        bb = B[0].shape
                        if aa[0]>0 and bb[0]>0:
                            if (A[0][0]+1==(B[0][0])) or (A[0][0]==(B[0][0]+1)):
                                delta_tau+=M_dist[pp1,pp2]
                    TAU = (1-rho)*M_tau[pp1,pp2]+delta_tau
                    NEW_Mtau[pp1,pp2]=TAU
                M_tau=NEW_Mtau
#SE BUSCA QUÉ RUTA SIGUE LA MATRIZ DE TAU-CUÁL ES LA MÁS DESTACADA
            ruta_tau=[num_inicio]
            seguimiento_tau=[Nodos.index(num_inicio)]
            a=num_inicio
            b=Nodos.index(num_inicio)
            cont=0
            M_tau2=np.copy(M_tau)
            while a!=num_fin:
                if cont%2==0:
                    pos=np.argmax(M_tau2[Nodos.index(ruta_tau[cont]),:])
                    M_tau2[Nodos.index(ruta_tau[cont]),pos]=0
                else:
                    pos=np.argmax(M_tau2[:,Nodos.index(ruta_tau[cont])])
                    M_tau2[pos,Nodos.index(ruta_tau[cont])]=0
                a=Nodos[pos]
                b=pos
                ruta_tau.append(a)
                seguimiento_tau.append(b)
                cont+=1
                if cont>15:
                    a=num_fin
            print("\n Seguimiento Tau")
            print(ruta_tau)
            new_cont=0
            impresion=[]
            mov=""
            if len(ruta_tau)>len(RUTA_op):
                RUTAFINAL=RUTA_op
            else:
                RUTAFINAL=ruta_tau
            for i in RUTAFINAL:           
                if new_cont == 0:
                    mov+=str(i)+" Inicia en "+str(Lista_estaciones[i-1])+"\n"
                elif new_cont>0 and new_cont<len(RUTA_op)-1:
                    mov+=str(i)+" Viaja por "+str(Lista_estaciones[i-1])+"\n"
                else:
                    mov+=str(i)+" Termina en "+str(Lista_estaciones[i-1])
                new_cont+=1
            txtrespuesta.insert(INSERT,mov)
            txtrespuesta.insert(END,"")
    else:
        txtrespuesta.insert(INSERT,"Lo siento. No entendí ):\n Intenta de nuevo")
        txtrespuesta.insert(END,"")
# ------------------------- TERMINA BOTON --------------------------------

#FRAME DEL TITULO 
frameT=Frame(raiz,width="400",height="80")
frameT.pack()
frameT.config(bg="orange")


#FRAME DE LA IMAGEN 
frameM=Frame(raiz,width="700",height="500")
frameM.pack(side="left")
frameM.config(bg="orange")

#FRAME DE LA BUSQUEDA 
frameS=Frame(raiz,width="500",height="600")
frameS.pack(side="right", anchor="n")
frameS.config(bg="orange")

###########################################################
#IMAGEN DEL METRO 
imagenM=PhotoImage(file="MapaMetro.png")
labelM=Label(frameM,image=imagenM)
labelM.place(x=20,y=1)

# TEXTO DEL TITULO 
labelT=Label(frameT,text="ACO METRO",font=("Arial Narrow",25))
labelT.place(x=80,y=25)
labelT.config(bg="orange")

# TEXTO DEL RESPUESTA 
labelA=Label(frameS,text="¿A dónde quieres ir?",font=("Arial Narrow",15))
labelA.place(x=150,y=20)
labelA.config(bg="orange")
#----------------- TEXTO DE RESPUESTA--------------------------
labelA=Label(frameS,text="RUTA A SEGUIR",font=("Arial Narrow",10))
labelA.place(x=50,y=200)
labelA.config(bg="orange")

texto=StringVar()
txtrespuesta=Text(frameS,width=40,height=14)#,state=DISABLED)
txtrespuesta.place(x=50,y=245)
txtrespuesta.config(bg="white")
#----------------- TEXTO DE INICIO -----------------------------
cuadroinicio=ttk.Combobox(frameS)#,state="readonly")
cuadroinicio["values"]=Lista_estaciones_alf
cuadroinicio.place(x=110,y=100)

labelinicio=Label(frameS,text="INICIO:",font=("Arial Narrow",10))
labelinicio.place(x=45,y=100)
labelinicio.config(bg="orange")
#----------------- TEXTO DE FIN -----------------------------
cuadrofin=ttk.Combobox(frameS)#,state="readonly")
cuadrofin["values"]=Lista_estaciones_alf
cuadrofin.place(x=110,y=140)

labelfin=Label(frameS,text="FIN:",font=("Arial Narrow",10))
labelfin.place(x=45,y=140)
labelfin.config(bg="orange")
#------------------ BOTON-------------------------------------
Bbuscar=Button(frameS,text="Buscar",command=boton_buscar)
Bbuscar.place(x=350,y=115)
Bbuscar.config(bg="white")


raiz.mainloop()