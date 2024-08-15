from pages.paymentProxyPage.components.Order import Order


class OrderComponentProxy:

    excluded_environments = ['PROD', 'STAGE']

    def __init__(self, service, driver=None):

        '''
         This line should read the value set in the test class
         current_env = 'env'
         For the time being using default as QA.
        '''
        current_env = 'QA'

        if current_env not in self.excluded_environments:
            self.order = Order(service, driver)
        else:
            self.order = None


    def placeOrder(self):
        if self.order is not None:
            return self.order.placeOrder()
        else:
            return 'Skipped'
