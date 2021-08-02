# **Mailshot**

Mailshot is a wrapper around smtplib's SMTP connection and simplifying sending of email using python.

<br>

## **Example**

<br>

```python
from mailshot import Mailshot

mailshot = Mailshot()
mailshot.compose("to@example.com", subject="Example")
mailshot.send()
```

<br>

## **Install**

<br>

Run the following command

```bash
pip install mailshot
```

<br>

## **Username & Password**

<br>

Usage of [application specific passowrd](https://support.google.com/accounts/answer/185833) is recommended. Store it in the environment variable. Use `EMAIL` for storing the Gmail address and `PASSWORD` for storing application-specific passwords (recommended).

<br>

If you want to store the password in the script, you can do it as follows.

<br>

```python
from mailshot import Mailshot

mailshot = Mailshot("u@example.com", "password")
```

<br>

The best way to can take the password as an input.

<br>

```python
from mailshot import Mailshot

password = input("Password : ")

mailshot = Mailshot("u@example.com", password)
```

<br>

If you don’t want your password to show on your screen when you type it, you can import the getpass module and use `.getpass()` instead for blind input of your password.

<br>

## **Usage**

<br>

`compose()` method takes following arguments

* **to** *(required)* : A string or list of strings of recipients.
* **cc** *(optional)* : A string or list of strings of recipients of the carbon copy.
* **bcc** *(optional)* : A string or list of strings of recipients of the blind carbon copy.
* **subject** *(optional)* : A subject string.
* **text** *(optional)* : A text string.
* **html** *(optional)* : A html string to render.
* **files** *(optional)* : A file or list of files.

<br>

### Example

<br>

``` python
from mailshot import Mailshot

mailshot = Mailshot()

mailshot.compose("to@example.com", cc=["one@example.com", "two@example.com"], subject="Test Mail", text="Test Mail", files=["test.pdf", "test.png"])
```

<br>

## **Features**

<br>

Mailshot allows you to
* Send mail to bulk of recipients.
* Send text and HTML body.
* Send bulk of files.
* Send the personalised email.

<br>

## **Author**

<br>

Mailshot is developed by Rohan Pednekar.


<br>

## **License**

<br>

Mailshot is licensed under the MIT License.

<br>

## **Source Code**

<br>

Source code is available on GitHub at: [rohan-pednekar/mailshot](https://github.com/rohan-pednekar/mailshot).


<br>

## **Issues**

<br>

To file issue reports and feature requests use the project's issue tracker on GitHub.
