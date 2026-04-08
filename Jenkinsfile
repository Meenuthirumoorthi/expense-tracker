pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Meenuthirumoorthi/expense-tracker.git'
            }
        }

        stage('Build Docker') {
            steps {
                sh 'docker build -t expense-app ./backend'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker stop expense || true'
                sh 'docker rm expense || true'
                sh 'docker run -d -p 5000:5000 --name expense expense-app'
            }
        }
    }
}
