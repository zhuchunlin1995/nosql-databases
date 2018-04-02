import urllib.request as request
url = 'https://api.nasa.gov/planetary/apod?api_key=o71eOeRUuccZPqz5hvmRV1vLN5tE9SdIuH0Vl1Cc&date=2017-09-20'
content = request.urlopen(url).read()
array = content.splitlines()
res = array[len(array) - 2]
print(res[10:len(res) - 1].decode('utf-8'))
