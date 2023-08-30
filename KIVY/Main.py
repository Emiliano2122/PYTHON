from ast import Pass
from cProfile import label
from sqlite3 import sqlite_version
from tkinter import Button, Widget
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import datetime

import mysql.connector

fechaCompleta = datetime.now()
fechaCompleta = fechaCompleta.strftime("%d-%m-%Y")
print(fechaCompleta)

class Bienvenido(Screen):
    pass

class Login(Screen):
    def iniciar_sesion(self):
        miBasedeDatos = mysql.connector.connect(
            host = "192.168.64.4", 
            user = "MYPRIMERAPP",
            password = "MIPRIMERAPP",
        )
        cursorDB = miBasedeDatos.cursor()
        cursorDB.execute("MYPRIMERAPP")

        user_email = (self.ids.Ingresa_tu_usuario.text,)
        user_password = self.ids.Ingresa_tu_contraseña.text
        
        
        sql_query = ("SELECT * FROM table_users WHERE user_email = %s")
        cursorDB.execute(sql_query, user_email)
        user = cursorDB.fetchall()
        print(user[0][4])
        if (user[0][4] == user_password):
            print("contraseña correcta")
        else:
            print("contraseña incorrecta")

    pass

class Createacount(Screen):
    def crear_cuenta(self):
        try:
            miBasedeDatos = mysql.connector.connect(
                host = "192.168.64.4", 
                user = "MYPRIMERAPP",
                password = "MIPRIMERAPP",
            )
            cursorDB = miBasedeDatos.cursor()
            cursorDB.execute("MYPRIMERAPP")
            
            user_name = self.ids.Ingresa_tu_Nombre.text
            user_last_name = self.ids.Ingresa_tu_Apellido.text
            full_name = user_name + " " + user_last_name
            print(full_name)
            user_email = self.ids.Ingresa_tu_correo_electronico.text
            user_password = hash(self.ids.Ingresa_tu_contraseña.text)
            id = 2
            datos = (id, user_name, user_last_name, user_email, user_password)
            sql_query = """INSERT INTO `table_users`(`id`, `user_name`, `user_last_name`, `user_email`, `user_password`) 
                        VALUES (%s,%s,%s,%s,%s)"""
            cursorDB.execute(sql_query, datos)
            print("Se realizo el ingreso de datos")
            miBasedeDatos.commit()
            #miBasedeDatos.close()
            print("crear_cuenta")
        except mysql.connector.Error as error:
            print("Fallo en BD {}".format(error))
        
        finally:
            miBasedeDatos.close()
    pass

class BienvenidoUser(Screen):
    def guardar_orden(self):
        try:
            miBasedeDatos = mysql.connector.connect(
                host = "192.168.64.4", 
                user = "MYPRIMERAPP",
                password = "MIPRIMERAPP",
            )
            cursorDB = miBasedeDatos.cursor()
            cursorDB.execute("MYPRIMERAPP")
            
            fecha = datetime.strptime(self.ids.fecha_text.text, "%d/%m/%Y")
            tecnico_id = self.ids.tecnico_text.text
            numero_de_orden = self.ids.orden_text.text
            id_vehiculo = self.ids.vehiculo_text.text
            estado = self.ids.estado_text.text
            id_asesor = self.ids.asesor_text.text
            color1 = self.ids.color1_text.text
            feche_orden = datetime.strptime(self.ids.fecha_orden_text.text, "%d/%m/%Y")
            dato = (fecha, tecnico_id, numero_de_orden, id_vehiculo, estado, id_asesor, color1, feche_orden)

            sql_insert="INSERT INTO `ordenes`(`fecha_orden_servicio`, `id_tecnico`, `numero_de_orden`, `id_vehiculo`, `estado`, `id_asesor`, `color1`, `fecha` ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) "
            cursorDB.execute(sql_insert, dato)
        except mysql.connector.Error as error:
            print(error)
        
        finally:
            miBasedeDatos.close()
    pass

class MenuBienvenida(Screen):
    pass

