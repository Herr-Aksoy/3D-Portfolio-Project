# 3D-Portfolio-Project



## Creating .github\workflows\build-and-push.yml

In order to push images to the Docker Hub repo, we create secrets in the Githup account and use them in the file.

![parameters](project-images/repo-images/project-images.png)

```sh

    - name: Docker Login
      run: docker login --username ${{ secrets.DOCKER_USERNAME }} -p ${{ secrets.DOCKER_PWD }}

```

We go to Repo > Setting > Secrets and variables > Actions and create "New repository secrets" here.

![parameters](project-images/repo-images/repo-secrets.png)



```sh


```


```sh


```