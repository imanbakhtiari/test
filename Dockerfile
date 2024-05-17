FROM python:3.11

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Required to install postgresql-client with Pip
# RUN apt-get update && \
#     apt-get install -y --no-install-recommends \
#     # postgresql-client


# install dependencies with requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application files into the image
COPY . .

ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
#RUN python3 manage.py runserver 0.0.0.0:8000
#RUN chmod +x docker-entrypoint.sh

# Expose port 8000 on the container
EXPOSE 8000

