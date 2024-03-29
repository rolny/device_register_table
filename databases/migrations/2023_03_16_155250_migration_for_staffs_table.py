"""MigrationForStaffsTable Migration."""

from masoniteorm.migrations import Migration


class MigrationForStaffsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("staffs") as table:
            table.increments("id")
            table.string("name")
            table.string("number").unique()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("staffs")
