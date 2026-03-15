pipeline {

    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t cbdocker2525/iris-ml-model .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push cbdocker2525/iris-ml-model:latest'
            }
        }

    }
}