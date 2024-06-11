class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.allowed_contract_types = []

    def add_contract_type_permission(self, contract_type):
        if contract_type not in self.allowed_contract_types:
            self.allowed_contract_types.append(contract_type)

    def remove_contract_type_permission(self, contract_type):
        if contract_type in self.allowed_contract_types:
            self.allowed_contract_types.remove(contract_type)

    def can_view_contract(self, contract_type):
        return contract_type in self.allowed_contract_types


class Admin:
    def __init__(self, admin_id, username):
        self.admin_id = admin_id
        self.username = username

    def set_user_permissions(self, user, contract_types):
        user.allowed_contract_types = contract_types

    def add_permission(self, user, contract_type):
        user.add_contract_type_permission(contract_type)

    def remove_permission(self, user, contract_type):
        user.remove_contract_type_permission(contract_type)
