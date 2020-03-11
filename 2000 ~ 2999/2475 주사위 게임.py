checksum = input().split(' ')
print((int(checksum[0])**2 + int(checksum[1])**2 + int(checksum[2])**2 + int(checksum[3])**2 + int(checksum[4])**2) % 10)