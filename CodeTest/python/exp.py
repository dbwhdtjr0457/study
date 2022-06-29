import hashlib

def solution(data):
    result = hashlib.sha256(data.encode())

    print(result.hexdigest())

if __name__ == '__main__':
    data = input()

    solution(data)