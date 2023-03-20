"""StaffTableSeeder Seeder."""
from masoniteorm.seeds import Seeder
from masonite.facades import Hash

from app.models.Staff import Staff


class StaffTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Staff.create(
            {
                "name": "Joe",
                "staff_number": "qwe456"
            }
        )

        Staff.create(
            {
                "name": "XXX",
                "staff_number": "we123"
            }
        )
