"""MigrationForComputersTable Migration."""

from masoniteorm.migrations import Migration


class MigrationForComputersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("computers") as table:
            table.increments("id")
            table.string("name")
            table.string("number").unique()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("computers")
