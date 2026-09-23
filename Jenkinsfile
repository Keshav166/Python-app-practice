pipeline {
    agent any
 
    stages {
 
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
 
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t python-demo .'
            }
        }
 
       stage('Run Docker Container') {
        steps {
            sh '''
                docker run -d --name python-demo-container python-demo
                sleep 5
                docker ps
                docker stop python-demo-container
                docker rm python-demo-container
            '''
        }
    }
    }
}