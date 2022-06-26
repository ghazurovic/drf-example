def get_unique_or_none(model, **kwargs):
    """Gets unique or None for provided model.
    Args:
        model (Model): Model on which query should be performed.
    Returns:
        Model: Result of query as signle instance or None.
    """
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None
    except model.MultipleObjectsReturned:
        return None
