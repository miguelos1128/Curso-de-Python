import csv

file_path =  'products_updated.csv'
updated_file_path = 'prodcuts_updated_4.csv'

with open(file_path, mode= 'r') as file:
    csv_reader = csv.DictReader(file)
    #Obtener los nombres de las columnas existentes
    fieldnames = csv_reader.fieldnames + ['total_value2'] +['description_value2']

    with open(updated_file_path, mode = 'w', newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames = fieldnames)
        csv_writer.writeheader() #Escribir los encabezados

        for row in csv_reader:
            row['total_value2'] = float(row['price']) * int(row['quantity'])
            row['description_value2'] = row['name'] + ' de la marca ' + row['brand'] + ' Costo: $' + row['price'] +' Disponibles: ' + row ['quantity'] + ' Unidades '
            csv_writer.writerow(row)