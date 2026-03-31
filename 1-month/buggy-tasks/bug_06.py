# Bug count: ? (find them all)
# Topic: file I/O, with statement, string methods, loops
# Give after: L10
#
# Scenario: A log file analyzer for a small web server.
#           The program reads a log file, counts how many times
#           each status code appears, and writes a summary report.
#
# First create this test file manually (or the program creates it):
#   log.txt contents:
#     200 /home
#     404 /about
#     200 /products
#     500 /checkout
#     404 /contact
#     200 /home
#     301 /old-page
#     404 /missing
#
# Expected output in report.txt:
#   === Server Log Report ===
#   200: 3 requests
#   404: 3 requests
#   500: 1 requests
#   301: 1 requests

# Step 1: create the sample log file
with open("log.txt", "w") as f:
    f.write("200 /home\n404 /about\n200 /products\n500 /checkout\n")
    f.write("404 /contact\n200 /home\n301 /old-page\n404 /missing\n")

# Step 2: read and analyze
status_counts = {}

with open("log.txt", r) as f:  # BUG
    for line in f:
        parts = line.split(" ")
        status_code = parts[0]

        if status_code in status_counts:
            status_counts[status_code] =+ 1  # BUG
        else:
            status_counts[status_code] = 1

# Step 3: write report
with open("report.txt", "w") as f:
    f.write("=== Server Log Report ===\n")
    for code, count in status_counts:  # BUG
        f.write(f"{code}: {count} requests\n")

# Step 4: verify by printing the report
with open("report.txt", "r") as f:
    print(f.read)  # BUG

