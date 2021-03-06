__author__ = 'rylan'

# import RSA module
import rsa


def main():

    # generate public and private keys
    (publicKey, privateKey) = rsa.newkeys(1048)

    # create message to digitally sign
    msg = 'I, Rylan Schaeffer, signed this sentence!'

    # hash the message using SHA-256, then sign the hash using private key
    signature = rsa.sign(msg, privateKey, 'SHA-256')

    # print message, signature and public key components
    print 'Message: ' + msg
    print 'Signature: ' + signature
    print 'Public Key (n): ' + str(publicKey.n)
    print 'Public Key (e): ' + str(publicKey.e)

    # return message, signature and public key
    return msg, signature, publicKey

if __name__ == '__main__':
    main()
