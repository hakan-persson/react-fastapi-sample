FROM node:18 AS build

WORKDIR /jsapp

COPY jsapp/*.json ./
COPY jsapp/*.js ./

# RUN npm ci --omit=dev
RUN npm ci

COPY jsapp/public ./public
COPY jsapp/app ./app
RUN npm run build


FROM python:3.11-slim

WORKDIR /usr/src/app
ENV TZ="Europe/Stockholm"

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY --from=build /jsapp/out ./jsapp/out
# COPY static ./static
COPY pyapp/ ./

EXPOSE 8000

CMD [ "python", "./main.py" ]
