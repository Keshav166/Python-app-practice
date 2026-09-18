# 1. Use Python as the base image
FROM python:3.12

# 2. Set the working directory
WORKDIR /app

# 3. Copy requirements first
COPY requirements.txt .

# 4. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your Python code
COPY . .

# 6. Run the application
CMD ["python", "app.py"]