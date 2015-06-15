from api.organization_management import add_department

# NOTE: this script expects a trigger and a department name

class add_dept(NebriOS):
    listens_to = ['add_dept']

    def check(self):
        return self.add_dept == True

    def action(self):
        self.add_dept = "Ran"
        add_department(self)
