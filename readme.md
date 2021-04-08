On creating the project.
On windows:

    python -m venv venv

Change the file settings.py in under myproject
at line 35 to your mail with the protocol support enabled.

To activate, https://myaccount.google.com/security?pli=1
Less secure app access option will be present. Turn on the access.
If you are just testing, then you can temporarily do this setting. For a permanent setup, I would recommend a new account. Since, using your main account will be risky.

Activate the virtual environment.Then,

    pip install -r requirements.txt

Then,
    Add your gmail credentials in th filemailCredentials.py under myproject,
    python manage.py runserver

NOTE: THE PROJECT IS MADE ON LINUX, THE PACKAGES MAY DIFFER.
NOTE: PROJECT MADE ON PYTHON 3.9.2, PIP 20.3.4.