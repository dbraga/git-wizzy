from M2Crypto import RSA
import re
import StringIO

def pgp_pubkey_to_pem(pgp_key):
    # Normalise newlines
    pgp_key = re.compile('(\n|\r\n|\r)').sub('\n', pgp_key)

    # Extract block
    buffer = StringIO.StringIO()
    # Write PEM header
    buffer.write('-----BEGIN RSA PUBLIC KEY-----\n')

    in_block = 0
    in_body = 0
    for line in pgp_key.split('\n'):
        if line.startswith('-----BEGIN PGP PUBLIC KEY BLOCK-----'):
            in_block = 1
        elif in_block and line.strip() == '':
            in_body = 1
        elif in_block and line.startswith('-----END PGP PUBLIC KEY BLOCK-----'):
            # No checksum, ignored for now
            break
        elif in_body and line.startswith('='):
            # Checksum, end of the body
            break
        elif in_body:
            buffer.write(line+'\n')

    # Write PEM footer
    buffer.write('-----END RSA PUBLIC KEY-----\n')

    return buffer.getvalue()

pem=pgp_pubkey_to_pem("/Users/dbraga/.ssh/id_rsa.pub")
print pem
# rsa = RSA.load_pub_key(pem)
# ctxt = rsa.public_encrypt(fileinput.input().read(), RSA.pkcs1_padding)
# print ctxt.encode('base64')