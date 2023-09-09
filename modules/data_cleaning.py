import math
import datetime
import pandas as pd
def clean_data(df_raw):
    
    """# Limpieza de dataset"""

    useless_col =[0,1,2,3,4,5,6,10,16,18,23,27,30,35,37,38,39,44,45,46,47,48,50,54,55,56,57,58,61,62,63,64,65,66,67,68]
    target_col = [52]
    df_raw.drop(columns=df_raw.columns[useless_col], inplace=True)

    df_raw.columns

    """Cleaning TC timing"""

    df_raw.info()

    numeros = df_raw.iloc[:, 27].values


    def convertir_a_minutos(tiempo):
        if '.' in tiempo and tiempo.endswith(':00'):
            formato = '%H:%M:%S.%f'
        else:
            formato = '%H:%M:%S'

        # Dividir los componentes de la cadena de tiempo
        componentes = tiempo.split(':')
        horas = int(componentes[0])
        minutos = int(componentes[1])
        segundos = int(componentes[2]) if len(componentes) > 2 else 0

        # Manejar horas que exceden el rango permitido
        horas %= 24

        # Crear un objeto datetime con los componentes divididos
        tiempo_dt = datetime.time(horas, minutos, segundos)

        # Calcular el tiempo total en minutos
        tiempo_total_segundos = tiempo_dt.hour * 3600 + tiempo_dt.minute * 60 + tiempo_dt.second + tiempo_dt.microsecond / 1e6
        tiempo_total_minutos = tiempo_total_segundos / 60

        return tiempo_total_minutos

    rnd_time = []
    for i in [19,50,150,500,800,900]:
        valor = df_raw.iloc[i, 27]
        rnd_time.append(valor)



    numeros_convertidos = []
    for numero in numeros:
        if isinstance(numero, str) and (':' in numero):
            numero_convertido = convertir_a_minutos(numero)
            numeros_convertidos.append(numero_convertido)
        else:
            numeros_convertidos.append(numero)


    def convertir_a_entero(valor):
        if valor == 'NaN':
            return None
        else:
            try:
                return int(float(valor))
            except (ValueError, TypeError):
                return None

    numeros_convertidos = [convertir_a_entero(x) for x in numeros_convertidos]

    df_raw.iloc[:,27]=numeros_convertidos

    rnd_time = []
    for i in [19,50,150,500,800,900]:
        valor = df_raw.iloc[i, 27]
        rnd_time.append(valor)

    rnd_time

    df_raw.shape

    df_raw.iloc[987, 27]

    df_raw.iloc[:,19].unique()

    df_raw.iloc[:,19].replace(to_replace="128 weeks", value=128, inplace=True)
    df_raw.iloc[:,19].replace(to_replace="64 weeks", value=64, inplace=True)
    df_raw.iloc[:,19].replace(to_replace="32 weeks", value=32, inplace=True)
    df_raw.iloc[:,19].replace(to_replace="16,8,4 weeks", value=16, inplace=True)
    df_raw.iloc[:,19].replace(to_replace="Not recommended", value=0, inplace=True)

    rangos = [0, 30, 40, 50, 60, 90, 150, 5000]
    etiquetas = ['Less30','30-40', '40-50', '50-60', '60-90', '-90-150', 'More150']

    df_raw.iloc[:,27] = pd.cut(df_raw.iloc[:, 27], bins=rangos, labels=etiquetas, right=False)

    df_raw.iloc[:,27].unique()

    df_raw.dropna(inplace = True)

    df_raw = df_raw[~((df_raw.iloc[:,27] == 'Less30') | (df_raw.iloc[:,27] == 'More150'))]


    df_raw.iloc[:,15].unique()

    df_raw.iloc[:,29].replace(to_replace="Yes", value=1, inplace=True) # Did the parent pay in the TC?
    df_raw.iloc[:,29].replace(to_replace="No", value=0, inplace=True)

    df_raw.iloc[:,30].replace(to_replace="Yes", value=1, inplace=True) #'Did the manager offer the discount?'
    df_raw.iloc[:,30].replace(to_replace="No", value=0, inplace=True)

    df_raw.iloc[:,31].replace(to_replace="Yes", value=1, inplace=True) #'The parent was present throughout the lesson?'
    df_raw.iloc[:,31].replace(to_replace="Partially", value=0, inplace=True)

    #the manager suggested groups from the available ones that are in the set (not which one is convenient for you)
    df_raw.iloc[:,22].replace(to_replace="Yes", value=1, inplace=True)
    df_raw.iloc[:,22].replace(to_replace="No", value=0, inplace=True)

    df_raw.iloc[:,15].replace(to_replace="5%", value=1, inplace=True)  #Start date
    df_raw.iloc[:,15].replace(to_replace="-5%", value=0, inplace=True)


    cols_obj = [0,1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,20,21,23,24,25,26]

    df_raw.iloc[:, cols_obj] = df_raw.iloc[:, cols_obj].replace('%', '', regex=True).astype(float)

    df_raw.iloc[:,8].replace(to_replace="Python", value=1, inplace=True)  # Which course the client came to
    df_raw.iloc[:,8].replace(to_replace="Scratch", value=1, inplace=True)
    df_raw.iloc[:,8].replace(to_replace="FWD", value=1, inplace=True)
    df_raw.iloc[:,8].replace(to_replace="Roblox", value=1, inplace=True)
    df_raw.iloc[:,8].replace(to_replace="Yes", value=1, inplace=True)
    df_raw.iloc[:,8].replace(to_replace="No", value=0, inplace=True)

    df_raw['How old is the child?'].unique()

    cols_dum = [27,32]

    df_raw['TC timing ']

    valores_no_deseados = ["didn't asked during the tc", "older than 11 but I am not sure", "No info"]
    df_raw = df_raw[~df_raw.iloc[:,28].isin(valores_no_deseados)] #'How old is the child?

    df_raw.iloc[:,27] = df_raw.iloc[:,27].astype(str) #TC Timing

    df_raw.columns[cols_dum]

    df_raw = pd.get_dummies(df_raw, columns = df_raw.columns[cols_dum])

    return df
