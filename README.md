# commonect
The web application for the Commonect application


## Tools and Requirements

-   Docker
-   Typescript
-   Vue
-   FastAPI
-   PostgreSQL

## Development

To get started developing, make sure you first have docker installed. Once we have that we can simply start the develoment services by navigating to the root directory of this project (it contains a `compose.yaml` file) and running the following command:
```
docker compose up
```
This should start up 2 services. `commonect-backend-dev` and `commonect-frontend-dev`. The frontend service is already setup to proxy certain requests to the backend service and can be reached at `localhost:5173`

Happy developing!
