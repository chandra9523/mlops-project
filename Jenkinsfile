pipeline {

```
agent any

stages {

    stage('Clone Repo') {
        steps {
            git branch: 'main', url: 'https://github.com/chandra9523/mlops-project.git'
        }
    }

    stage('Setup Python Environment') {
        steps {
            sh '''
            python3 -m venv venv
            . venv/bin/activate
            pip install -r requirements.txt
            '''
        }
    }

    stage('Train Model') {
        steps {
            sh '''
            . venv/bin/activate
            python train.py
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
```

}
