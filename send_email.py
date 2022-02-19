def send_email(names, type):
    from bubble_sort import bubble_sort
    import smtplib

    username = ("wuq@asmilan.org")
    password = ("**************")

    fake_from = "facial-recognition-attendance@auto.com"
    fake_name = "Facial Recognition Attendance Machine"

    to_email = ("wuq@asmilan.org")
    to_name = ("Teacher")

    subject = "{} Students".format(type)
    names = bubble_sort(names)

    content = "The following students are {} \n".format(type)
    for name in names:
        content = content + str(name) + '\n'

    message = f"From: {fake_name} <{fake_from}>\nTo: {to_name} <{to_email}>\nSubject: {subject}\n\n{content}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(username, password)
    server.sendmail(username, to_email, message.encode())
    server.close()

names = ['Ken', 'Nick']
type = 'present'
send_email(names, type)
