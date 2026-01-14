from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool=True

product_1 = Product(id=1, name="Test Prod 1", price=999.99, in_stock=False)

product_2 = Product(id=2, name="Test Prod 2", price=24.99)