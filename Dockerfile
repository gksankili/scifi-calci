# Use an official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy source files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5011

# Run the application
CMD ["python", "app.py"]
