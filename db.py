from mysql.connector import connection

class Banco:
    def __init__(self):
        self.conexao = connection.MySQLConnection(host='localhost', user='root', password='', database='db')
        
    
    def getConexao(self):
        return self.conexao

    def setConexao(self, conexao):
        self.conexao = conexao

    def cadastrar(self, sql, valores):
        cursor = self.conexao.cursor()
        cursor.execute(sql, valores)
        print("Salvo com sucesso")
    
    def consultar(self, sql, valores):
        cursor = self.conexao.cursor()
        cursor.execute(sql, valores)
        resultado = cursor.fetchall()
        return resultado
    
    def consutarAll(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM dados")
        cursor.fetchall()
        return cursor
