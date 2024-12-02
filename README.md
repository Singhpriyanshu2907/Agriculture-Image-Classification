# Agriculture-Image-Classification

This project classifies agricultural images into 30 categories using MobileNetV2 with transfer learning. The project is built with modular code architecture, enabling easy scalability and deployment using a CI/CD pipeline. It uses tools like DVC, TensorFlow, MLflow, and Docker, with deployment on AWS EC2 and Elastic Container Registry (ECR).

#Project Structure

.dvc/                     # DVC configuration files

.github/workflows/        # CI/CD GitHub workflows

config/                   # Configuration files for pipeline and parameters

model/                    # Directory to store trained models

research/                 # Research and experimental notebooks

src/AgriClassifier/       # Source code for the application

templates/                # HTML templates (for web app, if any)

.dvcignore                # DVC ignore file

.gitignore                # Git ignore file

Dockerfile                # Dockerfile for containerization

LICENSE                   # License for the project

README.md                 # Project documentation

app.py                    # Flask/Django-based app entry point

dvc.lock                  # DVC lock file

dvc.yaml                  # DVC pipeline configuration

main.py                   # Entry point for pipeline stages

params.yaml               # Parameter configuration for model training

requirements.txt          # Dependencies list

scores.json               # Saved evaluation scores

setup.py                  # Python package setup

template.py               # Template Python script


# Steps to Run the Project

# 1. Setup the Environment
Install Python 3.10.
 Create a virtual environment:
    python3 -m venv env
    source env/bin/activate   # For Linux/Mac
    env\Scripts\activate      # For Windows

  Install dependencies:
    pip install -r requirements.txt

# 2. Data Version Control with DVC
  Initialize DVC:
    dvc init

  Pull data using DVC:
    dvc pull

# 3. Run the Pipeline
  Execute the main pipeline:
    python main.py

# 4. Model Evaluation
  Evaluate the model:
    python src/AgriClassifier/components/model_evaluation_mlflow.py

  Save evaluation metrics:
    dvc repro

# 5. Deploy the Model
  Build Docker image:
    docker build -t agriculture-classifier .
    (Deploy on AWS EC2 using Elastic Container Registry (ECR))

# Model Structure
Base Model: MobileNetV2 with pre-trained weights (ImageNet).
Input Size: 224x224x3 images.
Output Classes: 30 categories.
Optimization: Adam optimizer, learning rate from params.yaml.

# Features
MLflow for experiment tracking and model evaluation.
CI/CD pipeline for automated testing, building, and deployment.
DVC for managing data and model versions.
Dockerized Deployment on AWS EC2 with ECR.
  

# AWS-CICD-Deployment-with-Github-Actions
1. Login to AWS console.
2. Create IAM user for deployment

# with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


# Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

# Policy:
1. AmazonEC2ContainerRegistryFullAccess
2. AmazonEC2FullAccess
3. Create ECR repo to store/save docker image
4. Save the URI: 615299775421.dkr.ecr.ap-south-1.amazonaws.com/agriclassifier
5. Create EC2 machine (Ubuntu)
6. Open EC2 and Install docker in EC2 Machine:

# optinal
sudo apt-get update -y
sudo apt-get upgrade

# required
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker

# Configure EC2 as self-hosted runner:
setting>actions>runner>new self hosted runner> choose os> then run command one by one

# Setup github secrets:
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION =

AWS_ECR_LOGIN_URI =

ECR_REPOSITORY_NAME =  

# Contributing
Feel free to fork the repository, submit pull requests, or raise issues.

# License
This project is licensed under the MIT License. See LICENSE for details.
