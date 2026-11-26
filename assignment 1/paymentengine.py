"""
Multi-Gateway Payment Processing Engine

Pick a gateway (stripe / razorpay), pick a method (card / upi),
enter the details and amount, and the program makes the payment.
Objects are created through factories, so there is no if/else chain.
""'

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    """Every payment method must know how to describe itself and how to pay."""

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass


class StripeCard(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def get_details(self):
        # Show only the last 4 digits, like real payment apps do
        return f"Stripe card ending in {self.card_number[-4:]}"

    def pay(self, amount):
        print(f"Paying Rs. {amount} using {self.get_details()}")
        print("Payment successful via Stripe (Card)")


class StripeUPI(PaymentMethod):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def get_details(self):
        return f"Stripe UPI ID {self.upi_id}"

    def pay(self, amount):
        print(f"Paying Rs. {amount} using {self.get_details()}")
        print("Payment successful via Stripe (UPI)")

class RazorpayCard(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def get_details(self):
        return f"Razorpay card ending in {self.card_number[-4:]}"

    def pay(self, amount):
        print(f"Paying Rs. {amount} using {self.get_details()}")
        print("Payment successful via Razorpay (Card)")

class RazorpayUPI(PaymentMethod):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def get_details(self):
        return f"Razorpay UPI ID {self.upi_id}"

    def pay(self, amount):
        print(f"Paying Rs. {amount} using {self.get_details()}")
        print("Payment successful via Razorpay (UPI)")

class StripeFactory:
    methods = {
        "card": StripeCard,
        "upi": StripeUPI,
    }

    def create_payment(self, method, **details):
        if method not in self.methods:
            raise ValueError(f"Stripe does not support '{method}'")
    
        return self.methods[method](**details)

class RazorpayFactory:
    methods = {
        "card": RazorpayCard,
        "upi": RazorpayUPI,
    }

    def create_payment(self, method, **details):
        if method not in self.methods:
            raise ValueError(f"Razorpay does not support '{method}'")
        return self.methods[method](**details)

class StripeAggregator:
    def __init__(self):
        self.factory = StripeFactory()

    def process(self, method, amount, **details):
        payment = self.factory.create_payment(method, **details)
        payment.pay(amount)

class RazorpayAggregator:
    def __init__(self):
        self.factory = RazorpayFactory()

    def process(self, method, amount, **details):
        payment = self.factory.create_payment(method, **details)
        payment.pay(amount)

class AggregatorFactory:
    
    factory = {
        "stripe": StripeAggregator,
        "razorpay": RazorpayAggregator,
    }

    @classmethod
    def get_aggregator(cls, gateway):
        if gateway not in cls.factory:
            raise ValueError(f"Unknown gateway '{gateway}'. Choose: {', '.join(cls.factory)}")
        return cls.factory[gateway]()

DETAIL_PROMPTS = {
    "card": ("card_number", "Enter 16-digit card number: "),
    "upi": ("upi_id", "Enter UPI ID (e.g. name@bank): "),
}

def main():
    print("=== Multi-Gateway Payment Engine ===")

    try:
        gateway = input("Choose gateway (stripe / razorpay): ").strip().lower()
        method = input("Choose payment method (card / upi): ").strip().lower()

        if method not in DETAIL_PROMPTS:
            raise ValueError(f"Unknown payment method '{method}'. Choose: card, upi")

        field_name, prompt = DETAIL_PROMPTS[method]
        detail_value = input(prompt).strip()
        amount = float(input("Enter amount: "))

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        aggregator = AggregatorFactory.get_aggregator(gateway)
        
        aggregator.process(method, amount, **{field_name: detail_value})

    except ValueError as error:
        print(f"Error: {error}")
    except Exception as error:
        print(f"Something went wrong: {error}")

if __name__ == "__main__":
    main()