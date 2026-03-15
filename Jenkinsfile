pipeline {

    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/chandra9523/mlops-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t cbdocker2525/iris-ml-model .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push cbdocker2525/iris-ml-model'
            }
        }

    }
}