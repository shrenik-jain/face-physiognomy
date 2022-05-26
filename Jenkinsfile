pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS=credentials('DockerHub')
    }

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main', credentialsId: 'github', url: 'https://github.com/shrenik-jain/face-physiognomy.git'
            }
        }

        stage('Docker Build') {
            steps {
                sh "docker build -t ${DOCKERHUB_CREDENTIALS_USR}/face-physiognomy:latest ."
            }
        }

        stage('Docker Login') {
            steps {
                sh "docker login -u ${DOCKERHUB_CREDENTIALS_USR} -p ${DOCKERHUB_CREDENTIALS_PSW}"
            }
        }

        stage('Docker Push') {
            steps {
                sh "docker push ${DOCKERHUB_CREDENTIALS_USR}/face-physiognomy:latest"
            }
        }

    }

    post {
        always {
            sh "docker logout"
        }
    }
}
