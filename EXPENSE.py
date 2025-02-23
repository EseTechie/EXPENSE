class Expense:
    def __init__(self, title: str, amount: float):
        self.id = str(uuid.uuid4())  # Generate a unique UUID
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
    
    def update(self, title: str = None, amount: float = None):
        if title:
            self.title = title
        if amount:
            self.amount = amount
        self.updated_at = datetime.utcnow()
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

class ExpenseDatabase:
    def __init__(self):
        self.expenses = []
    
    def add_expense(self, expense: Expense):
        self.expenses.append(expense)
    
    def remove_expense(self, expense_id: str):
        self.expenses = [expense for expense in self.expenses if expense.id != expense_id]
    
    def get_expense_by_id(self, expense_id: str):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None
    
    def get_expense_by_title(self, title: str):
        return [expense for expense in self.expenses if expense.title.lower() == title.lower()]
    
    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]
