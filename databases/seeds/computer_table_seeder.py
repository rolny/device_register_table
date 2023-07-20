"""ComputerTableSeeder Seeder."""
from masoniteorm.seeds import Seeder

from app.models.Computer import Computer


class ComputerTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        for i in range(10):
            Computer.create(
                {
                    "name": f"asus{i}",
                    "number": f"ul{i}"
                }
            )


