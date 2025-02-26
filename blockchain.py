import hashlib
import json
import time


class Transaction:
    def __init__(self, from_addr, to_addr, amount):
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.amount = amount


class Block:
    def __init__(self, timestamp, transactions, prior_hash=''):
        self.timestamp = timestamp
        self.transactions = transactions
        self.prior_hash = prior_hash
        self.nonce = 0
        self.hash = self.create_hash()

    def create_hash(self):
        block_string = (str(self.prior_hash) + str(self.timestamp) + str(self.transactions) + str(self.nonce)).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, target):
        target = str(id)[-3:]
        print(f'Mining block with target: {target}')
        start_time = time.time()
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.create_hash()
            # print(f"Searching through, hash :{self.hash}")
        end_time = time.time()
        print(f"Block mined! Nonce: {self.nonce}, Hash: {self.hash}")
        print(f"Time to mine block: {end_time - start_time} seconds")


class BlockChain:
    def __init__(self, id):
        self.id = id
        self.chain = [self.create_genesis_block()]
        self.difficulty = 3
        self.pending_transactions = []
        self.mining_reward = 10

    def create_genesis_block(self):
        genesis_hash = str(self.id).zfill(64)
        print(f"Genesis block. Hash: {genesis_hash}")
        return Block(time.time(), [], genesis_hash)

    def get_last_block(self):
        return self.chain[-1]

    def mine_pending_transactions(self, mining_reward_address):
        new_block = Block(time.time(), self.pending_transactions, self.get_last_block().hash)
        new_block.mine_block(self.id)

        self.chain.append(new_block)
        self.pending_transactions = [Transaction(None, mining_reward_address, self.mining_reward)]

    def create_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def get_balance_of_address(self, address):
        balance = 0
        for block in self.chain:
            for transaction in block.transactions:
                if transaction.from_addr == address:
                    balance -= transaction.amount
                if transaction.to_addr == address:
                    balance += transaction.amount
        return balance

    def valid_block(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.create_hash():
                return False
            if current_block.prior_hash != previous_block.hash:
                return False
        return True

    def to_json(self, filename):
        blockchain_json = []
        for block in self.chain:
            transactions = []
            for transaction in block.transactions:
                transactions.append({
                    "from": transaction.from_addr,
                    "to": transaction.to_addr,
                    "amount": transaction.amount
                })
            blockchain_json.append({
                "timestamp": block.timestamp,
                "nonce": block.nonce,
                "transactions": transactions,
                "hash": block.hash,
                "previous_hash": block.prior_hash
            })
        with open(filename, 'w') as file:
            json.dump(blockchain_json, file, indent=2)


id = 279449
coin = BlockChain(id)
coin.create_transaction(Transaction('address1', 'address2', 75))
coin.mine_pending_transactions('miner-address')
coin.create_transaction(Transaction('address2', 'address1', 25))
coin.mine_pending_transactions('miner-address')
coin.create_transaction(Transaction('address3', 'address4', 25))
coin.mine_pending_transactions('miner-address')
coin.create_transaction(Transaction('address4', 'address3', 55))
coin.mine_pending_transactions('miner-address')
coin.create_transaction(Transaction('address3', 'address1', 35))
coin.mine_pending_transactions('miner-address')
coin.to_json("blockchain.json")
