import sqlite3

class UsuarioDAO:
    def __init__(self):
        self.conexion = sqlite3.connect("BaseDeDatos.db")
    
    def AñadirUsuario(self, Nombres,Apellidos,Contrasena):
            self.conexion.execute("INSERT INTO Usuario(Nombres,Apellidos,Contrasena) VALUES (?,?,?)", (Nombres, Apellidos,Contrasena))
            self.conexion.commit()


    def ObtenerUsuarios(self):
            cursor=self.conexion.execute("SELECT * FROM Usuario")
            for fila in cursor:
                print(fila)


    def ActualizarContrasenaUsuario(self,ID_Usuario,Contrasena):
            cursor=self.conexion.execute("UPDATE Usuario SET Contrasena = ? WHERE ID_Usuario = ?",(Contrasena,ID_Usuario))

          
    def EliminarUsuario(self,ID_Usuario):
            cursor=self.conexion.execute("DELETE FROM Usuario WHERE ID_Usuario = ?",(ID_Usuario,))

        
         
         