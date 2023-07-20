"""StaffTableSeeder Seeder."""
from masoniteorm.seeds import Seeder

from app.models.Staff import Staff


class StaffTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Staff.create(
            {
                "name": "Joe",
                "number": "qwe456"
            }
        )

        Staff.create(
            {
                "name": "XXX",
                "number": "we123"
            }
        )
