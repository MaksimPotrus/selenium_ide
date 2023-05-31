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
<<<<<<< HEAD
    sh 'pip3.10 install -r ./requirements.txt'
}
    stage ('Test'){
        steps {
<<<<<<< HEAD
        sh 'pytest --version'
=======
>>>>>>> b6e990d8d51b55a822555680c1ff90fd8e0f009d
            sh 'pytest test_login.py'
        }
    }
}
}
