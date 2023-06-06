import sqlite3

class RolDAO:
    def __init__(self):
        self.conexion = sqlite3.connect("BaseDeDatos.db")
    
    def AñadirRol(self, Nombre,Otros_atributos):
            self.conexion.execute("INSERT INTO Rol(Nombre,Otros_atributos) VALUES (?,?)", (Nombre,Otros_atributos))
            self.conexion.commit()

    def ObtenerRoles(self):
            cursor=self.conexion.execute("SELECT * FROM Rol")
            for fila in cursor:
                print(fila)
    
    def ActualizarAtributosRol(self,ID_Rol,Otros_atributos):
            cursor=self.conexion.execute("UPDATE Rol SET Otros_atributos = ? Where ID_Rol = ?",(Otros_atributos,ID_Rol))

          
    def EliminarRol(self,ID_Rol):
            cursor=self.conexion.execute("DELETE FROM Rol WHERE ID_Rol = ?",(ID_Rol,))

         
         