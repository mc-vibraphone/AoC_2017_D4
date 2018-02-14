

def validate_passphrase(phrase):
    bits = set()
    for bit in phrase.split():
        print(bit)
        if bit in bits:
            return False
        bits.add(bit)
    return True
