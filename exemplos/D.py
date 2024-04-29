class PaymentProcessor:
    def process_payment(self, payment_provider):
        return payment_provider.process()

class PaymentProvider:
    def process(self):
        pass

class CreditCardPaymentProvider(PaymentProvider):
    def process(self):
        return "Processing credit card payment"

class PayPalPaymentProvider(PaymentProvider):
    def process(self):
        return "Processing PayPal payment"

# Exemplo de uso
payment_processor = PaymentProcessor()
credit_card_provider = CreditCardPaymentProvider()
paypal_provider = PayPalPaymentProvider()

print(payment_processor.process_payment(credit_card_provider))
print(payment_processor.process_payment(paypal_provider))
