# Gunakan Python
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy File sira
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Buka porta sira
EXPOSE 8000

# Lao Django Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
