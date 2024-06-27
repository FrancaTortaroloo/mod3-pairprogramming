
#Creamos la función para explorar los datos. 

def exploracion_datos(df):
    print('_____________ INFORMACIÓN GENERAL DEL DATAFRAME ____________\n')
    print(df.info())

    print('___________________ FORMA DEL DATAFRAME ____________________\n')
    
    print(f"El número de filas que tenemos es de {df.shape[0]}.\nEl número de columnas es de {df.shape[1]}\n")
    

    print('_______________ NULOS, ÚNICOS Y DUPLICADOS _________________\n')
    
    print('La cantidad de valores NULOS por columna es de:\n')
    print(df.isnull().sum())
    print('____________________________________________________________\n')

    print('La cantidad de valores ÚNICOS por columna es de:\n')
        
    for columna in df.columns:
        cantidad_valores_unicos = len(df[columna].unique())
    
        print(f'La columna {columna}: {cantidad_valores_unicos}')

    """ Otra forma más rápida de obtener la lista de valores únicos por columna es usando df.nunique()"""

    print('____________________________________________________________\n')

    print('La cantidad de valores DUPLICADOS por columna es de:\n')

    """En análisis posteriores hemos detectado que hay columnas con valores duplicados que nos interesa filtrar, 
    así que vamos a realizar otro bucle for para iterar por todas las columnas del DF y obtener los duplicados de cada una de ellas."""

    for columna in df.columns:
        cantidad_duplicados = df[columna].duplicated().sum()
    
        print(f'La columna {columna}: {cantidad_duplicados}')


    print('____________________ RESUMEN ESTADÍSTICO ____________________')
    print('____________________ Variables Numéricas __________________\n')
    print(df.describe().T)
    
    print('___________________ Variables Categóricas _________________\n')
    print(df.describe(include='object').T)
    
    
    
#  ver duplicados en las columnas
    
def ver_duplicados(df, columna):
     duplicated_rows = df.loc[clientes_df.duplicated(subset=[columna], keep=False)]
     return duplicated_rows
 
 
 #funcion para convertir a minuscula
def pasar_minuscula(df):
# vamos a iterar por todas las columnas del DataFrame y a cada una de ellas la pondremos en minúsula y le aplicaremos un replace para quitar los puntos. 
    nuevas_columnas = {columna: columna.lower() for columna in df.columns}
# comprobamos que hemos creado el diccionario correctamente
    return nuevas_columnas

# conteo de nulos coolumnas categoricas
def conteo_columnas_cat(df):
    nulos_esta_cat = df[df.columns[df.isnull().any()]].select_dtypes(include = "O").columns
    return f"Las columnas categóricas que tienen nulos son : {nulos_esta_cat}"



#reemplazar nulos por moda en UNA SOLA COLUMNA

def reemplazar_nulos_por_moda(df, columna_categorica):

# Ejemplo de carga de un DataFrame
# df = pd.read_csv('tus_datos.csv')  # Si estás cargando datos desde un archivo CSV
# Para este ejemplo, crearé un DataFrame de muestra
# Calcula la moda de la columna
    moda = df[columna_categorica].mode()[0]

# Reemplaza los valores nulos por la moda
    df[columna_categorica].fillna(moda, inplace=True)

#verificar que no haya nulos
    conteo_nulos = df[columna_categorica].isnull().sum()
    
# Muestra el DataFrame actualizado
    return f'Hay {conteo_nulos} nulos'


# reemplazar columnas categoricas por unknown

def reemplazar_unknown(columnas, df):
    #recorremos las columnas
    for columna in columnas_desconocido:
    # reemplazamos los nulos por el valor Unknown para cada una de las columnas de la lista
        df[columna] = df[columna].fillna("Unknown")
    
    # comprobamos si quedan nulos en las columnas categóricas. 
    print("Después del reemplazo usando 'fillna' quedan los siguientes nulos")
    print(df[columnas_desconocido].isnull().sum())