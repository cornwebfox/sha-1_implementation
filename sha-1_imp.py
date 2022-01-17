#coding using pseudocode from wikipedia https://en.wikipedia.org/wiki/SHA-1#Algorithm
#only for educational purpose, this code is not designed to be used in real-life, use hashlib for that
def rotate_to_left(splitted_1, rotateLength):
    return ((splitted_1 << rotateLength) | (splitted_1 >> (32 - rotateLength))) &  0xffffffff


def sha1(a):
  h0 = 0x67452301
  h1 = 0xEFCDAB89
  h2 = 0x98BADCFE
  h3 = 0x10325476
  h4 = 0xC3D2E1F0

  l,m=[],[]
  for i in a:
    l.append(ord(i)) #converting user input to an ASCII value

  for i in l:
    m.append(format(i, '08b'))#converting an ASCII value into binary, then padding it with zeros so that it is equal to 8 bits
    joined_data = "".join(map(str,m)) # joining the lists

    another_var = joined_data + str(1) #adding 1 to the end of binary


  while len(another_var) % 512 != 448: #padding it zeros until it's equal to 448
      another_var += '0'
  gg = len(a) * 8 #getting length of 8bit ASCII value binary
  forfor =  format(gg, "08b")
  padded_64 = forfor.zfill(64) #then padding it with zeros until it's equal to 64 bits
  final_512 = another_var + padded_64 #connecting the previous and last values
  splitted_1 = final_512.split() #splitting into array of chunks
  n = 32 #now splitting it into subarray of of sixteen 32-bit value
  words = [final_512[i:i + n] for i in range(0, len(final_512), n)]

  for eachChunk in splitted_1: # looping through each array of sixteen 32-bit words and extending them to 80 words using bitwise operations
        w = [0] * 80
        for n in range(0, 16):
            w[n] = int(words[n], 2)

        for i in range(16, 80):
            w[i] = rotate_to_left((w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]), 1)


        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        #main loop algorithm taken from pseudocode:
        for i in range(0, 80):
            if 0 <= i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999

            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1

            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC

            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            a, b, c, d, e = ((rotate_to_left(a, 5) + f + e + k + w[i]) & 0xffffffff, a, rotate_to_left(b, 30), c, d)

        h0 = h0 + a & 0xffffffff
        h1 = h1 + b & 0xffffffff
        h2 = h2 + c & 0xffffffff
        h3 = h3 + d & 0xffffffff
        h4 = h4 + e & 0xffffffff

  return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)

input_text = input("Enter text: ")
print("Output: " + sha1(input_text))
