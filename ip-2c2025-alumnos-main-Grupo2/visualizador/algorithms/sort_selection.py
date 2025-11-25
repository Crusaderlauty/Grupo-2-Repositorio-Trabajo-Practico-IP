# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

def step():
   
    # - Fase "buscar": comparar j con min_idx, actualizar min_idx, avanzar j.
    #   Devolver {"a": min_idx, "b": j_actual, "swap": False, "done": False}.
    #   Al terminar el barrido, pasar a fase "swap".
    # - Fase "swap": si min_idx != i, hacer ese único swap y devolverlo.
    #   Luego avanzar i, reiniciar j=i+1 y min_idx=i, volver a "buscar".
    # Cuando i llegue al final, devolvé {"done": True}.
    global i, j, min_idx, fase,n
    if i >= n - 1:
        return {"done": True} 
          
    if fase == "buscar":  
            # Comparar j con min_idx y actualizar min_idx si es necesario
            if items[j] < items[min_idx]:
                min_idx = j    
            
            salida = {"a":min_idx, "b": j,"swap": False, "done": False}     
            j+=1
            # Terminó el barrido, pasar a fase "swap"
            if j>=n:
                fase = "swap"       
            return salida 
                       
    elif fase == "swap":
        swapped = min_idx != i
        
        if swapped:
            
            items[i], items[min_idx] = items[min_idx], items[i]
            salida = {"a":i, "b": min_idx,"swap": True, "done": False}
        else:
            salida = {"a":i, "b": min_idx,"swap": False, "done": False}   
             
        # Preparar siguiente iteración
        i += 1
        j = i + 1
        min_idx = i
        fase = "buscar"
        
        if i>=n-1:
             return {"done":True}                  
        return salida
    
    
  
#init([5,2,8,1,9])
#print("lista original",items)
#Ejecutar usando una condición en el while
#result = {"done": False}
#while result["done"] == False:
 # result = step()
  #print(result)

#print("Lista ordenada:", items)
