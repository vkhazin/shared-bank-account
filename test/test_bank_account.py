import os
import sys
sys.path.append('../')
import account

def test_open():
  result = account.open(admin_user_id = 1, account = {
    
  })
  assert result != None