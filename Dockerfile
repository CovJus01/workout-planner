
FROM node:20-alpine AS frontend-base
FROM python:3.11-slim AS backend-base


FROM frontend-base AS frontend-common

WORKDIR /app

COPY ./frontend/package*.json ./

RUN npm install

COPY ./frontend .


FROM frontend-common AS frontend-development

WORKDIR /app

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]

# ADD PRODUCTION FRONTEND
#
#
#

FROM backend-base AS backend-common

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY ./backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./backend .

FROM backend-common AS backend-development

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
