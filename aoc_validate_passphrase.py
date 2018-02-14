

def validate_passphrase(phrase):
    bits = set()
    for bit in phrase.split():
        bit = ''.join(sorted(bit))
        print(bit)
        if bit in bits:
            return False
        bits.add(bit)
    return True


if __name__ == '__main__':
    with open('./test_data', 'r') as f:
        phrases = f.readlines()

    count = 0
    for p in phrases:
        print('Checking {}'.format(p))
        if validate_passphrase(p):
            count = count + 1

    print('Valid count was {}'.format(count))

