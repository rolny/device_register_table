"""BookTableSeeder Seeder."""
from masoniteorm.seeds import Seeder

from app.models.Book import Book


class BookTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        for i in range(10):
            Book.create(
                {
                    "name": f"book{i}",
                    "books_number": f"ICS_{i}"
                }
            )


