from datetime import date
from datetime import datetime
import os
import os.path as path
from datetime import timedelta

def fechaParaPC(fecha):
# 2021-04-23  -> 23-04-2021

    anio = fecha[0:4]
    mes = fecha[5:7]
    dia = fecha[8:10]
    
    nueva = dia + "-" + mes + "-" + anio
    return(nueva)



file = open("sample.xml", "w")
file.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>")
file.write("\n")
file.write("<data-set xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\">")
file.write("\n")
file.write("\t\t")
file.write("<record>")
file.write("\n")
file.write("\t\t")
file.write("<LastName>Smith</LastName>")
file.write("\n")
file.write("\t\t")
file.write("<Sales>16753</Sales>")
file.write("\n")
file.write("\t\t")
file.write("<Country>UK</Country>")
file.write("\n")
file.write("\t\t")
file.write("<Quarter>Qtr 3</Quarter>")
file.write("\n")
file.write("\t")
file.write("</record>")
file.write("\n")
file.write("</data-set>")
file.close()


dia = date.today()

vendedores = ["Carlos", "Salvador", "Alfonso", "Cynthia", "Karla", "Genaro", "Oscar",  "Héctor", "Demian", "Liliana"]
proyectos = ["Unico Coyoacan", "Park Andalucia", "Icon Roma", "Casa Roma 315", "Icon Condesa", "Park Del Carmen", "Casa Roma 127", "Unico Roma"]

mon = ["Cynthia", "Héctor"]
tue = ["Alfonso", "Oscar"]
wed = ["Salvador", "Genardo"]
thu = ["Carlos", "Karla"]
fri = ["Liliana", "Demian"]
sat = ["Héctor", "Cynthia"]
sun = ["Oscar", "Alfonso"]

numVendedores = len(vendedores)
numProyectos = len(proyectos)

limite = 100
inicia = 1

contaVendedores = 0
contaProyectos = 0

print("Mis vendedores son: ", numVendedores)
print("Mis proyectos son: ", numProyectos)


file = open("RoldeGuardia.xml", "w")
file.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>")
file.write("\n")
file.write("<data-set xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\">")
file.write("\n")

while inicia <= limite:
    
    nueva = fechaParaPC(str(dia))
    
    file.write("\t")
    file.write("<record>")
    file.write("\n")
    file.write("\t\t")
    file.write("<Dia>"+dia.strftime("%a")+"</Dia>")
    file.write("\n")
    file.write("\t\t")
    file.write("<Fecha>"+nueva+"</Fecha>")
    file.write("\n")
    file.write("\t\t")
    file.write("<Vendedor>"+vendedores[contaVendedores]+"</Vendedor>")
    file.write("\n")
    file.write("\t\t")
    file.write("<Proyectos>"+proyectos[contaProyectos]+"</Proyectos>")
    file.write("\n")
    file.write("\t")
    file.write("</record>")
    file.write("\n")
    
    contaVendedores = contaVendedores + 1
    if contaVendedores == numVendedores:
        contaVendedores = 0
        
    contaProyectos = contaProyectos + 1
    if contaProyectos == numProyectos:
        contaProyectos = 0
        dia = dia + timedelta(days = 1)
        
    inicia = inicia + 1


file.write("</data-set>")
file.close()

file = open("RoldeGuardia.xsd", "w")
file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
file.write("\n")
file.write("<xs:schema xmlns:xs=\"http://www.w3.org/2001/XMLSchema\">")
file.write("\n")
file.write("<xs:element name=\"record\">")
file.write("\n")
file.write("\t")
file.write("<xs:complexType>")
file.write("\n")
file.write("\t\t")
file.write("<xs:sequence>")
file.write("\n")
file.write("\t\t\t")
file.write("<xs:element name=\"Fecha\" type=\"xs:string\" />")
file.write("\n")
file.write("\t\t\t")
file.write("<xs:element name=\"Dia\" type=\"xs:string\" />")
file.write("\n")
file.write("\t\t\t")
file.write("<xs:element name=\"Vendedor\" type=\"xs:string\" />")
file.write("\n")
file.write("\t\t\t")
file.write("<xs:element name=\"Proyectos\" type=\"xs:string\" />")
file.write("\n")
file.write("\t\t")
file.write("</xs:sequence>")
file.write("\n")
file.write("\t")
file.write("</xs:complexType>")
file.write("\n")
file.write("</xs:element>")
file.write("\n")
file.write("</xs:schema>")
file.close()






