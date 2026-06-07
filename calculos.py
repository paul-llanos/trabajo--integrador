def calculo_cuello_de_botella(cpu_usada, ram_usada):
    if cpu_usada > ram_usada:
        cuello_de_botella = cpu_usada - ram_usada
        return cuello_de_botella
    else:
        cuello_de_botella = ram_usada - cpu_usada
        return cuello_de_botella