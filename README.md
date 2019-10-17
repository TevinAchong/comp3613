Group Members, to get started: 

# 1. Setup the PIP package manager:
```
pip -h
```

# 2. Install the virtualenv package:
```
pip install virtualenv
```

# 3. Create the virtual environment
```
virtualenv venv
```

# 4. Activate the virtual environment
## Mac OS/Linux:
```
source venv/bin/activate
```
## Windows:
```
venv\Scripts\activate
```

Now that we are inside the virtual environment, we can install all the necessary packages using:
```
pip install -r requirements.txt
```

# To exit the virtual environment, deactive the virtual environment:
```
deactivate
```