#Programa que redirige a un buscador
#Creado por @neriphy

import webbrowser

print("¿Que buscador desea usar?")
buscador = input()

if buscador == "google":
    buscar = input("Introduce lo que quieres buscar: ")
    webbrowser.open("https://www.google.com.mx/search?q="+buscar+"&oq=go&aqs=chrome..69i57j69i60l4j35i39.2719j0j4&sourceid=chrome&ie=UTF-8")

if buscador == "duckduckgo":
    buscar = input("Introduce lo que quieres buscar: ")
    webbrowser.open("https://duckduckgo.com/?q="+buscar+"&t=h_&ia=web")

if buscador == "bing":
    buscar = input("Introduce lo que quieres buscar: ")
    webbrowser.open("https://www.bing.com/search?q="+buscar+"&qs=n&form=QBLH&sp=-1&ghc=1&pq=google&sc=8-6&sk=&cvid=C78CC4585DA247A6B10DBA2E29FB9BD9")

else:
    buscar = input("Introduce lo que quieres buscar: ")
    webbrowser.open("https://duckduckgo.com/?q="+buscar+"&t=h_&ia=web")
