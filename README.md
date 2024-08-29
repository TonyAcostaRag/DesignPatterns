## Every class should have been implemented under the Single Responsibility Principle.

## Different design patterns are displayed on different key classes within the project.

Factory design pattern, implemented on /pages/factory_googleSearch/GoogleFactory.py

*> Instantiates a google page depending on the language given.*

Strategy design pattern, implemented on /pages/strategy_paymentPage/components/PaymentOption.py

*> Code decides which payment details provide on runtime depending of the payment method selected.*

Proxy design pattern, implemented on /pages/paymentProxyPage/components/OrderComponentProxy.py

*> If the configured environment is not Production, so instantiate the object which manages sensitive data.*

Execute around pattern, implemented on /pages/executeAroundPattern/Main.py

*> Encapsulates the actions for getting into a frame within a web page, execute the required actions on the frame, then 
get out from the frame. Pattern used for setting up conditions, executing actions and cleaning the environment.*

Decorator pattern, implemented on /pages/decorator/paymentPage/PaymentPromoDecorators.py

*> Provide to a specific instance separated capabilities instead of inherit from a super class. 
In the test class a decorator is applied to handle the different test cases given in the test parameters.*
