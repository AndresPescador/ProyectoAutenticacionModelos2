import sqlite3

class Relacion_Rol_PermisoDAO:
    def __init__(self):
        self.conexion = sqlite3.connect("BaseDeDatos.db")
    
    def AñadirRol_Permiso(self,ID_Rol,ID_Permiso):
            self.conexion.execute("INSERT INTO Relacion_Rol_Permiso(ID_Rol,ID_Permiso) VALUES (?,?)", (ID_Rol,ID_Permiso))
            self.conexion.commit() 

    def ObtenerRol_Permiso(self):
            cursor=self.conexion.execute("SELECT ID_Rol,ID_Permiso FROM Relacion_Rol_Permiso")
            for fila in cursor:
                print(fila)
          
    def EliminarRelacion_Rol_Permiso(self,ID_Rol,ID_Permiso):
            cursor=self.conexion.execute("DELETE FROM Relacion_Rol_Permiso Where (ID_Rol = ?) AND (ID_Permiso = ?)",(ID_Rol,ID_Permiso))