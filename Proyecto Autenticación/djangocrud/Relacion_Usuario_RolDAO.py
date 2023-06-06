import sqlite3

class Relacion_Usuario_RolDAO:
    def __init__(self):
        self.conexion = sqlite3.connect("BaseDeDatos.db")
    
    def AñadirRol_Permiso(self,ID_Usuario,ID_Rol):
            self.conexion.execute("INSER INTO Relacion_Usuario_Rol(ID_Usuario,ID_Rol) VALUES (?,?)", (ID_Usuario,ID_Rol))
            self.conexion.commit()

    def ObtenerRol_Permiso(self):
            cursor=self.conexion.execute("SELECT ID_Usuario,ID_Rol FROM Relacion_Usuario_Rol")
            for fila in cursor:
                print(fila)
    
    def EliminarRelacion_Usuario_Rol(self,ID_Rol,ID_Usuario):
            cursor=self.conexion.execute("DELETE FROM Relacion_Usuario_Rol WHERE (ID_Rol = ?) AND (ID_Usuario = ?)",(ID_Rol,ID_Usuario))
         
         