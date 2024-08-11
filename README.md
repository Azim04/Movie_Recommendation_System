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
Run the following command in the terminal: <br> <br>


    git clone https://github.com/Azim04/Movie_Recommendation_System.git

Once the project is cloned, open it in any code editor (Pycharm is preferred) <br>
Run the following commands in terminal of the same directory which contains **manage.py** file <br>


    python manage.py makemigrations

    python manage.py migrate 

    python manage.py runserver

Once the server is initiated, you can access the project in your local browser at http://localhost:8000

# Containerizing using Docker
In order to containerize the application, install Docker 
<h3>Windows:</h3>
    Download Docker Desktop https://www.docker.com/products/docker-desktop/ <br>
<h3>Linux & Mac</h3>
    Download docker from command line: <br> <br>

    sudo apt install docker.io

<h2>Containerize</h2> 
  Once Docker is successfully installed in the system, navigate into the project where Dockerfile is located <br>
  In the terminal, run the following command to build a Docker Image: <br> <br>

    docker build . -t movie_recommendation_system

  Once the image is created, verify it using the command:<br>

    docker images

  After the image is created, run the container in detached mode on port 8000 using the above built image: <br>

    docker run -d -p 8000:8000 movie_recommendation_system

  Verify whether the container is running: <br>

    docker ps 

  Once, the container is running, access the website on http://your-device-ip:8000
