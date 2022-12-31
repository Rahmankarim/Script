import os

# Create 300 text files
for i in range(1, 20):
    filename = f"dumpz-{i}.txt"
    with open(filename, "w") as f:
        f.write(f"This is the content of {filename}.")  # Custom content can be added here
    print(f"Created {filename}")
