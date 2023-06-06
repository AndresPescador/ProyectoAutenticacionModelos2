import sqlite3

class PermisoDAO:
    def __init__(self):
        self.conexion = sqlite3.connect("BaseDeDatos.db")
    
    def AñadirPermiso(self,Descripcion):
            self.conexion.execute("INSERT INTO Permiso (Descripcion) VALUES (?)", (Descripcion,))
            self.conexion.commit()

    def ObtenerPermisos(self):
            cursor=self.conexion.execute("SELECT ID_Permiso,Descripcion FROM Permiso")
            for fila in cursor:
                print(fila)
    
    def ActualizarDescripcion(self,ID_Permiso,Descripcion):
            cursor=self.conexion.execute("UPDATE Permiso SET Descripcion = ? Where ID_Permiso = ?",(Descripcion,ID_Permiso))

          
    def EliminarPermiso(self,ID_Permiso):
            cursor=self.conexion.execute("DELETE FROM Permiso WHERE ID_Permiso = ?",(ID_Permiso,))
         
         