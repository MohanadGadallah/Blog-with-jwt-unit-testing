

# FastAPI Project for Blogs Website

This project is a REST API for a blogs website, developed using FastAPI. It incorporates modern development practices and tools to ensure robust and efficient performance.

## Key Features

### Environment
- **Poetry**: Manages dependencies and virtual environments.

### Database
- **SQLAlchemy ORM**: Provides seamless interaction with the database.

### API Development
- **FastAPI**: Powers the REST API endpoints.
- **Status Codes and HTTPExceptions**: Manages responses and errors.
- **Repository Design Pattern**: Abstracts data access logic for better separation of concerns.
- **Routes**: Organizes API routes for various functionalities.

### Authentication
- **JWT**: Implements JSON Web Tokens for secure authentication.
- **OAuth2**: Integrates OAuth2 for enhanced authentication and third-party service support.

### Async Operations
- **Async I/O**: Utilizes asynchronous programming for improved performance.

### Containerization
- **Docker**: Containers the application for consistent environments across development and production.

### Testing
- **Pytest**: Facilitates writing and executing tests.
- **Mock DB**: Uses a mock database for initial test cases.

## Recent Updates (As of 11/8)
1. **Database Engine**: Transitioned from SQLite to PostgreSQL for advanced features and improved performance.
2. **Database Management Tool**: Integrated `adminpg` for managing and viewing the PostgreSQL database.

## To-Do List
1. **Structure the project**
2. **Database Migration Tool**: Continue using Alembic for migrations.
3. **Separate Databases**: Maintain and manage separate databases for production and testing environments.
4. **Comprehensive Unit Tests**: Develop more unit tests using the test database.

## Installation Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MohanadGad38/Blog-with-jwt-unit-testing.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Blog-with-jwt-unit-testing
   ```
In the `fast-api` folder, you must create two environment files before running the project:

1. **`database_mangement.env`**
   ```bash
   PGADMIN_DEFAULT_EMAIL="test@gmail.com"
   PGADMIN_DEFAULT_PASSWORD="test"
   ```

2. **`database.env`**
   ```bash
   POSTGRES_USER="MM"
   POSTGRES_PASSWORD="1G"
   POSTGRES_DB=blog
   ```



4. **Set up the databases:**
   - Ensure PostgreSQL is running.
   - Create the `blog` database:
     ```sql
     CREATE DATABASE blog;
     ```
   - Configure the database URLs in your `.env` file.

5. **Run the application:**
   ```bash
   docker-compose up
   ```
6. **Install dependencies if you want to run it without docker but you must run database:**  
   ```bash
   poetry install
   ```



## Usage

Once the application is running, you can access the API at:  
`http://localhost:8000`

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

