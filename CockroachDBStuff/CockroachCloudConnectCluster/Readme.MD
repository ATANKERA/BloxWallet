This is the cloud cluster, steps to run:

https://www.cockroachlabs.com/docs/stable/build-a-python-app-with-cockroachdb-sqlalchemy.html?

and then just replace user/pass details with  your own cluster details and ou are set!

This will allow us to upload private keys and store them securely on cockroachDB and retrieve them!

I was not able to load this onto the Raspberry Pi because I did all config on windows and raspbian is linux causing migrate issues.


Note - You will need to have python and download the venv, unpack it and install requirements (SQLAlchemy)

Running a venv is like so, navigate to location on cmd, and type py -m venv venv assuming you have pip installed venv
