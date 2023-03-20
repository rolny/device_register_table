"""MigrationForDevicesTable Migration."""

from masoniteorm.migrations import Migration


class MigrationForDevicesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("devices") as table:
            table.increments("id")
            table.string("name")
            table.string("devices_number").unique()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("devices")
