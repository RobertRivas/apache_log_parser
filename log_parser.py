import apache_log_parser

with open("first-aidcompany.com-ssl_log-Aug-2020.txt", "r") as openfileobject:
    file2 = open(r"500_errors.txt", "w+")
# need while loop to read all lines into a variable
# then use variable to load line parser
# then use pandas to analyze and get all 500 errors determine if customers are being turned away

    for line in openfileobject:

        line_parser = apache_log_parser.make_parser("%h %l %u %t \"%r\" %>s %b")

        log_line_data = line_parser(str(line))
        server_errors = []
        if log_line_data['status'] == "500":
            file2.write(str(log_line_data) + '\n')



print("Done")

