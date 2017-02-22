# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 09:23:21 2017

@author: carlo
"""


def Dummy():
    global Var_0
    print Var_0.get()
    return()

def Search_File():
    
    global Excel, Flag_00, Var_0
    
    file    = tkFileDialog.askopenfilename()
    Excel   = openpyxl.load_workbook(file) 
    Names   = Excel.sheetnames
    DDM_0   = OptionMenu(top, Var_0, *Names)
    
    if Flag_00 == 1:
        DDM_0.pack_forget()
        
    Var_0.set('Select Sheet')
    DDM_0.place(x=105,y=0,height=30, width=200)
    Flag_00    = 1

def Acquire_Sheets():
    global Sheet, Sheet_2, Var_0, Stops , Flags, Sub_List_Variables, Sub_Index_Cat
    global List_Variables,  Sub_List_Cat,  List_Variables
    global Index_Variables, Index_Gender, Index_Variables
    global Amount_People, List_Cat
    
    Sheet   = Excel.get_sheet_by_name(Var_0.get())
    Sheet_2   = Excel.get_sheet_by_name("Hoja1") 
    
    List_Variables  = []
    Sub_List_Variables = []

    Index_Variables = []
    Sub_Index_Variables = []


    List_Cat  = []
    Sub_List_Cat = []

    Index_Cat = []
    Sub_Index_Cat = []

    Amount_People   = 0

    a = 0
    h = 1
    Flags = []
    Stops = []

    while a == 0:
        f = str(Sheet.cell(row=1, column=h).value)
        if f == 'Finito':
            a = 1
        if 'Flag' in f:
            Flags.append(h)
        if 'Stop' in f:
            Stops.append(h)
        h =h+1
    
    while a == 0:
        f = str(Sheet.cell(row=1, column=h).value)
        if f == 'Finito':
            a = 1
        if 'Flag' in f:
            Flags.append(h)
        if 'Stop' in f:
            Stops.append(h)
        h =h+1
    
    print Stops
    temp_0 = []
    temp_1 = []

    for k in range(len(Stops)-1):
        for i in range (Stops[k]+1,Stops[k+1],1):
            temp_0.append(Sheet.cell(row=2, column=i).value)
            List_Variables.append(Sheet.cell(row=2, column=i).value)
            temp_1.append(i)
            Index_Variables.append(i)
        Sub_List_Variables.append(temp_0)
        Sub_Index_Variables.append(temp_1)
        temp_0 = []
        temp_1 = []

    Sub_Tags_Variables = []
    for i in range(1,len(Flags),1):
        Sub_Tags_Variables.append(str(Sheet.cell(row=2, column=Flags[i-1]).value))
        
    temp_0 = []
    temp_1 = []

    for k in range(len(Flags)-1):
        for i in range (Flags[k]+1,Flags[k+1],1):
            temp_0.append(Sheet.cell(row=2, column=i).value)
            List_Cat.append(Sheet.cell(row=2, column=i).value)
            temp_1.append(i)
            Index_Cat.append(i)
        Sub_List_Cat.append(temp_0)
        Sub_Index_Cat.append(temp_1)
        temp_0 = []
        temp_1 = []

    Sub_Tags_Cat = []
    for i in range(1,len(Stops),1):
        Sub_Tags_Cat.append(str(Sheet.cell(row=2, column=Stops[i-1]).value))
        
    print len(Sub_List_Variables[0])
    print len(Sub_List_Variables[1])
    print len(Sub_List_Variables[2])
    
    i=1
    Aux_0=0
    while Aux_0 != None:
        Aux_0 = Sheet.cell(row=i, column=1).value
        i = i + 1
    Amount_People = i-4
               
    print 'cantidad de Variables  ', len(List_Variables)
    print 'Cantidad de Encuestados', Amount_People


def Create_Window():
    
    global my_objects, Variable_CB_0, Variable_CB_1, Variable_CB_2
    global SW, Var_G2, Var_G3, Flag_5, Sub_List_Cat, Sub_List_Variables
    Flag_5  = 0
    Row     = 0
    Column  = 0
    Variable_CB_0    = []
    Variable_CB_1    = []
    Variable_CB_2    = []

    SW      = Tkinter.Toplevel()
    SW.geometry = ("1000x400")
    SW.wm_title("Select Variable")
    
    labelframe = LabelFrame(SW, text="Variables")
    labelframe.grid(sticky=W+E,row=0, column=0)
    frame = Frame(labelframe, bd=1)
    
    my_objects = []
    for i in range(len(List_Variables)):
        my_objects.append(object)
    
    k = 0
    Row = 0
    Column = 0
    for i in List_Variables:
        Var_G   = IntVar()
        my_objects[k]    = Checkbutton(frame, text=i, variable=Var_G)
        my_objects[k].grid(sticky=W, row=Row, column=Column)
        Column  = Column + 1
        if Column > 5:
            Row     = Row + 1
            Column  = 0
        Variable_CB_0.append(Var_G)
        k = k + 1
    frame.grid(sticky=W, row=0, column=0)


    k = 0
    Row = 0
    Column = 0
    labelframe2 = LabelFrame(SW, text="Genero")
    labelframe2.grid(sticky=W+E,row=1, column=0)
    frame2 = Frame(labelframe2, bd=1)
    
    my_objects_1 = []
    for i in range(len(Sub_List_Cat[0])):
        my_objects_1.append(object)

    Var_G2   = IntVar()
    for i in Sub_List_Cat[0]:
        my_objects_1[k]    = Radiobutton(frame2, text=i, variable=Var_G2, value=k)
        my_objects_1[k].grid(sticky=W, row=Row, column=Column)
        Column  = Column + 1
        if Column > 5:
            Row     = Row + 1
            Column  = 0
        k = k + 1
    frame2.grid(sticky=W+E,row=0, column=0)
    
    
    k = 0
    Row = 0
    Column = 0
    labelframe3 = LabelFrame(SW, text="Parametro")
    labelframe3.grid(sticky=W+E,row=2, column=0)
    frame3 = Frame(labelframe3, bd=1)
    
    my_objects_2 = []
    for i in range(len(Sub_List_Cat[1])):
        my_objects_2.append(object)

    Var_G3   = IntVar()
    for i in Sub_List_Cat[1]:
        my_objects_2[k]    = Radiobutton(frame3, text=i, variable=Var_G3, value=k)
        my_objects_2[k].grid(sticky=W, row=Row, column=Column)
        Column  = Column + 1
        if Column > 5:
            Row     = Row + 1
            Column  = 0
        k = k + 1
    frame3.grid(sticky=W+E,row=0, column=0)

    labelframe4 = LabelFrame(SW, text="Opciones")
    labelframe4.grid(sticky=W,row=3, column=0)
    frame4 = Frame(labelframe4, bd=1)
    
    B_0     = Tkinter.Button(frame4, text = "Cerrar"    , command = Close)
    B_1     = Tkinter.Button(frame4, text = "Var_1 "    , command = Toggle_00)
    B_2     = Tkinter.Button(frame4, text = "Var_2 "    , command = Toggle_01)
    B_3     = Tkinter.Button(frame4, text = "Var_3 "    , command = Toggle_02)
    B_4     = Tkinter.Button(frame4, text = "Leyenda"   , command = Leyenda)
    
    k = 0
    for i in [B_0,B_1,B_2,B_3,B_4]:
        i.grid(row = 0, column = k, padx=5)
        k = k + 1
    frame4.grid(sticky=W+E,row=0, column=0)
    SW.mainloop()
    
def Toggle_00():
    global my_objects, Sub_List_Variables
    for i in range(len(Sub_List_Variables[0])):
        my_objects[i].toggle()

def Toggle_01():
    global my_objects, Sub_List_Variables
    for i in range(len(Sub_List_Variables[0]),len(Sub_List_Variables[0])+len(Sub_List_Variables[1]),1):
        my_objects[i].toggle()
        
def Toggle_02():
    global my_objects, Sub_List_Variables
    for i in range(len(Sub_List_Variables[0])+len(Sub_List_Variables[1]),len(Sub_List_Variables[0])+len(Sub_List_Variables[1])+len(Sub_List_Variables[2]),1):
        my_objects[i].toggle()

def Table ():                                         
    global New_Ind_0, New_Ind_1, Amount_People, Index_Variables, Index_Gender, Sub_Index_Cat
    global Tabla_Datos, Lista_Indice, New_Ind_2, State_2, Var_G2, Var_G3
    global Var_G6, Index_Variables, Name_Fin

    State_0 = map((lambda var: var.get()), Variable_CB_0)
    State_1 = Var_G2.get() 
    State_2 = Var_G3.get() 
    New_Ind_0 = []
    New_Ind_1 = []
    New_Ind_2 = []
    
    print "Variables"
    for i in range(len(State_0)):
        if State_0[i] == 1:
            print i, List_Variables[i]
            New_Ind_0.append(Index_Variables[i])
    print ''
    
    print "Genero"    
    print State_1, Sub_List_Cat[0][State_1]
    New_Ind_1.append(Sub_Index_Cat[0][State_1])
    print ''
    Name_Fin = str(Sub_List_Cat[0][State_1]) + '_'
    
    print "Parametro"        
    print State_2, Sub_List_Cat[1][State_2]
    New_Ind_2.append(Sub_Index_Cat[1][State_2])
    print '-----------5--------------'
    print New_Ind_2
    Name_Fin = Name_Fin + str(Sub_List_Cat[1][State_2]) + '_'

    Flag_0      = 0                                                             #Bandera para discriminar celdas vacias
    Aux_0       = 0                                                             #Auxiliar 0, valor de la celda de datos                                                            #Auxiliar 1, valor de la celda de la variable
    Lista_Indice= []                                                            #Lista donde se almacena el indice de la tabla de datos 
    Lista_Temp  = []                                                            #Vector auxiliar para armar la Matriz
    Tabla_Datos = numpy.zeros((0, len(New_Ind_0)))                              #Matriz con los datos de dimensiones 0x(Numero de variables)
    
    for i in range (3, Amount_People, 1):                                       #Desde la primera Columna hasta la ultima
        Flag_0 = 0                                                              #Bandera en 0
        for j in New_Ind_0:                                                     #Desde la primera Fila hasta la ultima
            Aux_0 = Sheet.cell(row=i, column=j).value                           #Aux_0 toma el valor de datos de la celda leida                        #Aux_1 toma el valor de la variable en la misma fila
            if Aux_0 is None or Val_Check_0(i) == 1:                                  #Si ni la celda de la variable ni la del dato carecen de valor
                Flag_0 = 1                                                      #Bandera en 1
            else:
                Aux_0 = Sheet.cell(row=i, column=j).value * 1.0                 #Valor de la tabla pasa de int a float
                Lista_Temp.append(Aux_0)                                        #Se crea una lista temporal con el valor de la celda de datos
        if Flag_0 == 0:                                                         #Si la bandera no fue levantada
            Tabla_Datos = numpy.vstack((Tabla_Datos,Lista_Temp))                #Se agrega la lista de datos sobre la Tabla que se esta generando
            Lista_Indice.append(i)                                              #Srea una lista indice de la tabla original del Excel
        Lista_Temp = []                                                         #Se reinicia la lista para la siguiente fila                                         #Devuelve la Tablaz y el Indice

    global vart
    vart = IntVar()
    scale = Scale( top,label="    Number of Clusters", orient=HORIZONTAL, variable = vart, from_= 2, to=10,length=200, width= 28)
    scale.set(3)
    scale.place(x=130,y=32,width=150)
    
    Var_G6   = IntVar()
    my_objects_5 = []
    for i in range(3):
        my_objects_5.append(object)
    k = 0
    d = 0
    for i in ["Kmeans","MeanShift","DBSCAN"]:
        my_objects_5[k]    = Radiobutton(top, text=i, variable=Var_G6, value=k)
        my_objects_5[k].place(x = 120, y = 105 + d * 20)
        k = k + 1
        d = d + 1
    print Tabla_Datos

def Close():
    SW.destroy()

def test():
    State_0 = map((lambda var: var.get()), Variable_CB_0)
    for i in range(len(List_Variables)):
        if State_0[i] == 1:
            print list[i]
    
def Val_Check_0(k):
    Aux_0 = 0
    Vec_0 = []
    for i in range(len(Index_Variables)):
        Aux_0 = Sheet.cell(row=k, column=Index_Variables[i]).value
        Vec_0.append(Aux_0)
    if numpy.count_nonzero(Vec_0) < len(Vec_0):
        return(1)
    else:
        return(0)
    
def Process():
    global Variables, labels, Rango, Flag_5, Tabla, Indice, g, h, Tabla_Datos
    global Lista_Cluster, Lista_Position, Lista_Indice, n_clusters_, List_Cat
    global List_Countries, cluster_centers, Var_G5, Var_G6, Name_Fin, Distancias_Vectoriales
    
    Book                = xlwt.Workbook()                                           #Parametro para grabar nueva hoja de Excel
    Sheet_1             = Book.add_sheet('sheet1')                                  #Hoja dentro del nuevo archivo donde se guardaran los datos
    Indice              = []
    Tabla               = []
    Tabla               = Tabla_Datos
    Indice              = Lista_Indice
    
    if Var_G6.get() == 0:
        kmeans              = KMeans(n_clusters=vart.get())                                      #Inicializacion de Kmeans con 3 Clusters
        kmeans.fit(Tabla)                                                               #Ejecutar Kmeans sobre la Tabla
        labels              = kmeans.labels_                                            #Etiqueta representando a que cluster pertenece cada elemento de la tabla
        n_clusters_         = len(numpy.unique(labels))                                 #Cantidad de Clusters
        cluster_centers     = kmeans.cluster_centers_                                   #Posicion de los Centros de cada Cluster
    elif Var_G6.get() == 1:
        ms = MeanShift()
        ms.fit(Tabla)
        labels = ms.labels_
        n_clusters_ = len(numpy.unique(labels))
        cluster_centers = ms.cluster_centers_
    else:
        db = DBSCAN(eps=0.3, min_samples=10).fit(Tabla)
        core_samples_mask = numpy.zeros_like(db.labels_, dtype=bool)
        core_samples_mask[db.core_sample_indices_] = True
        labels = db.labels_
        n_clusters_ = len(numpy.unique(labels))
 
    
    Variables           = var_4(Indice, New_Ind_2[0])  
    print '--------------5'
    print Variables
    Criteria            = []
    Criteria.append(Sub_List_Cat[1][State_2])    
    print Criteria
    Rango = []
    if Criteria[0] == "Age":
        Lista_Position, Lista_Cluster, Rango = Intervalos_0(Variables, labels, Indice)             #Separar en Sub-listas con los rangos de a 5 en 5
    else:
        List_Countries = []
        Ind, aux = numpy.unique(Variables, return_counts=True)    #Ver cuantos elementos                                                  #unicos estan en la                                                   #lista
        for i in range(len(aux)):
            if aux[i] >= 35:
                List_Countries.append(Ind[i])
    
        Lista_Cluster   = []
        Lista_Position  = []
        Index_Aux_0     = []
        Index_Aux_1     = []
        
        for i in range(len(List_Countries)):
            for j in range(len(Variables)):
                if Variables[j]==List_Countries[i]:
                    Index_Aux_0.append(labels[j])
                    Index_Aux_1.append(Indice[j])
            Lista_Cluster.append(Index_Aux_0)
            Lista_Position.append(Index_Aux_1)
            Index_Aux_0 = []
            Index_Aux_1 = []

    Tabla_Porcentual = []                                                           #Tabla de Clusters expresada en porcentajes cada lista con respecto a si misma
    for i in range(len(Lista_Cluster)):                                             #Iteracion por el largo de la lista de Clusters
        Ind_0, Val_0 = numpy.unique(Lista_Cluster[i], return_counts=True)           #Indice de elementos unicos y sus cantidades
        Aux_0 = copy.copy(Val_0)                                                    #Copiar la tabla de cantidades a una auxiliar
        Aux_0 = Aux_0 * 1.0                                                         #Nueva tabla expresada con puntos decimales
        Aux_0 = Porcentaje(Aux_0)                                                   #Tabla de cantidades expresada en porcentaje con respecto a si misma
        if sum(Val_0)>=35: 
            if Criteria[0] != "Age":
                Rango.append(List_Countries[i])                                                         #Se guarda el rango de edades
            Tabla_Porcentual.append(Aux_0)      
    
    k = 0
    for i in range(len(Tabla_Porcentual)):
        if len(Tabla_Porcentual[i]) > k:
            k = len(Tabla_Porcentual[i])
    
    for i in range(len(Tabla_Porcentual)):
        for j in range(len(Tabla_Porcentual[i]),k,1):
            Tabla_Porcentual[i] = numpy.append(Tabla_Porcentual[i],0)
    
    for i in range(0,len(Tabla_Porcentual),1):                                      #Visualizar la lista
        if Criteria[0] == "Age":        
            print 'Rango    ', int(Rango[i]), '-' ,int(Rango[i]+5)                          #Mostrar los rangos de edades
        else:
            print 'Rango    ', Rango[i]
        print 'Elementos', Tabla_Porcentual[i]                                      #Mostrar la ponderacion porcentual
    
    SW2                 = Tkinter.Toplevel()
    if Var_G6.get() == 0:
        SW2.wm_title("Metodo de Clusterizacion: Kmeans  " + "Numero de Clusters: " + str(vart.get()))
    elif Var_G6.get() == 1:
        SW2.wm_title("Metodo de Clusterizacion: MeanShift")
    else:
        SW2.wm_title("Metodo de Clusterizacion: DBSCAN")
    
    if Criteria[0] == "Age":        
        Aux_0 = ()                                                                      #Auxliar para el texto de cada fila y columna
        for i in range(0,len(Rango),1):                                                 #Iteracion por la cantidad de rangos
            Aux_0 = (int(Rango[i]),'-',(int(Rango[i]+5)))                                     #Texto para el titulo de las filas y columnas
            Label(SW2,text=Aux_0, relief=GROOVE,width=15).grid(row=i+1,column=0)            #Rangos como titulos en las filas
            Label(SW2,text=Aux_0, relief=GROOVE,width=15).grid(row=0,column=i+1)            #Rangos como titulos en las columnas
            Sheet_1.write(i+1,0,str((Rango[i]*5,'-',(Rango[i]+1)*5)))                   #Guardar las filas en un archivo de excel
            Sheet_1.write(0,i+1,str((Rango[i]*5,'-',(Rango[i]+1)*5)))                   #Guardar las columnas en un archivo de excel
    else:
        Aux_0 = ()                                                                      #Auxliar para el texto de cada fila y columna
        for i in range(0,len(Rango),1):                                                 #Iteracion por la cantidad de rangos
            Aux_0 = (Rango[i])                                     #Texto para el titulo de las filas y columnas
            Label(SW2,text=Aux_0, relief=GROOVE,width=15).grid(row=i+1,column=0)            #Rangos como titulos en las filas
            Label(SW2,text=Aux_0, relief=GROOVE,width=15).grid(row=0,column=i+1)            #Rangos como titulos en las columnas
            Sheet_1.write(i+1,0,str((Aux_0)))                   #Guardar las filas en un archivo de excel
            Sheet_1.write(0,i+1,str((Aux_0)))                   #Guardar las columnas en un archivo de excel

    Aux_1 = 0                                                                       #Variable Auxiliar
    Distancias_Vectoriales = []                                                     #Lista para las distancias vectoriales
    for i in range(len(Tabla_Porcentual)):                                      #Iteracion por el numero de filas
        for j in range(len(Tabla_Porcentual)):                                  #Iteracion por el numero de columnas
            Aux_1 = vector(Tabla_Porcentual[i],Tabla_Porcentual[j])           #Calcular distancias entre dos puntos
            Distancias_Vectoriales.append(Aux_1)                                    #Guardar las distancias en una lista
            
    Distancias_Vectoriales = Escalar(Distancias_Vectoriales, 255 , 4)               #Convertir las distancias a una escala de 255
    
    Aux_2 = 0                                                                       #Variable Auxiliar
    Aux_3 = 0                                                                       #Contador
    for i in range(0,len(Rango),1):                                                 #Iteracion por el numero de filas
        for j in range(0,len(Rango),1):                                             #Iteracion por el numero de Columnas
            Aux_2 = Distancias_Vectoriales[Aux_3]                                   #Auxiliar es igual a la distancia entre el rango de las filas y el rango de las columnas
            #Color_1 = '#%02x%02x%02x' % ((0),(0),(1*Aux_2))                       #Color de la celda proporcional al valor de la distancia, en escala de grises
            Color_1 = '#%02x%02x%02x' % gradient[int(Aux_2)]                      #Color de la celda proporcional al valor de la distancia, en escala de grises
            Color_2 = '#%02x%02x%02x' % (0, 0, 0)           #Color para el texto inverso al color de la celda
            Label(SW2,text=("%.1f" % Aux_2), bg=Color_1, fg=Color_2, 
                  relief=RIDGE, width=15).grid(row=i+1, column=j+1)                 #Crea una celda en la ventada de Display
            Sheet_1.write(i+1, j+1, Aux_2)                                          #Guarda el valor en la celda correspondiente
            Aux_3 = Aux_3 + 1                                                        #Contador incrementa en 1

    Var_G5   = IntVar()
    my_objects_3 = []
    for i in range(2):
        my_objects_3.append(object)
    k = 0
    d = 0
    for i in ["TSNE","MDS"]:
        my_objects_3[k]    = Radiobutton(top, text=i, variable=Var_G5, value=k)
        my_objects_3[k].place(x = 220, y = 105 + d * 20)
        k = k + 1
        d = d + 1

    Flag_5 == 0
    st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H;%M;%S')
    Aux_G = ["Kmeans","MeanShift","DBSCAN"]
    if Var_G6.get() == 0:
        Name_Fin = Name_Fin + str(Aux_G[Var_G6.get()]) + '_' + str(vart.get()) +'_' +st
    else:
        Name_Fin = Name_Fin + str(Aux_G[Var_G6.get()])+'_' +st
    print Name_Fin
    name = 'Table_' + Name_Fin +'.xls'                                                         #Nombre del Archivo de Excel
    Book.save(name)                                                                 #Grabar archivo Excel con el nombre definido
    Book.save(TemporaryFile())                                                      #Grabar archivo Excel en la carpeta Definida 
    net()
    mainloop()
    
def TaC(Indice):
    Ind, aux = numpy.unique(Indice, return_counts=True)    #Ver cuantos elementos                                                  #unicos estan en la                                                   #lista
    for i in range(0,len(Ind),1):        #De 0 hasta la cantidad de intervalos
        for j in range(0,len(Indice),1): #De 0 hasta la cantidad de elemtneos
            if Indice[j] == Ind[i]:      #Si el elemento es igual al del indice
                Indice[j] = i            #Elemento guardado en la matriz
    return Indice                        #Retornar matriz

def Graphic():
    global Lista_Position, Lista_Indice, Lista_Cluster, List_Countries, Name_Fin
    global g, h, cluster_centers, Flag_5, Rango, Var_G5, Var_G6, vart,n_clusters_,Rango
    
    if Flag_5 == 0:
        n_components = 2
        if Var_G5.get() == 0:
            Trans = manifold.TSNE(n_components=n_components, init='pca', random_state=0, perplexity=05)
        else:
            Trans = manifold.MDS(n_components=n_components, random_state=0)
        if Var_G6.get() != 2:
            Combinadas = armar(Tabla, cluster_centers)
            Desdoblada = Trans.fit_transform(Combinadas)
            g, h = desarmar(Desdoblada, n_clusters_)
        else:
            g = Trans.fit_transform(Tabla)
    Flag_5 = 1
    
    Aux_0 = []
    for i in range(len(Lista_Position)):
        Aux_0 = Aux_0 + Lista_Position[i]

    Aux_1 = []
    for i in range(len(Aux_0)):
        Aux_1.append(Lista_Indice.index(Aux_0[i]))
        
    Aux_2 = []
    for i in range(len(Lista_Cluster)):
        Aux_2 = Aux_2 + Lista_Cluster[i]

    if New_Ind_2[0] != 5:
        Variables = var_4(Aux_0, New_Ind_2[0])     
        Aux_3 = []
        for i in range (len(Variables)):
            for j in range (len(List_Countries)):
                if Variables[i]==List_Countries[j]:
                    Aux_3.append(j)
    else:
        Variables = var_4(Aux_0, New_Ind_2[0])     
        Aux_3 = []
        List_Countries = []
        for i in range (len(Variables)):
            k = 0            
            for j in Rango:
                if Variables[i] < (j) and Variables[i]>=((j-5)):
                    Aux_3.append(k)
                k = k + 1 
        for i in Rango:
            Rango_0 = str(int(i)) + '-' + str(int(i-5))
            List_Countries.append(Rango_0)
            
    Aux_G = ["Kmeans","MeanShift","DBSCAN"]
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    ax1.tick_params(
        axis='both',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom='off',      # ticks along the bottom edge are off
        top='off',         # ticks along the top edge are off
        labelbottom='off') # labels along the bottom edge are off
    ax2.tick_params(
        axis='both',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom='off',      # ticks along the bottom edge are off
        top='off',         # ticks along the top edge are off
        labelbottom='off') # labels along the bottom edge are off
    plt.rcParams['figure.figsize'] = 16, 7
    if Var_G5.get() == 0:
        f.canvas.set_window_title('TSNE' + '_' + Aux_G[Var_G6.get()] + '_' + '# Clusters' + str(n_clusters_))
    else:
        f.canvas.set_window_title('MDS' + '_' + Aux_G[Var_G6.get()] + '_' + '# Clusters' + str(n_clusters_))  
    
    
        
    k = 0
    for i in Aux_1:
        ax1.plot(g[i][0], g[i][1], c=colors[Aux_2[k]], marker='o', markersize = 5)
        ax1.set_title('Clusters')
        k = k + 1
    my_objects_5 = []
    for i in range(n_clusters_):
        my_objects_5.append(object)
    
    k = 0
    for i in range (n_clusters_):
        my_objects_5[k] = mpatches.Patch(color=colors[k], label=str(i+1))
        k = k + 1
    Handles = []
    for i in range(k):
        Handles.append(my_objects_5[i])
        
    plt.legend(bbox_to_anchor=(1, 1),handles=Handles)

    k = 0
    for i in Aux_1:        
        if New_Ind_2[0] == 5:
            ax2.plot(g[i][0], g[i][1], c=colors[Aux_3[k]], marker='o', markersize = 5)
            ax2.set_title('Rangos de Edades')
        else:
            ax2.plot(g[i][0], g[i][1], c=colors[Aux_3[k]], marker='o', markersize = 5)
            ax2.set_title('Paises')
        k = k + 1
        
    if Var_G6.get() != 2:
        for i in range(len(h)):
            ax1.plot(h[i][0], h[i][1], c="black", marker='*', markersize = 10)

    my_objects_4 = []
    for i in range(len(List_Countries)):
        my_objects_4.append(object)
    
    k = 0
    for i in List_Countries:
        my_objects_4[k] = mpatches.Patch(color=colors[k], label=i)
        k = k + 1
        
    Handles = []
    for i in range(k):
        Handles.append(my_objects_4[i])
    if New_Ind_2[0] != 7:
        plt.legend(bbox_to_anchor=(1.15, 1),handles=Handles)
    else:
        plt.legend(bbox_to_anchor=(1.35, 1),handles=Handles)
    plt.savefig('Graph' + Name_Fin + '.png', bbox_inches='tight')
    plt.show()
###############################################################
#Muestra en Pantalla los elementos de la lista, linea por linea
#Muestra el largo de cada linea y la cantidad total de elmentos
###############################################################
def Show_List(Array):                                           
    print len(Array)                                                            #Cantidad de Sub-Listas en la lista principal
    Elementos_Totales = 0                                                       #Contador de Elementos dentro de las sublistas
    for i in range(len(Array)):                                                 #Bucle por la cantidad de elementos dentro de la lista principal
        print Array[i], len(Array[i])                                           #Mostrar la sub-lista i y la cantidad de elementos de esta misma
        Elementos_Totales = Elementos_Totales + sum(Array[i])                   #Contador de elementos totales de las sublistas
    print Elementos_Totales                                                     #Mostrar Cantidad Total de elementos
    
    return ()

###############################################################
#Separa los elementos de una lista en intervalos de a 5 
#del 0-100 y devuelve dos nuevas listas, una con 20 sub-lsitas
#con las posiciones de la tabla original y la segunda con los
#clusters a los que cada uno pertenece
###############################################################
def Intervalos_0(Lista, Clusters, Indice):
    Aux_0 = []                                                                  #Array Auxiliar 0
    Aux_1 = []                                                                 #Array Auxiliar 1
    Lista_Posiciones = []                                                       #Array para las Posiciones con respecto al Array Original
    Lista_Clusters = []                                                         #Array con el cluster al que pertenece cada elemento
    Intervalos = numpy.linspace(0, 100, 21)                                     #Lista de intervalos del 0-100 de a 5 en 5
    for i in range(1,len(Intervalos),1):                                        #Desde el segundo elemento del intervalo hasta el ultimo
        for j in range(len(Lista)):                                             #Bucle por la cantidad de elementos del Array principal
            if Lista[j]<Intervalos[i] and Lista[j]>=Intervalos[i-1]:            #Si el elemento del Array esta entre el rago de intervalos
                Aux_0.append(Indice[j])                                         #Lista temporal con los elementos que entran en ese rango
                Aux_1.append(Clusters[j])                                       #Lista Temporal con el Cluster al que pertenecen
        if len(Aux_0)>35:
            Rango.append(Intervalos[i])
            Lista_Posiciones.append(Aux_0)                                          #Lista con sub-listas clasificadas por Rangos
            Lista_Clusters.append(Aux_1)                                            #Lista con sub-listas clasificadas por Clusters
        Aux_0 = []                                                              #Reiniciar la lista temporal de Posiciones
        Aux_1 = []                                                              #Reiniciar la lista temporal de Clusters 
    return (Lista_Posiciones, Lista_Clusters, Rango)                                   #Retorna la lista de posiciones y la lista de clusters


###############################################################
#Crea una lista con el parametro designado tomando en cuenta
#el indice generado en la funcion tabla
###############################################################

def var_4(Indice, Parametro):                                                     
    Lista_Parametro = []                                                        #Vector Auxiliar
    Aux_0 = 0    
    for i in range(0, len(Indice), 1):                                          #Desde 0 hasta la ultima posicion del Indice
        Aux_0 = Sheet.cell(row=Indice[i], column=Parametro).value               #Aux_0 toma el valor de la celda
        Lista_Parametro.append(Aux_0)                                           #Cargar el valor de la celda en la lista
        
    return (Lista_Parametro)                                                    #Devolver la lsita del Parametro

###############################################################
#Funcion para medir la distancia vectorial entre 2 puntos de
#en un plano cartesiano de 3 dimensiones
###############################################################

def vector(Vec_0, Vec_1):                                             #Distancia Vectorial entre 2 puntos
    Aux_0 = 0
    for i in range(len(Vec_0)):
        Aux_0 = Aux_0 + math.pow((int(Vec_0[i]-Vec_1[i])),2)
    Dis = math.sqrt(Aux_0)           #Formula de distancia vectorial
    
    return (Dis)                                                                #Devuelve la Distancia calculada

###############################################################
#Funcion para escalar una lista con un valor dado
###############################################################

def Escalar(Array , Value, Decimal):                                            
    Max = numpy.amax(Array)                                                     #Valor maximo dentro de la lista
    Lista_Escalada = []                                                         #Nueva lista escalada
    for i in range(len(Array)):                                                 #Iteracion por el largo de la lista
        Lista_Escalada.append(round((Array[i] * Value / Max), Decimal))         #Escala al numero designado y redondeado con los decimales designados
    
    return (Lista_Escalada)                                                     #Devuelve Lista Escalada

###############################################################
#Funcion Para convertir una lista a su equivalente en 
#porcentajes con respecto a todos los elementos de la misma
###############################################################

def Porcentaje(Lista):                                                          
    if len(Lista)>0:                                                            #Si la lista no esta vacia
        Aux_0 = sum(Lista)                                                      #Aux_0 la sumatoria de los valores de la lista
        for i in range(len(Lista)):                                             #Iteracion del largo de la lista
            Lista[i] = Lista[i] * 100 / Aux_0                                   #Porcentaje de cada elementeo de la lista con respecto a Aux_0
    
    return (Lista)                                                              #Devuelve la lista porcentualizada

def armar (Vector, Cluster):        #Funcion para armar una nueva matriz 
                                    #uniendo otras  dos
    Cluster = numpy.vstack((Cluster, Vector))  #Vector Cluster es la suma de 
                                            #los dos importados
    return Cluster                          #Devuelve la nueva Matriz

def desarmar (Vector, ClusterNum):   #Funcion para desarmar una matriz en un 
                                     #punto de Division
    a = Vector.shape[1]              #Una constante de la dimension de las 
                                     #columnas del vector
    b = []                           #Vector auxiliar 
    NewCluster = numpy.zeros((1, a))    #Crear el primer valor de un vector de 
                                     #dimensiones 1xa
    NewCluster = numpy.delete(NewCluster, 0, 0) #Eliminar la primera posicion del 
                                             #vector mantieniendo la estructura  
    for i in range(0, ClusterNum, 1):   #Desde 0 hasta el punto de division
        b.append(Vector[i])             #Crea un nuevo vector con los valores
                                        #de la fila correspondiente
        NewCluster = numpy.vstack((NewCluster, b)) #Armar una Matriz con los 
                                                #vectores obtenidos
        b = []                          #Vaciar el Vector "b"
        
    for i in range(0, ClusterNum, 1):   #Desde 0 hasta el punto de division
        Vector = numpy.delete(Vector, 0, 0)#Borrar la primera fila de la Matriz
        
    return (Vector, NewCluster)     #Devuelve el vector reducido y un nuevo 

def net():
    global Rango, Distancias_Vectoriales,Name_Fin
    G=nx.Graph()
    
    k=0
    for i in range (len(Rango)):
        for j in range(len(Rango)):
            G.add_edge(str(Rango[i]),str(Rango[j]),weight=Distancias_Vectoriales[k],group=str(k))
            k = k + 1

    h=[]
    o=[]

    for i in range(k):
        Aux_0=[(u,v) for (u,v,d) in G.edges(data=True) if d['group'] == str(i)]
        h.append(Aux_0)

    print len(h)

        
        
    pos=nx.spring_layout(G,k=10000) # positions for all nodes
    
    # nodes
    Color_0 = '#%02x%02x%02x' % (255, 69, 8)
    nx.draw_networkx_nodes(G,pos,node_size=1500,node_color=Color_0)
    
    # edges
    Distancias_Vectoriales = Escalar(Distancias_Vectoriales,5,4)
    Color_1 = '#%02x%02x%02x' % (17, 66, 170)
    Color_2 = '#%02x%02x%02x' % (0, 176, 96)
    for i in range(len(h)):
        if 5-Distancias_Vectoriales[i] <=5 and 5-Distancias_Vectoriales[i] >3.5:
            nx.draw_networkx_edges(G,pos,edgelist=h[i], edge_color=Color_1,
                                   width=5-Distancias_Vectoriales[i],style='solid')
        elif 5-Distancias_Vectoriales[i] <=3.5 and 5-Distancias_Vectoriales[i] >2:
            nx.draw_networkx_edges(G,pos,edgelist=h[i], edge_color=Color_1,
                                   width=5-Distancias_Vectoriales[i],style='dashed')
        else:
            nx.draw_networkx_edges(G,pos,edgelist=h[i], edge_color=Color_1,
                                   width=5-Distancias_Vectoriales[i],style='dotted')
#    nx.draw_networkx_edges(G,pos,edgelist=esmall,
#                        width=6,alpha=0.5,edge_color='b',style='dashed')
    
    # labels
    
    nx.draw_networkx_labels(G,pos,font_size=8,font_family='sans-serif',font_color='Black')
    
    plt.axis('off')
    plt.savefig('Graph_2' + Name_Fin + '.png', bbox_inches='tight',dpi=200)
    plt.show() # display