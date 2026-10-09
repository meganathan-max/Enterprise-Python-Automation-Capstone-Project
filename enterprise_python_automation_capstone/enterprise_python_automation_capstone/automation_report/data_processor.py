from dataclasses import dataclass
from pathlib import Path
from collections import defaultdict
import csv

REQUIRED_COLUMNS = {"date", "product", "category", "quantity", "unit_price"}

@dataclass(frozen=True)
class Sale:
    date: str
    product: str
    category: str
    quantity: int
    unit_price: float
    @property
    def total(self) -> float:
        return self.quantity * self.unit_price

def load_sales(path: str | Path) -> list[Sale]:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Input dataset not found: {path}")
    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV file has no header.")
        missing = REQUIRED_COLUMNS - set(reader.fieldnames)
        if missing:
            raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
        sales = []
        for line, row in enumerate(reader, 2):
            try:
                quantity = int(row["quantity"])
                price = float(row["unit_price"])
                if quantity <= 0: raise ValueError("quantity must be positive")
                if price < 0: raise ValueError("unit_price cannot be negative")
                sales.append(Sale(row["date"].strip(), row["product"].strip(), row["category"].strip(), quantity, price))
            except (TypeError, ValueError) as exc:
                raise ValueError(f"Invalid data on CSV line {line}: {exc}") from exc
    if not sales: raise ValueError("Dataset contains no sales records.")
    return sales

def calculate_metrics(sales: list[Sale]) -> dict:
    total = sum(s.total for s in sales)
    by_product, by_category = defaultdict(float), defaultdict(float)
    for s in sales:
        by_product[s.product] += s.total
        by_category[s.category] += s.total
    top_product = max(by_product, key=by_product.get)
    top_category = max(by_category, key=by_category.get)
    return {
        "record_count": len(sales), "total_sales": total,
        "average_transaction": total / len(sales),
        "total_quantity": sum(s.quantity for s in sales),
        "top_product": top_product, "top_product_sales": by_product[top_product],
        "top_category": top_category, "top_category_sales": by_category[top_category],
        "sales_by_product": dict(sorted(by_product.items(), key=lambda x:x[1], reverse=True)),
        "sales_by_category": dict(sorted(by_category.items(), key=lambda x:x[1], reverse=True)),
    }
