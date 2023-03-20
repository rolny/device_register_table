"""DeviceTableSeeder Seeder."""
from masoniteorm.seeds import Seeder

from app.models.Device import Device


class DeviceTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        for i in range(10):
            Device.create(
                {
                    "name": f"eth{i}",
                    "devices_number": f"eth{i}"
                }
            )


