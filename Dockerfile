# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy just the poetry files (to leverage caching)
COPY poetry.lock pyproject.toml /app/

# Install dependencies using Poetry
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root

# Copy the rest of the application code
COPY . /app

# Ensure dependencies are re-installed with the project
RUN poetry install

# Run the command-line tool when the container launches
CMD ["poetry", "run", "gaan"]

