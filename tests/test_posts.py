  EC2-Deploy:
    runs-on: ubuntu-latest
    needs: build
    steps: 
      - name: checkout Repo
        uses: actions/checkout@v4

      - name: Build & Deploy
        env: 
            PRIVATE_KEY: ${{secrets.SSH_PRIVATE_KEY}}
            HOSTNAME: ${{secrets.SSH_HOST}}
            USER_NAME: ${{secrets.USER_NAME}}

        run: |        
          mkdir -p ~/.ssh
          echo "$PRIVATE_KEY" > private_key && chmod 600 private_key
          ssh -o StrictHostKeyChecking=no -i private_key ${USER_NAME}@${HOST_NAME} 
          docker run -d -p 8000:8000 ${{vars.DOCKER_USERNAME}}/blog:${{github.sha}}
