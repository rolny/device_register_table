"""MigrationForBorrowbooksTable Migration."""

from masoniteorm.migrations import Migration


class MigrationForBorrowbooksTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("borrowbooks") as table:
            table.increments("id")
            table.string("borrow_staff_number")
            table.foreign("borrow_staff_number").references("staff_number").on("staffs")
            table.string("confirm_user_id").nullable()
            table.foreign("confirm_user_id").references("id").on("users")
            table.string("books_number")
            table.foreign("books_number").references("number").on("books")
            table.datetime("borrow_time").nullable()
            table.datetime("return_time").nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("borrowbooks")
