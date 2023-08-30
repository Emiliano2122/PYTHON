import datetime
import os
import sys
hashseed = os.getenv('PYTHONHASHSEED')
if not hashseed:
    os.environ['PYTHONHASHSEED'] = '0'
    os.execv(sys.executable,[sys.executable]+sys.argv)
from cgitb import text
from unicodedata import name
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem


import mysql.connector

class Login_screen(Screen):
    def iniciar_sesion(self):
        miBasedeDatos = mysql.connector.connect(
            host = "192.168.64.4", 
            user = "MYPRIMERAPP",
            password = "MIPRIMERAPP",
        )
        cursorDB = miBasedeDatos.cursor()
        cursorDB.execute("MYPRIMERAPP")

        user_email = (self.ids.user.text,)
        user_password = self.ids.password.text
        
        
        sql_query = ("SELECT * FROM table_users WHERE user_email = %s")
        cursorDB.execute(sql_query, user_email)
        user = cursorDB.fetchall()
        #print(user[0][2])
        #if (user[0][2] == user_password):
            #print("contraseña correcta")
        #else:
            #print("contraseña incorrecta")
        print(type(user[0][4]))
        hashpassword =str(hash(self.ids.password.text))
        print(type(hashpassword))
        if user[0][4]==hashpassword:
            self.manager.current = "Welcome_screen"
        else:
            print("Error contraseña incorrecta")

    pass

class Welcome_screen(Screen):
    pass

class Create_account(Screen):
    def crear_cuenta(self):
        try:
            miBasedeDatos = mysql.connector.connect(
                host = "192.168.64.4", 
                user = "MYPRIMERAPP",
                password = "MIPRIMERAPP",
            )
            cursorDB = miBasedeDatos.cursor()
            cursorDB.execute("MYPRIMERAPP")
            
            user_name = self.ids.user.text
            last_name = self.ids.last_name.text
            user_email = self.ids.correo_electronico.text
            user_password = hash(self.ids.password.text)
            id = 2
            datos = (id, user_name, last_name, user_email, user_password)
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

class ElijeEltecnico(Screen):
    #def on_start(self):
        #for i in range(20):
            #self.root.ids.container.add_widget(
                #OneLineListItem(text=f"Single-line item {i}")
            #)
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
     #def on_start(self):
        #for i in range(20):
            #self.root.ids.container.add_widget(
                #OneLineListItem(text=f"Single-line item {i}")
            #)
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

sm = ScreenManager()
sm.add_widget(Login_screen(name="Login"))
sm.add_widget(Welcome_screen(name="Welcome"))
sm.add_widget(Create_account(name="Create_account"))

class MainApp(MDApp):

    def build(self):
        return Builder.load_file('kivyMD.kv')

        
MainApp().run()
