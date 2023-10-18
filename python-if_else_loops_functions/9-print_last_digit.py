 #!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if ord(i) <= ord('a') and ord(i) <= ord('z'):
            result += chr(ord(i) - 32)
        else:
            result += i
    print(result)
