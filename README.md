# 3D-Portfolio-Project

<br><br>

## Project Owners
<table>
  <tr>
    <td><img src="project-images/readme-images/AhmetAksoy.png" alt="Ahmet Aksoy" width="250"></td>
    <td><img src="project-images/readme-images/MehmetSever.png" alt="Mehmet Sever" width="250"></td>
    <td><img src="project-images/readme-images/AkifGüngör.png" alt="Akif Güngör" width="250"></td>
  </tr>
  <tr>
    <td><a href="https://www.linkedin.com/in/aksoy-ahmet/" title="LinkedIn Profili">Ahmet Aksoy</a></td>
    <td><a href="https://www.linkedin.com/in/mehmet8sever/" title="LinkedIn Profili">Mehmet Sever</a></td>
    <td><a href="https://www.linkedin.com/in/akifgungor" title="LinkedIn Profili">Akif Güngör</a></td>
  </tr>
  <tr>
    <td colspan="3"><img src="project-images/readme-images/contributions.png" alt="Contributions to main" width="750"></td>
  </tr>
</table>
<br><br>
<table>
  <tr>
    <td colspan="3"><img src="project-images/readme-images/contributions.png" alt="Contributions to main" width="750"></td>
  </tr>
  <tr>
    <td><a href="https://www.linkedin.com/in/aksoy-ahmet/" title="LinkedIn Profili">Ahmet Aksoy</a></td>
  </tr>
</table>
  
    
  



## Project Technologies

<table>
  <tr>
    <td><strong>Infrastructure:</strong></td>
    <td>AWS (Amazon Web Services), Terraform</td>
  </tr>
  <tr>
    <td><strong>Containerization & Orchestration:</strong></td>
    <td>Docker</td>
  </tr>
  <tr>
    <td><strong>CI/CD Tools:</strong></td>
    <td>GitHub Actions</td>
  </tr>
  <tr>
    <td><strong>Frontend:</strong></td>
    <td>HTML, CSS, JavaScript</td>
  </tr>
  <tr>
    <td><strong>Backend:</strong></td>
    <td>Python, Flask</td>
  </tr>
  <tr>
    <td><strong>Version Control:</strong></td>
    <td>GitHub</td>
  </tr>
  <tr>
    <td><strong>Cloud Services:</strong></td>
    <td>AWS EC2, AWS VPC</td>
  </tr>
</table>
  
    
      


## Infrastructure Process



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











