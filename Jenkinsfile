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
    sh 'pip3.10 install -r ./requirements.txt'
    sh 'pip3.10 install pytest'
    sh 'pip3.10 install selenium'
      sh 'pip3.10 install async-generator'
      sh 'pip3.10 install attrs'
      sh 'pip3.10 install certifi'
      sh 'pip3.10 install cffi'
      sh 'pip3.10 install charset-normalizer'
      sh 'pip3.10 install h11'
      sh 'pip3.10 install idna'
      sh 'pip3.10 install iniconfig'
      sh 'pip3.10 install outcome'
      sh 'pip3.10 install packaging'
      sh 'pip3.10 install pluggy'
      sh 'pip3.10 install py'
      sh 'pip3.10 install pycparser'
        sh 'pip3.10 install PySocks'
        sh 'pip3.10 install pytest-html'
        sh 'pip3.10 install pytest-metadata'
        sh 'pip3.10 install python-dotenv'
        sh 'pip3.10 install requests'
        sh 'pip3.10 install selenium'
        sh 'pip3.10 install sniffio'
       sh 'pip3.10 install sortedcontainers'
        sh 'pip3.10 install tomli'
        sh 'pip3.10 install tqdm'
        sh 'pip3.10 install trio'
        sh 'pip3.10 install trio-websocket'
        sh 'pip3.10 install webdriver-manager'
        sh 'pip3.10 install wsproto'
      sh 'pip3.10 install six'
  }
}
    stage ('Test'){
        steps {
        sh 'pytest --version'
            sh 'pytest test_login.py'
        }
    }
}
}
