# Radio Station

Radio Station is a web application that allows users to explore and manage a collection of songs sorted by genres and artists. Authenticated users have the ability to add, update, and delete data within the website.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/KirillMelanich/radio_station.git
   
2. Navigate to the project directory:
   ```shell
   cd radio-station
   
3. Install dependencies:
   ```shell
    pip install -r requirements.txt
   
4. Perform database migrations:
    ```shell
    python manage.py migrate

## Usage

1. Run the development server:
     ```shell
    python manage.py runserver
2. Open your web browser and visit:
    ```shell 
    http://localhost:8001/
3. Log in using:
    ```shell 
      admin: admin
      password: 1234
  
or create your own user using python manage.py createsuperuser

4. Start exploring and managing the songs, genres, and artists within the Radio Station!

# Folder structure:
         
                radio_station
        ├── catalog
        │   ├── migrations
        │   ├── static
        │   ├── templates
        │   ├── admin.py
        │   ├── models.py
        │   ├── views.py
        │   ├── tests.py
        │   └── ...
    ├── radio_station
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── ...
    ├── templates
    │   ├── catalog
    │   ├── includes
    │   ├── registration
    │   ├── base.html
    │   └── ... 
    ├── static
    │   ├── asserts
    │   ├── css
    │   └── ...
    ├── manage.py
    └── README.mdradio-station
    ├── requirements.py
    └── .gitignore
    └── db.sqlite3
    └── .env



## Features:
```shell 
User authentication: Allow users to sign up, log in, and manage their account.
Songs: Browse, add, update, and delete songs in the collection.
Genres: View and manage genres of songs.
Artists: Explore and manage artists associated with songs.