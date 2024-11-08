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

### Please note you'll need docker desktop for the next steps

4. Spin up the infra you'll need (Airflow, Evidence, Redis and Jupyter Notebook)
    ```sh
    docker compose up -d

5. For Workflow: Exec into dependents-airflow-webserver-1 and create an admin account
    ```sh
    airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin

6. For Workspace the token is 
    ```sh
    your_secure_token


