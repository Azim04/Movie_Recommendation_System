<h1>Movie Recommendation System</h1>
Hey viewer ! <br>
The project is a Movie Recommendation System developed in Django.<br>
It uses the Kaggle dataset of movies. <br>
Once you select a movie, the platform will recommend you the movie consisting of the same Genre as that of the selected movie.<br>
It also uses a search box, that makes it easier to search for the movie that you wish to search for. <br>
Feel free to download this project ! <br>

<h2>Install Python on your system</h2>
    Download python from https://www.python.org/downloads/ <br>
    Please refer to the original documentation of python at https://docs.python.org/3/ <br>
    
<h2>Install Django in the system</h2>
    Once python is downloaded and successfully installed in the system, install Django in your system by running the following command:<br><br>
    

    pip install django
    
Refer to the Django documentation --> https://docs.djangoproject.com/en/5.1/

<h2>Clone the project</h2>
Run the following command in the terminal: <br> 


    git clone https://github.com/Azim04/Movie_Recommendation_System.git

Once the project is cloned, open it in any code editor (Pycharm is preferred) <br>
Run the following commands in terminal of the same directory which contains **manage.py** file <br>


    python manage.py makemigrations

    python manage.py migrate 

    python manage.py runserver

Once the server is initiated, you can access the project in your local browser at http://localhost:8000
