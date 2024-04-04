from pydantic import BaseModel, Field, field_validator
from pydantic_extra_types.payment import PaymentCardBrand, PaymentCardNumber
from datetime import date, datetime


class CardInfo(BaseModel):
    name_on_card: str = Field(
        title="Name on Card",
        description="Name on the card",
        examples=["Fortune Okolo"],
        min_length=3,
        max_length=50,
        pattern=r"^[a-zA-Z\s]+$"
    )
    card_no: PaymentCardNumber = Field(
        title="Card Number",
        description="Card number",
        examples=["4000122356789010"],
        min_length=16,
        max_length=16,
    )
    cvv: str = Field(
        title="CVV", description="CVV", examples=["123"], min_length=3, max_length=4
    )
    expiry_date: str = Field(
        title="Expiry Date",
        description="Expiry date of the card",
        examples=["11/24"],
        pattern="^[0-9]{2}/[0-9]{2}$",
    )

    @field_validator("card_no")
    def validate_card_brand(cls, value):
        if value.brand not in [PaymentCardBrand.visa, PaymentCardBrand.mastercard, PaymentCardBrand.verve, PaymentCardBrand.amex]:
            raise ValueError("Only Visa, MasterCard or verve cards are accepted") #pragma: no cover
        return value

    @field_validator("expiry_date")
    def validate_expiry_date(cls, value):
        mm, yy = value.split("/")
        expiration_date = date(int("20" + yy), int(mm), 1)
        current_date = date.today()
        if expiration_date < current_date:
            raise ValueError("Card has expired")
        return value

    @field_validator("cvv")
    def validate_cvv(cls, value):
        if not value.isnumeric():
            raise ValueError("CVV must be numeric") #pragma: no cover
        return value


class PaymentModel(BaseModel):
    amount: float = Field(
        title="Amount", description="Amount to be paid", examples=[1000.00], gt=0
    )
    card: CardInfo

class TransactionModel(BaseModel):
    message: str