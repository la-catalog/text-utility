def stringfy(value) -> str:
    """
    In some cases it's better to show
    an empty string than "None" or "<NaN>".

    For example, i'm using in Dataframes.
    """
    return str(value or "")
