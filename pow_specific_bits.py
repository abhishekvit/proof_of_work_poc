import hashlib
import time

max_nonce = 2 ** 32 # 4 billion

def proof_of_work(header, difficulty_bits):

    # calculate the difficulty target
    #target = 2 ** (256-difficulty_bits)

    target = 10 * difficulty_bits
    for nonce in range(max_nonce):
        hash_result = hashlib.sha256((str(header)+str(nonce)).encode('utf-8')).hexdigest()
        print (" target %d " % target )
        print ("Nonce %d" % nonce)
        print ("Hash is %s" % hash_result)
        print("int of result %d" % int(hash_result, 16))   
        # check if this is a valid result, below the target
        if int(hash_result, 16) < target:
        #if int(hash_result, 16) % target == 0:
            #print (" target %d " % target )
            #print ("Success with nonce %d" % nonce)
            #print ("Hash is %s" % hash_result)
            print ( "success" )
            return (hash_result,nonce)
        else:
            print("failed")

    print ("Failed after %d (max_nonce) tries" % nonce)
    return nonce


if __name__ == '__main__':

    nonce = 0
    hash_result = ''

    # difficulty from 0 to 31 bits
    original_max_range = 32
    test_range = 32
    '''
    for difficulty_bits in range(test_range):

        difficulty = 2 ** difficulty_bits
        print ("Difficulty: %ld (%d bits)" % (difficulty, difficulty_bits))

        print ("Starting search...")

        # checkpoint the current time
        start_time = time.time()

        # make a new block which includes the hash from the previous block
        # we fake a block of transactions - just a string
        new_block = 'test block with transactions' + hash_result

        # find a valid nonce for the new block
        (hash_result, nonce) = proof_of_work(new_block, difficulty_bits)
           
        # checkpoint how long it took to find a result
        end_time = time.time()

        elapsed_time = end_time - start_time
        print ("Elapsed Time: %.4f seconds" % elapsed_time)

        if elapsed_time > 0:

            # estimate the hashes per second
            hash_power = float(int(nonce)/elapsed_time)
            print ("Hashing Power: %ld hashes per second" % hash_power)
    '''
    difficulty_bits = 101 # with increase in difficulty bits the time to attain the nonce value increases cool? for our assignment this sould suffice?4

    # you can change/tweak the logic of nonce calc and we are good to go
    difficulty = difficulty_bits
    print ("Difficulty: %ld (%d bits)" % (difficulty, difficulty_bits))
    print ("Starting search...")

            # checkpoint the current time
    start_time = time.time()

            # make a new block which includes the hash from the previous block
            # we fake a block of transactions - just a string
    new_block = 'test block with transactions' + hash_result

            # find a valid nonce for the new block
    (hash_result, nonce) = proof_of_work(new_block, difficulty_bits)
               
            # checkpoint how long it took to find a result
    end_time = time.time()

    elapsed_time = end_time - start_time
    print ("Elapsed Time: %.4f seconds" % elapsed_time)

    if elapsed_time > 0:

                # estimate the hashes per second
        hash_power = float(int(nonce)/elapsed_time)
        print ("Hashing Power: %ld hashes per second" % hash_power)
