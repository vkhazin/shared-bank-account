# Shared Bank Account

## RDBMS Database

### Account

* AccountId: uuid, PK
* Owner: uuid FK to Organization
* ...

### User

* UserId: uuid, PK
* ...

### Account User

* AccountId: uuid, FK to account, composite PK
* UserId: uuid, FK to users, composite PK
* UserType: Administrator or Standard
* Status: Active or Inactive

### Transaction

* TransactionId: uuid, PK
* AccountId: uuid, FK to account
* UserId: uuid, FK to user
* Type: Deposit or Withdraw
* Amount: money
* Balance: money
* Timestamp: date-time

### Withdraw Limit

* AccountId: uuid, FK to account, composite PK
* UserId: uuid, FK to users, composite PK
* LimitType: daily, weekly, or monthly
* Amount: money
* Timestamp: date-time

Comments: Timestamp can be used to preserve history of limits where the latest record per user-id is used for verification

### Organization

* OrganizationId: uuid, PK
* ...

### Organization Users

* OrganizationId: uuid, FK
* UserId: uuid, FK
* ...

### Audit Trail

* TableName: string
* UserId: uuid
* Timestamp: date-time
* OldValues: json
* NewValues: json


## Classes

### Bank Account

#### Methods

* open(admin_user_id: str, account: dict): dict
* get(account_id: str, admin_user_id: str): dict
* update(account_id: str, admin_user_id: str, account_details: dict): dict
* close(account_id: str, admin_user_id: str)
* deposit_funds(account_id: str, user_id, amount: float)
  ```
    * User must be on the list of account users for the account
  ```
* withdraw_funds(account_id: str, user_id, amount: float): dict
  ```
    * User must not exceed limit as defined in the withdraw limits
    * Withdraw limit is compared to the total of all transactions for the given user for the day, week, or month
  ```  
* view_available_balance(account_id: str, user_id: str): dict
  ```
    * Available balance is a delta between withdraw limits
    * And total sum of withdraw transaction for the given user and account for the day, week, or month
  ```
* view_transaction_history(**kwargs): list of dict
  ```
    account_id
    user_id: based on whether user is an admin or standard apply different filter
    start_date
    end_date
  ```
* get_withdraw_limits(account_id: str, admin_user_id: str, user_id: str)
* set_withdraw_limits(**kwargs)
  ```
  account_id
  admin_user_id
  user_id
  limit_type
  amount
  ```
* add_user(account_id: str, admin_user_id: str, user: dict)
  ```
  * cannot add user to an account where user is not on the list of organization users for the account owner
  ```
* get_users(account_id: str, admin_user_id: str)
* remove_user(account_id: str, admin_user_id: str, user_id: str)
* update_user(account_id: str, admin_user_id: str, user: dict)

### Users

* No requirements provided for user management

### Organization

* No requirements provided for organization management