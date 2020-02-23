def send_an_email(recipient,filename):
    try:
        df=pandas.read_csv('rootkey.csv')
        fromaddr = df['fromaddr'][0]
        password=  df['pass'][0]
        toaddr = recipient

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Prescription"
        body = ""

        msg.attach(MIMEText(body, 'plain'))
        print(filename)
        # filename="PrescriptionRaWhJNwByKR73v1V6mNpT3GDQpJ2sa1921012020.pdf"
        attachment = open(filename, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())

        # encode into base64
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, password)
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        s.quit()
        dict  = {'response': "true" }
        return jsonify(dict)
