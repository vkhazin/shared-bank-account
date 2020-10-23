
def open(admin_user_id: str, account: dict) -> dict:
    """
    * User id will be added to account user as admin

    # Validate the account dict contains required keys and values
    # Convert dict to an insert sql statements: insert account and insert account_user
    # Leverage internal use class `Repository` to open a connection and execute sql statements within transation

    # Leverage try-except block to log errors before returning an error to the caller

    # Return account dict
    """

# ...more methods...