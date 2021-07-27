import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from mailshot.client import Client
from mailshot.utils import *
from mailshot.config import *

class Mailshot:
    """
        A class is a wrapper around smtplib's SMTP connection and allows email to be sent.

        Attributes:
            _sender (Client): A client object.
            _to (list): A list of recipients.
            _cc (list): A list of recipients of carbon copy.
                (default is a empty list)
            _bcc (list): A list of recipients of blind carbon copy.
                (default is a empty list)
            _subject (str): A string of subject.
                (default is None)
            _text (str): A text message.
                (default is None)
            _html (str): A string of HTML message.
                (default is None)
            _files (str): A list of files attached.
                (default is None)

        Methods:
            compose(to, cc=[], bcc=[], subject=None, text=None, html=None, files=None): Create and assign value to attributes.
            send(): Send composed email.
    """
    def __init__(self, email=None, password=None) -> None:
        """
            Create a client instance and assign it to the sender attribute.

            Args:
                email (str): An email string.
                    (default is None)
                password (str): A password string.
                    (default is None)
        """
        self._sender = Client(email=email, password=password)

    def compose(self, to, cc=[], bcc=[], subject=None, text=None, html=None, files=[]) -> None:
        """
            Gets and assign values to the attributes.

            Args:
            to (str/list): A string or list of strings of the recipients.
            cc (str/list): A string or list of strings of the recipients of carbon copy.
                (default is an empty list)
            bcc (str/list): A string or list of strings of the recipients of blind carbon copy.
                (default is an empty list)
            subject (str): A string of subject.
                (default is None)
            text (str): A text message.
                (default is None)
            html (str): A string of html message.
                (default is None)
            files (str/list): A list of files attached.
                (default is None)
        """
        self._to = to_list(to)
        self._cc = to_list(cc)
        self._bcc = to_list(bcc)
        self._subject = subject
        self._text = text
        self._html = html
        self._files = to_list(files)

    def send(self) -> None:
        """
            Try to log in to the server. Create a secure connection with the server and send an email.
        """
        message = MIMEMultipart()
        message["From"] = self._sender._get()["EMAIL"]
        message["To"] = ",".join(self._to)
        message["Cc"] = ",".join(self._cc)
        message["Bcc"] = ",".join(self._bcc)
        
        if self._subject is not None:
            message["Subject"] = self._subject
        
        if self._text is not None:
            message.attach(MIMEText(self._text, "plain"))
        
        if self._html is not None:
            message.attach(MIMEText(self._html, "html"))
        
        if self._files is not None:
            try:
                for file in self._files:
                    attachment = to_attachment(file)
                    message.attach(attachment)
            except:
                raise MemoryError
        
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
            server.login(self._sender._get()["EMAIL"], self._sender._get()["PASSWORD"])
            server.sendmail(
                self._sender._get()["EMAIL"], self._to + self._cc, message.as_string()
            )