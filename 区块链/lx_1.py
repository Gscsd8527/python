class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
    def new_block(self):
        pass
    # Creates a new Block and adds it to the chain
    def new_transaction(self):
        pass
#         class Blockchain(object):
#             def new_transaction(self, sender, recipient,amount):
#                 pass
#
# """ 生成新交易信息，信息将加入到下一个待挖的区块中
#  :param sender: <str> Address of the Sender :
#  param recipient: <str> Address of the Recipient :param amount:
#  <int> Amount :return: <int>
#   The index of the Block that will hold this transaction """
#                 # self.current_transactions.append({'sender': sender, 'recipient': recipient, 'amount': amount, })
#                 # return self.last_block['index'] + 1
#     # Adds a new transaction to the list of transactions
    @staticmethod
    def hash(block):
        pass
    # Hashes a Block
    @property
    def last_block(self):
        pass
    # Returns the last Block in the chain pass
block = { 'index': 1,
          'timestamp': 1506057125.900785,
          'transactions': [ { 'sender': "8527147fe1f5426f9dd545de4b27ee00", 'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f", 'amount': 5, } ],
          'proof': 324984774000,
          'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824" }