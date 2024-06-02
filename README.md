# news_app

```markdown
# News Search App

A web-based application that allows users to search for news articles based on keywords. Users can also view the results of their previous searches and refresh search results to fetch the latest articles.

## Features

- User registration and authentication (signup, login, logout)
- Search for news articles based on a keyword
- Store search results locally
- View a list of previous searches and their results
- Open original news articles in a new tab
- Refresh search results to fetch the latest articles
- Filters for date published, source name, and category of source

## Setup Instructions

### Prerequisites

- Python 3.x
- Django 3.x or higher
- pip (Python package installer)

### Installation

1. **Clone the repository:**

    ```bash
    git clone 
    cd news-search-app
    ```

2. **Create a virtual environment:**

    ```bash
    virtualenv -p python3.11 venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory of the project and add the following variables:

    ```plaintext
    NEWS_API_KEY=your-news-api-key
    ```

5. **Run database migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser (optional):**

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

8. **Open the application in your web browser:**

    Visit `http://127.0.0.1:8000` to access the application.



## Usage

- **Sign Up:** Register a new account using your email and password.
- **Login:** Log in using your registered email and password.
- **Search:** Enter a keyword to search for news articles.
- **View Results:** View the list of articles for your search keyword.
- **Refresh Results:** Refresh the search results to fetch the latest articles.
- **Filters:** Use the filters to narrow down your search results by date and source name.

## Experience and Time Taken

**Time Taken:** Approximately 3 hours

**Overall Experience:**
Working on this project was a rewarding experience. It involved setting up user authentication, integrating with an external API (News API), and implementing features such as search, filtering, and displaying results. I also learned a lot about managing environment variables securely using `python-dotenv` and structuring a Django project effectively.

```



This `README.md` provides clear setup instructions, an overview of the project's features, and personal insights, which are useful for both developers and users of the application.