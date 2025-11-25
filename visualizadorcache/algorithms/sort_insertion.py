# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0      # elemento que queremos insertar
j = None   # cursor de desplazamiento hacia la izquierda (None = empezar)

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1      # común: arrancar en el segundo elemento
    j = None

def step():
    
    # - Si i >= n: devolver {"done": True}.
    # - Si j es None: empezar desplazamiento para el items[i] (p.ej., j = i) y devolver un highlight sin swap.
    # - Mientras j > 0 y items[j-1] > items[j]: hacer UN swap adyacente (j-1, j) y devolverlo con swap=True.
    # - Si ya no hay que desplazar: avanzar i y setear j=None.
  global i,j         
  if i >= n: 
        return {"done": True} #Chequea si ya se paso por todos los elementos de la lista, i >= n singifica que se termino de ordenar en len(items), 
                             #ej: n = 3 y i = 3 significa que se completo todos los elementos y como no quedan restantes termina ahi

  if j == None:  #Verifica si todavia no se comenzo, si es asi, comienza el desplazamiento de los items
        j = i       #asignamos a j como i, ya que nos fijamos en items[i]
        return {"a": j-1, "b": j, "swap": False, "done": False} # highlight de que aca no se hizo swap int(a) = j-1 int(b) = j {"a": int, "b": int, "swap": bool, "done": bool}
    

  if j > 0 and items[j-1] > items[j]:             #Si j > 0 y items[j-1] > items[j] hacemos un swap adyacente 
        items[j], items[j-1] = items[j-1], items[j] #swap de items j y items j-1
        j -= 1                                      #movemos el j a la izquierda 
        return {"a": j, "b": j+1, "swap": True, "done": False} #lo devolvemos como swap = True, y done = False por que todavia no termino
    #como ya vimos la parte de la izquierda, avanzamos a la derecha determinando "a": como j y "b": como j+1
    

                                     #Si ya no hay que desplazar
  i += 1   #avanzar i
  j = None  #setear j en none
  return {"a": i-1,"b": i, "swap": False,"done": False}
 
