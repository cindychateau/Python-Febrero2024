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
        self.sender_name = data['sender_name']
    
    @classmethod
    def save(cls, form):
        #form = {"content": "Hola 2", "sender_id": 1, "receiver_id": 2}
        query = "INSERT INTO messages (content, sender_id, receiver_id) VALUES (%(content)s, %(sender_id)s, %(receiver_id)s)"
        result = connectToMySQL('esquema_muroprivado').query_db(query, form)
        return result