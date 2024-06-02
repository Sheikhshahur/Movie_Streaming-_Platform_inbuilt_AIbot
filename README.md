# Movie Streaming Platform with AI Bot

Welcome to the Movie Streaming Platform with an inbuilt AI Bot named Alif. This project is developed using Django and Dialogflow. The AI Bot, Alif, assists users by suggesting movies based on the genre input provided by the user.

## Features
- **User Authentication**: Secure login and registration system.
- **Movie Database**: A collection of movies sorted by genre.
- **AI Bot Integration**: Alif, an AI Bot, to suggest movies based on user preferences.
- **Interactive UI**: A user-friendly interface for seamless navigation and movie selection.

## Getting Started

### Prerequisites
- Python 3.x
- Django
- Dialogflow API credentials

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/moviestreamingplatform.git
   cd moviestreamingplatform
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows, use `env\Scripts\activate`
   ```

3. **Install the required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Dialogflow**
   - Create a Dialogflow agent and obtain the API credentials (JSON file).
   - Place the JSON file in the project directory and update the settings with the path to this file.

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

### Running the Project

To start the development server, use the following command:
```bash
python manage.py runserver
```

### Accessing the Platform

- Open your web browser and navigate to `http://127.0.0.1:8000/`.
- Log in with your credentials or create a new account.

## Usage

1. **Interacting with Alif**
   - Navigate to the chat interface.
   - Input your preferred movie genre.
   - Alif will suggest movies based on the input genre.

2. **Admin Panel**
   - Access the admin panel at `http://127.0.0.1:8000/admin/`.
   - Manage users, movies, and other data.

## Project Structure

- `moviestreamingplatform/`: Main project directory.
- `movies/`: Django app for managing movies.
- `users/`: Django app for user authentication.
- `chatbot/`: Integration with Dialogflow and handling AI Bot interactions.
- `templates/`: HTML templates for rendering web pages.
- `static/`: Static files (CSS, JavaScript, images).

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Django](https://www.djangoproject.com/)
- [Dialogflow](https://dialogflow.cloud.google.com/)
- All contributors and supporters.

## Contact

For any queries or support, please contact sheikhshahur57@gmail.com.

---

Thank you for using the Movie Streaming Platform with AI Bot! Enjoy your movie suggestions from Alif.
