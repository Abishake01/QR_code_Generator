import qrcode

# List of data you want to generate QR codes for
data_list = [
    "https://example.com/user1",
    "https://example.com/user2",
    "https://example.com/user3",
    "Hello from Abi!",
    "1234567890"
]

# Loop through the list and create a QR code for each
for i, data in enumerate(data_list):
    img = qrcode.make(data)
    filename = f"qrcode_{i+1}.png"
    img.save(filename)
    print(f"Saved {filename} for data: {data}")