class ElijeEltecnico(Screen):
    def nombre_del_tecnico(self):
        try:
            miBasedeDatos = mysql.connector.connect(
                host = "192.168.64.4", 
                user = "MYPRIMERAPP",
                password = "MIPRIMERAPP",
            )
            cursorDB = miBasedeDatos.cursor()
            cursorDB.execute("MYPRIMERAPP")

            nombre_id = self.ids.nombre_text.text
            apellido_id = self.ids.apellido_text.text
            nombrecompleto = nombre_id + " " + apellido_id
            numero_de_orden = self.ids.orden_text.text
            asesor = self.ids.asesor_text.text
            vehiculo = self.ids.vehiculo_text.text
            color1 = self.ids.color1_text.text
            tipo_de_orden = self.ids.orden_text.text
            estado = self.ids.estado_text.text
            dato = (nombrecompleto, numero_de_orden, asesor, vehiculo, color1, tipo_de_orden, estado)

            sql_insert="""INSERT INTO `nombres_mecanicos`(`nombre_mecanico`, `apellido`, `numero_de_orden`, `asesor`, `vehiculo`, `color1`, `tipo_de_orden`, `estado`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursorDB.execute(sql_insert, dato)
            miBasedeDatos.commit()
        except mysql.connector.Error as error:
            print(error)
        
        finally:
            miBasedeDatos.close()
    pass

class ElijeElnombreDelasesor(Screen):
    def nombre_del_asesor(self):
        try:
            miBasedeDatos = mysql.connector.connect(
                host = "192.168.64.4", 
                user = "MYPRIMERAPP",
                password = "MIPRIMERAPP",
            )
            cursorDB = miBasedeDatos.cursor()
            cursorDB.execute("MYPRIMERAPP")

            nombre_id = self.ids.nombre_text.text
            apellido_id = self.ids.apellido_text.text
            nombrecompleto = nombre_id + " " + apellido_id
            numero_de_orden = self.ids.orden_text.text
            cliente = self.ids.cliente_text.text
            fecha = datetime.strptime(self.ids.fecha_text.text, "%d/%m/%Y")
            piezas = self.ids.piezas_text.text
            precio = self.ids.precio_text.text
            dato = (nombrecompleto, numero_de_orden, cliente, fecha, piezas, precio)

            sql_insert="""INSERT INTO `asesores`(`nombre_asesores`, `apellido`, `numero_de_orden`, `cliente`, `fecha`, `piezas`, `precio`) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
            cursorDB.execute(sql_insert, dato)
            miBasedeDatos.commit()
        except mysql.connector.Error as error:
            print(error)
        
        finally:
            miBasedeDatos.close()
    pass

class NumeroDeOrden(Screen):
    def guardar_todos_los_numeros_de_las_ordenes(self):
        try:
            miBasedeDatos = mysql.connector.connect(
                host = "192.168.64.4", 
                user = "MYPRIMERAPP",
                password = "MIPRIMERAPP",
            )
            cursorDB = miBasedeDatos.cursor()
            cursorDB.execute("MYPRIMERAPP")

            guardar_todos_los_numeros_de_las_ordenes = self.ids.guardar_orden_text.text
            dato = (guardar_todos_los_numeros_de_las_ordenes)

            sql_insert="""INSERT INTO `numero_de_orden`(`numero_de_orden`) VALUES (%s)"""
            cursorDB.execute(sql_insert, dato)
            miBasedeDatos.commit()
        except mysql.connector.Error as error:
            print(error)
        
        finally:
            miBasedeDatos.close()
    pass

class TipoDeorden(Screen):
    def letras_de_la_orden(self):
        try:
            miBasedeDatos = mysql.connector.connect(
                host = "192.168.64.4", 
                user = "MYPRIMERAPP",
                password = "MIPRIMERAPP",
            )
            cursorDB = miBasedeDatos.cursor()
            cursorDB.execute("MYPRIMERAPP")

            letras_de_la_orden = self.ids.letras_text.text
            vehiculo = self.ids.vehiculo_text.text
            descripcion_de_la_falla = self.ids.descripcion_text.text
            dato=(letras_de_la_orden, vehiculo, descripcion_de_la_falla)

            sql_insert="""INSERT INTO `tipo_de_orden`(`tipo_de_orden`, `vehiculo`, `descripcion_de_la_falla`) VALUES (%s,%s,%s)"""
            cursorDB.execute(sql_insert, dato)
            miBasedeDatos.commit()
        except mysql.connector.Error as error:
            print(error)
        
        finally:
            miBasedeDatos.close()
    pass

