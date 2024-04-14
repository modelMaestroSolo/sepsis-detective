# Use Python 3.10.9 base image
FROM python:3.10.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./requirements.txt

# Install required Python packages
RUN python -m pip install --timeout 3000 -r requirements.txt

# Copy necessary files into the container
COPY main.py .
COPY models ./models 


# Expose the port on which the API will run 
EXPOSE 8000

# Command to run the API when the container starts
CMD ["python", "main.py"]
