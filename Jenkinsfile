pipeline {
agent any
stages {
    stage ('GIT Checkout'){
        steps {
            git changelog: false, poll: false, url: 'https://github.com/MaksimPotrus/selenium_ide.git'
        }
    }
    
    stage('build') {
  steps {
    sh 'pip install -r requirements.txt'
    sh 'pip install pytest'
  }
}
    stage ('Test'){
        steps {
            sh 'python test_login.py'
        }
    }
}
}