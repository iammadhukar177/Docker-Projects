
# Docker Advanced Multi-Service Application

This project is a multi-service web application built using Docker. It includes the following components:

- **Frontend**: React app served via Nginx.
- **Backend**: Flask REST API.
- **Database**: PostgreSQL.

The entire application is containerized using Docker Compose, making it easy to set up and run.

---

## Project Structure

```
docker-advanced-project/
├── backend/
│   ├── app.py                # Flask backend
│   ├── requirements.txt      # Python dependencies
│   ├── init.sql              # Database initialization script
│   └── Dockerfile            # Dockerfile for backend
├── frontend/
│   ├── Dockerfile            # Dockerfile for frontend
│   ├── package.json          # React app configuration
│   ├── public/               # Static files (favicon, index.html)
│   └── src/                  # React source files (App.js, index.js)
├── docker-compose.yml        # Compose configuration for services
└── README.md                 # Project documentation
```

---

## Prerequisites

Ensure you have the following installed on your system:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## How to Run the Application

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/docker-advanced-project.git
cd docker-advanced-project
```

### 2. Build and Start the Services

Run the following command to build and start the containers:

```bash
docker-compose up --build
```

This command will:
- Build the React frontend.
- Build the Flask backend.
- Start the PostgreSQL database and initialize it with `init.sql`.

### 3. Access the Services

- **Frontend (React)**: [http://localhost:3000](http://localhost:3000)
- **Backend (Flask API)**: [http://localhost:5000/api/data](http://localhost:5000/api/data)
- **Database (PostgreSQL)**: Connect using the credentials in the `docker-compose.yml` file.

---

## Services Overview

### **Frontend**
- Built with React.
- Dockerfile uses Nginx to serve the static build.
- Access: [http://localhost:3000](http://localhost:3000)

### **Backend**
- Built with Flask.
- API endpoint: `/api/data` (fetches data from the PostgreSQL database).
- Access: [http://localhost:5000](http://localhost:5000)

### **Database**
- PostgreSQL database for storing application data.
- The `init.sql` script creates a table `items` and inserts sample data.

---

## Environment Variables

The following environment variables are used in the project:

### **Backend**
Defined in `docker-compose.yml`:
- `DB_HOST`: Database host (set to `db` for Docker networking).
- `DB_NAME`: Database name.
- `DB_USER`: Database user.
- `DB_PASS`: Database password.

### **Database**
Defined in `docker-compose.yml`:
- `POSTGRES_USER`: PostgreSQL username.
- `POSTGRES_PASSWORD`: PostgreSQL password.
- `POSTGRES_DB`: PostgreSQL database name.

---

## How to Test

### Frontend
- Open [http://localhost:3000](http://localhost:3000) in your browser.
- Verify the UI displays data fetched from the API.

### Backend
- Test the API endpoint: [http://localhost:5000/api/data](http://localhost:5000/api/data)
- Use tools like `curl` or Postman:
  ```bash
  curl http://localhost:5000/api/data
  ```

### Database
- Connect to the database container:
  ```bash
  docker exec -it docker-advanced-project_db_1 psql -U dockeruser -d dockerdb
  ```
- Run SQL queries:
  ```sql
  SELECT * FROM items;
  ```

---

## Stopping the Application

To stop all running services:

```bash
docker-compose down
```

To remove volumes (including the database data):

```bash
docker-compose down --volumes
```

---

## Future Enhancements

Here are some features you can add to this project:
1. **HTTPS Support**: Use Traefik or Caddy as a reverse proxy.
2. **Monitoring**: Add Prometheus and Grafana for performance monitoring.
3. **CI/CD**: Automate deployment with GitHub Actions or Jenkins.
4. **Scaling**: Deploy the app on Kubernetes for horizontal scaling.

---

## Troubleshooting

### Common Issues
- **Port Conflict**: Ensure no other services are using ports `3000`, `5000`, or `5432`.
- **Database Connection Error**: Verify the backend environment variables for database credentials.

---

## License

This project is open-source and licensed under the MIT License. Feel free to use and modify it for your own purposes.

---
