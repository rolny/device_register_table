"""MigrationForBorrowcomputersTable Migration."""

from masoniteorm.migrations import Migration


class MigrationForBorrowcomputersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("borrowcomputers") as table:
            table.increments("id")
            table.string("borrow_staff_number")
            table.foreign("borrow_staff_number").references("staff_number").on("staffs")
            table.string("confirm_user_id").nullable()
            table.foreign("confirm_user_id").references("id").on("users")
            table.string("computers_number")
            table.foreign("computers_number").references("number").on("computers")
            table.datetime("borrow_time").nullable()
            table.datetime("return_time").nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("borrowcomputers")
