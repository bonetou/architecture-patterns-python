from domain import model
from adapters import repository
from domain.model import OrderLine


class InvalidSku(Exception):
    pass


def is_valid_sku(sku, batches):
    return sku in {b.sku for b in batches}


def allocate(line: OrderLine, repo: repository.AbstractRepository, session) -> str:
    batches = repo.list()
    if is_valid_sku(line.sku, batches):
        raise InvalidSku(f"Invalid Sku {line.sku}")

    batchref = model.allocate(line, batches)
    session.commit()
    return batchref
