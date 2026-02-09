__ACTION_PERM_MAP = {
    "list": "view",
    "create": "add",
    "retrieve": "view",
    "update": "change",
    "partial_update": "change",
    "destroy": "delete",
}

def get_perm(action: str) -> str:
    """
    Mapeia o tipo de permissão equivalente a view.action
    ---
    O retorno será view, add, change ou delete
    """
    perm =  __ACTION_PERM_MAP.get(action)
    if not perm:
        raise ValueError(f"Action '{action}' not found in ACTION_PERM_MAP")
    return perm
    