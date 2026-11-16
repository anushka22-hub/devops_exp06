
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Downloading code from GitHub'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building Web Application'
                bat 'dir'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing HTML using Python'
                bat 'python test.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Web Application'

                bat '''
                if not exist deployed mkdir deployed
                copy /Y index.html deployed\\
                copy /Y style.css deployed\\
                copy /Y script.js deployed\\
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed! Check Console Output.'
        }
    }
}
