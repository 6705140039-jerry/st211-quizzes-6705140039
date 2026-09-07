from bank import BankAccount

def test_deposit_increases_balance():
    # Arrange
    account = BankAccount(balance=100)
    
    # Act
    new_balance = account.deposit(50)
    
    # Assert
    assert new_balance == 150