class Vehiculo(Screen):
    def nombre_del_vehiculo(self):
        try:
            miBasedeDatos = mysql.connector.connect(
                host = "192.168.64.4", 
                user = "MYPRIMERAPP",
                password = "MIPRIMERAPP",
            )
            cursorDB = miBasedeDatos.cursor()
            cursorDB.execute("MYPRIMERAPP")

            nombre_vehiculo = self.ids.vehiculo_text.text
            color1 = self.ids.color1_text.text
            modelo = self.ids.modelo_text.text
            marca = self.ids.marca_text.text
            dato=(nombre_vehiculo, color1, modelo, marca)

            sql_insert="""INSERT INTO `vehiculo`(`id_niv`, `nombre_vehiculo`, `color1`, `modelo`, `marca`) VALUES (%s,%s,%s,%s,%s)"""
            cursorDB.execute(sql_insert, dato)
            miBasedeDatos.commit()
        except mysql.connector.Error as error:
            print(error)
        
        finally:
            miBasedeDatos.close()
    pass

class PiramideDelVehiculo(Screen):
    def piramide_del_vehiculo(self):
        try:
            miBasedeDatos = mysql.connector.connect(
                host = "192.168.64.4", 
                user = "MYPRIMERAPP",
                password = "MIPRIMERAPP",
            )
            cursorDB = miBasedeDatos.cursor()
            cursorDB.execute("MYPRIMERAPP")

            color_de_la_piramide = self.ids.piramide_text.text
            numero_de_la_piramide = self.ids.numero_text.text
            dato = (color_de_la_piramide, numero_de_la_piramide)

            sql_insert="""INSERT INTO `piramide_del_vehiculo`(`piramide_del_vehiculo`, `numero`) VALUES (%s,%s)"""
            cursorDB.execute(sql_insert, dato)
            miBasedeDatos.commit()
        except mysql.connector.Error as error:
            print(error)
        
        finally:
            miBasedeDatos.close()
    pass

class Color1(Screen):
    def todos_los_colores(self):
        try:
            miBasedeDatos = mysql.connector.connect(
                host = "192.168.64.4", 
                user = "MYPRIMERAPP",
                password = "MIPRIMERAPP",
            )
            cursorDB = miBasedeDatos.cursor()
            cursorDB.execute("MYPRIMERAPP")

            color1 = self.ids.color1_text.text
            codigo = self.ids.codigo_text.text
            nombre_del_color = self.ids.nombre_text.text
            dato = (color1, codigo, nombre_del_color)

            sql_insert="""INSERT INTO `color1`(`color1`, `codigo`, `nombre_del_color`, `año`) VALUES (%s,%s,%s,%s)"""
            cursorDB.execute(sql_insert, dato)
            miBasedeDatos.commit()
        except mysql.connector.Error as error:
            print(error)
        
        finally:
            miBasedeDatos.close()
    pass

class ManejadordePantalla(ScreenManager):
    pass

kv= Builder.load_file('test.kv')


class MiprimeraApp(App):
    def build(self):
        
        mydb = mysql.connector.connect(
            host ="192.168.64.4",
            user ="MYPRIMERAPP",
            password ="MIPRIMERAPP",
        
        )

        cursorDB = mydb.cursor()

        cursorDB.execute("CREATE DATABASE IF NOT EXISTS tennis_pro")
        cursorDB.execute("USE tennis_pro")
        cursorDB.execute("CREATE TABLE IF NOT EXISTS TEST (PRUEBA1 INT)")

        cursorDB.execute("CREATE DATABASE IF NOT EXISTS barcelona_bc")
        cursorDB.execute("USE barcelona_bc")
        cursorDB.execute("CREATE TABLE IF NOT EXISTS PADEL(PRUEBA2 INT)")

        cursorDB.execute("CREATE DATABASE IF NOT EXISTS formula1_f1")
        cursorDB.execute("USE formula1_f1")
        cursorDB.execute("CREATE TABLE IF NOT EXISTS AUDIFONOS (PRUEBA3 INT)")

        cursorDB.execute("CREATE DATABASE IF NOT EXISTS nombre_mecanico")
        cursorDB.execute("USE nombre_mecanico")
        cursorDB.execute("USE test")
        cursorDB.execute("""CREATE TABLE IF NOT EXISTS nombres_mecanicos(id int AUTO_INCREMENT, nombre_mecanico varchar(60),PRIMARY KEY (id))""")
        #cursorDB.execute("""SELECT * FROM table_users""")
        #cursorDB.execute("""SELECT `user_email`, `user_password` FROM `table_users` WHERE id= 1""")
        cursorDB.execute("""INSERT INTO `nombres_mecanicos`(`nombre_mecanico`) VALUES ('Alfredo')""")
        usuarios = cursorDB.fetchall()

        for usuario in usuarios:
            print(usuario)
        
        

        #cursorDB.close()





        return kv

MiprimeraApp().run()