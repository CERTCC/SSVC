FROM python:3.12-slim-bookworm AS base
RUN pip install --upgrade pip
WORKDIR /app

FROM base AS dependencies

# install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt
# Copy the files we need
COPY . /app
# Set the environment variable
ENV PYTHONPATH=/app/src


FROM dependencies AS test
# install pytest
RUN pip install pytest
# run the unit tests \
CMD ["pytest","src/test"]

FROM dependencies AS docs
CMD ["mkdocs", "serve", "--dev-addr", "0.0.0.0:8000"]