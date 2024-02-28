# Use an official TensorFlow runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Expose port 2375 for incoming requests
EXPOSE 2375

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install opencv-python

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y
RUN apt-get update -y && apt-get install -y libgl1-mesa-glx

COPY detect.py /app/
RUN chmod +x /app/detect.py

# Command to run on container start
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "2375"]