class Decorators:

    def __init__(self, dashboard_page):
        self._dashboard = dashboard_page

    def _should_display(self, elements):
        for element in elements:
            assert element.is_displayed() == True

    def _should_not_display(self, elements):
        for element in elements:
            assert element.is_displayed() == False

    def admin_components_presence(self):
        self._should_display(self._dashboard.get_list_admin())
        return self

    def admin_components_not_presence(self):
        self._should_not_display(self._dashboard.get_list_admin())
        return self

    def su_components_presence(self):
        self._should_display(self._dashboard.get_list_superuser())
        return self

    def su_components_not_presence(self):
        self._should_not_display(self._dashboard.get_list_superuser())
        return self

    def guest_components_presence(self):
        self._should_display(self._dashboard.get_list_guest())
        return self

    def guest_components_not_presence(self):
        self._should_not_display(self._dashboard.get_list_guest())
        return self

    def admin_selection(self):
        self._dashboard.selectRole('admin')
        return self

    def su_selection(self):
        self._dashboard.selectRole('superuser')
        return self

    def guest_selection(self):
        self._dashboard.selectRole('guest')
        return self

    def guest_page(self):
        (((self.guest_selection()
           .guest_components_presence())
          .su_components_not_presence())
         .admin_components_not_presence())
        return True

    def su_page(self):
        (((self.su_selection()
           .guest_components_presence())
          .su_components_presence())
         .admin_components_not_presence())
        return True

    def admin_page(self):
        (((self.admin_selection()
           .guest_components_presence())
          .su_components_presence())
         .admin_components_presence())
        return True

    def get_validation_role(self, role):

        roles_validation = {
            'guest': self.guest_page,
            'superuser': self.su_page,
            'admin': self.admin_page
        }
        return roles_validation[role]()
