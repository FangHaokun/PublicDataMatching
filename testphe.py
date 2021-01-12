from phe import paillier
public_key, private_key = paillier.generate_paillier_keypair()
secret_number_list = ['a', 'b']
encrypted_number_list = [public_key.encrypt(ord(x)) for x in secret_number_list]
print(encrypted_number_list)
print([private_key.decrypt(x) for x in encrypted_number_list])
