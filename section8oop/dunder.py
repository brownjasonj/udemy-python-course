class Book():
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    
    def __str__(self) -> str:
        return f"{self.title} by {self.author}"
        
    def __len__(self) -> int:
        return self.pages

b = Book('Life of Brian', 'Monty Python', 300)

print(b)
print(len(b))
