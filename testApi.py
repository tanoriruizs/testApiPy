import requests as requests 

codigo = input('Ingrese el codigo del producto: ')

url = 'http://localhost/apis/productos.php?codigo='+codigo
response = requests.get(url)
print(response.json())