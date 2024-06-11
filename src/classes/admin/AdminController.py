from src.classes.admin import User, Admin

class AdminController:
    def __init__(self):
        self.users = {}
        self.admins = {}

    def add_user(self, user_id, username):
        if user_id not in self.users:
            self.users[user_id] = User(user_id, username)

    def add_admin(self, admin_id, username):
        if admin_id not in self.admins:
            self.admins[admin_id] = Admin(admin_id, username)

    def set_user_permissions(self, admin_id, user_id, contract_types):
        if admin_id in self.admins and user_id in self.users:
            admin = self.admins[admin_id]
            user = self.users[user_id]
            admin.set_user_permissions(user, contract_types)

    def add_permission(self, admin_id, user_id, contract_type):
        if admin_id in self.admins and user_id in self.users:
            admin = self.admins[admin_id]
            user = self.users[user_id]
            admin.add_permission(user, contract_type)

    def remove_permission(self, admin_id, user_id, contract_type):
        if admin_id in self.admins and user_id in self.users:
            admin = self.admins[admin_id]
            user = self.users[user_id]
            admin.remove_permission(user, contract_type)

    def can_user_view_contract(self, user_id, contract_type):
        if user_id in self.users:
            user = self.users[user_id]
            return user.can_view_contract(contract_type)
        return False

# Exemplo de uso
if __name__ == "__main__":
    controller = AdminController()

    # Adicionando admin e usuário
    controller.add_admin(1, "admin1")
    controller.add_user(1, "user1")

    # Definindo permissões
    controller.set_user_permissions(1, 1, ["contract_type_1", "contract_type_2"])

    # Adicionando uma nova permissão
    controller.add_permission(1, 1, "contract_type_3")

    # Removendo uma permissão
    controller.remove_permission(1, 1, "contract_type_1")

    # Verificando permissões
    print(controller.can_user_view_contract(1, "contract_type_1"))  # False
    print(controller.can_user_view_contract(1, "contract_type_2"))  # True
    print(controller.can_user_view_contract(1, "contract_type_3"))  # True
