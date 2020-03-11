# Module 1 - Create  Blockchain
# block needs a datetime stamp
import datetime
# to hash the blocks
import hashlib
#usd the dumps function from json to encode the blocks before we hash them
import json
# we need to create an instance of the flask class which will be the
# web application itself and jsonify is a function we will use to return
# the messages and postman when we interact with our blockchain.
#for example when we make the request to get the current state of the chain
#to display the whole blockchain and jsonify to diplay the postman response
#of the request and when we mine a new block to add it to the blockchain, we 
#will use the jsonify function to return the key inforamtions of  this new
#block which was mined in json format.
# Basically we will be returning in json format the index of this new block
#the proof of this new blcok and the previous hash attached to this new block
#and also a message to say that the block was just mined.
from flask import Flask, jsonify

#Part 1 - Build a blockchain

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
        
    def create_block(self, proof, previous_hash):
        block = {'index' : len(self.chain) +1,
                 'timestamp' : str(datetime.datetime.now()),
                 'proof' : proof,
                 'previous_hash' : previous_hash}
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]
    
    def proof_of_work(delf, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode().hexdigest())
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof +=1
        return new_proof
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexadigist()
    
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['prrof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode().hexdigest())
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index +=1
        return True


# Mining our blockchain
# creating a web app
        
app = Flask(__name__)

 
# creating a blockchain
blockchain = Blockchain()


# Mining A New Block        
@app.route("/mine_block", methods=("GET"))
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block("proof")
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    blockchain.create_block(proof, previous_hash)
    block = blockchain.create_block(proof, previous_hash)
    response = {"message" : 'Congratulations, you just mined a block!',
                'index' : block('index'),
                'timestamp' : block('timestamp'),
                'proof' : block('proof'),
                'previous_hash' : block('previous_hash')}
    return jsonify(response), 200

#Getting the full Blockchain
    
@app.route('/get_chain', methods='GET')
def get_chain():
    response = {'chain' : blockchain.chain,
                'length' : len(blockchain.chain)}
    return jsonify(response), 200
    
    
    
    