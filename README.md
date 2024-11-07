# Bytestream

Bytestream is a unified platform that forks NocoDB and adds an analytical workspace component. It simplifies data management by handling both transactional and analytical data in one place, allowing businesses to store, process, and analyze data without juggling multiple systems.

## How to Run

1. Start the frontend:
   ```sh
   pnpm start:frontend
2. Start the backend: 
    ```sh
    pnpm start:backend
3.	Navigate to the scripts/dependents directory

4. Spin up the infra you'll need (Airflow, Evidence, and Jupyter Notebook)
    ```sh
    docker compose up -d