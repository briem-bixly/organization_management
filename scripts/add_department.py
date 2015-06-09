from api.organization_management import add_department

# NOTE: this script expects a trigger and a department name

class add_department(NebriOS):
    listens_to = ['add_department']

    def check(self):
        return self.add_department == True

    def action(self):
        self.add_department = "Ran"
        add_department(self)
