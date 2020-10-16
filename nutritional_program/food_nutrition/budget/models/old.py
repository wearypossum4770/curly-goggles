class Order:
    """
    Track usage
    """

    cash_based
    currency_code
    start_date
    download_token


class Item:
    name
    item_type
    description
    vendor = ForeignKey(Vendor, on_delete=Cascade)
    numeric_size = "positieve intgerfield"
    related_item = "array field"


class ItemInfo:
    item = ForeignKey(Item, on_delete=Cascade)
    dated_ordered = DateTimeField(auto_now_add=True)
    arrival_date = DateTimeField(auto_now_add=True)
    purchase_date = DateField()
    expiration_date = DateField()
    date_opened = DateField()
    discard_date = DateField()
    price = DecimalField(max_digits=7, decimal_places=2)
    is_open = BooleanField(default=False)
    was_discarded = BooleanField(default=False)


class ItemImages:
    item = "Forein key"
    image_url = "image url"


class Vendor:
    pass


class ItemInventory:
    pass


class Owner:
    pass


class Nutrition:
    pass


class Supplier:
    pass
