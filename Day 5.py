import hashlib

inp = "uqwqemis"

password1 = ""
password2 = ["_" for i in range(8)]

print("Computing 2nd password...\n" + "".join(password2))

i = 0

while '_' in password2:
    m = hashlib.md5()
    m.update((inp + str(i)).encode('utf-8'))
    h = m.hexdigest()

    if h[:5] == "00000":
        password1 += h[5]
        #check if 6th char is between 0-7
        if '0' <= h[5] <= '7':
            if password2[int(h[5])] == "_":
                password2[int(h[5])] = h[6]
                print("".join(password2))

    i += 1

print("\n1st Password was:\n" + password1[:8])
