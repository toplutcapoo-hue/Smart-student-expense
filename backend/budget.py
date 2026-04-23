class Budget:
    def __init__(self, limit):
        self.limit = limit

    def check_budget(self, total):
        if total > self.limit:
            return "⚠️ Budget exceeded!"
        else:
            return "✅ Within budget"
