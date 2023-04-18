# obtener la hora de entrada y salida en formato de 24 horas y el valor por hora

hora_entrada = input("Ingrese la hora de entrada (formato HH:MM): ")
hora_salida = input("Ingrese la hora de salida (formato HH:MM): ")
valor_hora = int(input("Ingrese el valor hora: "))

# convertir la hora de entrada y slaida en minutos
entrada_minutos = int(hora_entrada[:2]) * 60 + int(hora_entrada[3:])
salida_minutos = int(hora_salida[:2]) * 60 + int(hora_salida[3:])

# calcular las horas trabajadas
total_minutos = salida_minutos - entrada_minutos
horas_trabajadas = total_minutos // 60
minutos_trabajados = total_minutos % 60


# imprimir las horas trabajadas
print(
    f'El empleado trabajo {horas_trabajadas} horas y {minutos_trabajados} minutos.')

# imprimir el importe a cobrar
importe_cobrar = horas_trabajadas * valor_hora
print(f'Debe cobrar ${importe_cobrar}')
