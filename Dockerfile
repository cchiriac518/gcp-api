FROM python:3.8.1-slim
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./
RUN pip install Flask gunicorn
RUN pip install subprocess.run
RUN pip install flask
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app

