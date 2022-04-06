
pipeline {
    agent any
    stages {
        stage("Image build and push in China") {
            steps {
                script {
                    sh """
                    node -e 'console.log(v8.getHeapStatistics().heap_size_limit/(1024*1024))'
                    export NODE_OPTIONS="--max-old-space-size=8192"
                    node -e 'console.log(v8.getHeapStatistics().heap_size_limit/(1024*1024))'
                    node --max-old-space-size=8192
                    echo $NODE_OPTIONS
                    """
                }
            }
        }
    }
}
