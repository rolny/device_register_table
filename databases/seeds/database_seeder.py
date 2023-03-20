"""Base Database Seeder Module."""
from masoniteorm.seeds import Seeder

from .staff_table_seeder import StaffTableSeeder
from .device_table_seeder import DeviceTableSeeder


class DatabaseSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        self.call(StaffTableSeeder)
        self.call(DeviceTableSeeder)
