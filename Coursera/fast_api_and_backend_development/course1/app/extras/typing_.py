text: str = "Sumer"
num: int | float = .5

optional: str | None = "Sumer"
print(f"{optional=}")

table: tuple[int, ...] = (1,2,3,4,5)
print(f"{len(table)=}")

shipment: dict[str, str | None] = {"name": None, "content": "string"}
print(shipment)

def root(num: int | float) -> float:
    return num**num

print(root(num=num))