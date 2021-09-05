import pandas as pd
import plotly.graph_objects as go

url = 'https://raw.githubusercontent.com/RoTorresT/dolar/main/r/r.json'
df = pd.read_json(url)

def extraer_fila(j):

    a = list(df.iloc[j])    #ingreso a columnas
    
    compra = []             #listas vacias
    venta = []              #listas vacias


    for i in range(len(a)): #cada elemento columna

        try:
            #print(a[i])
            aux1 = a[i]['compra']   #por elemento compra
            aux2 = a[i]['venta']    #por elemento venta

            if aux1 == 0:
                compra.append(compra[-1])
            else:
                compra.append(aux1)
                

            if aux2 == 0:
                venta.append(venta[-1])
            else:
                venta.append(aux2)

        except:
            compra.append(compra[-1])
            venta.append(venta[-1])

    return [compra, venta]

def grafico_venta(df):

    fig = go.Figure()

    index = list(df.index)

    for i in range(0,14):
        
        r = extraer_fila(i) 
       
        fig.add_trace(go.Scatter(

            y=r[1],
            mode='lines',
            name=index[i],
            ))
        
    fig.write_html("venta.html")

    #fig.show() #time

def grafico_compra(df):

    fig = go.Figure()

    index = list(df.index)

    for i in range(0,14):
        
        r = extraer_fila(i)
       
        fig.add_trace(go.Scatter(
            y=r[0],
            mode='lines',
            name=index[i],
            ))
        
    fig.write_html("compra.html")   

grafico_compra(df)
grafico_venta(df)