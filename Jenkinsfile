pipeline {

    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/chandra9523/mlops-project.git'
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                docker run --rm \
                -v $PWD:/app \
                -w /app \
                python:3.11-slim \
                bash -c "pip install -r requirements.txt && python train.py"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t cbdocker2525/iris-ml-model:latest .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push cbdocker2525/iris-ml-model:latest'
            }
        }
    }
}