

# ===================== Convert base64 string to binary data and write to file

import base64

resp = ""
r2 = resp.encode("ascii")

# decode binary
decoded = base64.decodebytes(r2)

# Write binary data
with open('sucmanh1.mp3', 'wb') as output_file:
    output_file.write(decoded)

