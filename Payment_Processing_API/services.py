from datetime import datetime
from models import TransactionModel

def complete_transaction(payment_details) -> TransactionModel:
    balance = 5000
    charges = 3.5
    amount_to_debit = payment_details.amount + charges
    if amount_to_debit >= balance:
        raise ValueError("Transaction could not be completed") #pragma: no cover
    return TransactionModel(message="Transaction completed")
