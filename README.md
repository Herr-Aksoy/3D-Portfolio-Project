# 3D-Portfolio-Project

# Tech Used

<table>
  <tr>
    <td><strong>Infrastructure:</strong></td>
    <td>AWS (Amazon Web Services), Terraform</td>
  </tr>
  <tr>
    <td><strong>Containerization & Orchestration:</strong></td>
    <td>Docker, Docker-Compose, Kubernetes</td>
  </tr>
  <tr>
    <td><strong>CI/CD Tools:</strong></td>
    <td>Jenkins, GitHub Actions, Azure DevOps</td>
  </tr>
  <tr>
    <td><strong>Configuration Management:</strong></td>
    <td>Ansible, Crossplane</td>
  </tr>
  <tr>
    <td><strong>Frontend:</strong></td>
    <td>HTML, CSS, JavaScript, Angular, React, Bootstrap</td>
  </tr>
  <tr>
    <td><strong>Backend:</strong></td>
    <td>Python, Flask</td>
  </tr>
  <tr>
    <td><strong>Databases:</strong></td>
    <td>MySQL, PostgreSQL, MSSQL</td>
  </tr>
  <tr>
    <td><strong>Version Control:</strong></td>
    <td>Git, GitHub</td>
  </tr>
  <tr>
    <td><strong>Cloud Services:</strong></td>
    <td>AWS EC2, AWS S3, AWS RDS, AWS VPC, Azure ACR (Azure Container Registry)</td>
  </tr>
</table>



## Creating .github\workflows\build-and-push.yml

In order to push images to the Docker Hub repo, we create secrets in the Githup account and use them in the file.

![parameters](project-images/repo-images/secrets-actions.png)

We create a build-and-push.yaml file to use Github Action. And we specify the secrets inside.  

**❗ Sample Code line**

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


# Video-1 30 dk

Source kodlar kullanilan iconlar 

https://boxicons.com/

adresinden alinmistir











