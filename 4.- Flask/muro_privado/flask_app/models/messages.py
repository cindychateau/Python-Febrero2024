from flask_app.config.mysqlconnection import connectToMySQL

class Message:

    def __init__(self, data):
        #data = {"id": 1, "content": "Hola!", "created_at"...,  "sender_id": 1, "receiver_id": 5}
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sender_id = data['sender_id']
        self.receiver_id = data['receiver_id']

        #1 atributo extra
        self.sender_name = data['sender_name'] #Nombre que está enviando el mensaje
    
    @classmethod
    def save(cls, form):
        #form = {"content": "Hola 2", "sender_id": 1, "receiver_id": 2}
        query = "INSERT INTO messages (content, sender_id, receiver_id) VALUES (%(content)s, %(sender_id)s, %(receiver_id)s)"
        result = connectToMySQL('esquema_muroprivado').query_db(query, form)
        return result
    
    @classmethod
    def get_my_messages(cls, dicc):
        #dicc = {"id": ID del usuario en sesión}
        query = "SELECT messages.*, users.first_name as sender_name FROM messages JOIN users ON sender_id = users.id WHERE receiver_id =%(id)s "
        results = connectToMySQL('esquema_muroprivado').query_db(query, dicc) #Lista diccionarios
        messages = []
        for m in results:
            messages.append(cls(m))
        return messages
    
    @classmethod
    def delete_message(cls, form):
        #form = {"id": 1}
        query = "DELETE FROM messages WHERE id = %(id)s"
        result = connectToMySQL('esquema_muroprivado').query_db(query, form)
        return result
    
    @classmethod
    def sent_messages(cls, form):
        #form = {"id": ID del usuario en sesión}
        query = "SELECT COUNT(*) as cantidad FROM messages WHERE sender_id = %(id)s"
        result = connectToMySQL('esquema_muroprivado').query_db(query, form) #Lista con 1 registro que tiene un diccionario con la cantidad
        '''
        result = [
            {"cantidad":2}
        ]
        '''
        return result[0]['cantidad']
