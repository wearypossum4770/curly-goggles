class Water:
    def __init__(self):
        self.deny_infant = None
        self.warning = None

    def recommended_min(self, child_age=None):
        pass

    def recommended_max(self, child_age=None):

        if child_age is None:
            self.warning = (
                f"We received a child age of: {child_age}\nPlease check and try again."
            )
