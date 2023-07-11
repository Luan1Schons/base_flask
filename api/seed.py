import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import create_app, db
from app.models.user_status import UserStatus
from app.models.user import User

class StatusSeed:
    @staticmethod
    def seed():
        app = create_app()
        with app.app_context():
            status1 = UserStatus(description="Ativo")
            status2 = UserStatus(description="Inativo")
            status3 = UserStatus(description="Bloqueado")
            status4 = UserStatus(description="Pendente")

            db.session.add(status1)
            db.session.add(status2)
            db.session.add(status3)
            db.session.add(status4)
            db.session.commit()

            print('Status criados no banco de dados...')

class UsersSeed:
    @staticmethod
    def seed():
        app = create_app()
        with app.app_context():
            user1 = User(username="Admin", email="admin@example.com", password="secret")
            user2 = User(username="Luan", email="luan@example.com", password="secret")
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()

            print('Usuário criado no banco de dados...')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        seed_choice = sys.argv[1]
        seed_class = globals().get(seed_choice.capitalize() + 'Seed')
        if seed_class:
            seed_class.seed()
        else:
            print('Seed inválida.')
    else:
        print('Nenhuma escolha de seed fornecida.')
