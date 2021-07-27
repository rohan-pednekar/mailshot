from email import encoders
from email.mime.base import MIMEBase

def to_list(argument):
    """
        Gets and converts the argument to list type if it's not the type of list.

        Args:
            argument (str/list): String or list of string.
        
        Returns:
            list: A list of strings.
    """
    if type(argument) is not list:
        return [argument]
    return argument


def to_attachment(file):
    """
        Gets and open file in binary mode. Add file as application/octet-stream.
        Encode file in ASCII characters to send by email. Add header as key/value pair to attachment part.

        Args:
            attachment (str): A file.
        
        Returs:
            str: A file
    """
    filename = file
    with open(file, "rb") as f:
        attachment = MIMEBase("application", "octet-stream")
        attachment.set_payload(f.read())

    encoders.encode_base64(attachment)
    attachment.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    return attachment