# JobApplication 🤹

A web-based platforms used to connect employers with job seekers. Employers can use these platforms to post open positions that they are looking to fill, while job seekers visit or use the app to browse job opportunities and apply.<br />
<br />

### Setup 💻
After cloning repository,

- Install your virtual environment by running 
```{r}
python3 -m venv venvironment
```

-  Activate Your virtual environment on window by running
```{r}
venvironment\Scripts\activate
```

- Activate Your virtual environment on linux or mac os by running
```{r}
source venvname/bin/activate
```

- Assign Django secrete key to the variable in `.env.example` file

- Rename `.env.example` to `.env`

- install all required dependency by running 
```{r}
pip install Django
pip install pillow
pip install python-dotenv
```
- merge migration  by running
```{r}
python3 manage.py makemigrate --merge
python3 manage.py migrate
```

- Run the Apllication 
```{r}
python3 manage.py runserver
```

**Note** In case you encounter an error after running the application, Create some entry in the DB and don't let your databease be empty if the error persists [Create issue in the repo](https://github.com/KOLEAJEOLAYINKA/Job-Application/issues) 

### Technologies 🛠
- [Django](https://www.djangoproject.com/)
