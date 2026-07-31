#!/usr/bin/env python3


# Pseudo Code:
# 1. Get filename input → .lower()
# 2. if ends with .gif  → image/gif
# 3. elif ends with .jpg or .jpeg → image/jpeg
# 4. elif ends with .png → image/png
# 5. elif ends with .pdf → application/pdf
# 6. elif ends with .txt → text/plain
# 7. elif ends with .zip → application/zip
# 8. else → application/octet-stream


file_name = input("Enter filename: ").lower()

if file_name.endswith(".gif"):
    print("image/gif")
elif file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
    print("image/jpeg")
elif file_name.endswith(".png"):
    print("image/png")
elif file_name.endswith(".txt"):
    print("text/plain")
elif file_name.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
