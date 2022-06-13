# Docker
# What is Docker?
A format that wraps a number of different tech to create containers
* Namespaces
    * Isolate parts of the container
* Control groups - `cgroups`
    * Enable the system to limit resources used by application
* Union File Systems - `UnionFS`
    * File systems built layer-by-layer and combine resources
  This wrapper is used to create an image, which is a template used to create containers from.
## Container creation workflow
  1. Image created using `docker build` or `docker pull`
  2. Container ran using `docker run` or `docker container create`
  3. If the Docker daemon does not has a local copy of the image, it is gathered from a registry
  4. The docker daemon creates a container based on the image. If `docker run` is used, the container is logged into and commands are executed
# Anatomy of a Dockerfile
First, begin with an image that fits your basic needs.
* If building a nginx reverse proxy, could use `nginx:latest`

**An incomplete list of dockerfile keywords**
* FROM -> Base image to work from
* WORKDIR -> Working directory inside the image we are building
* COPY -> Copies a file or folder from the host to the container
* RUN -> Commands to run while building the container
* CMD -> Commands to run while the container is running
* EXPOSE -> Expose a port inside the container to the outside world

# Running a Docker Container - The Cisco Way
An example to parse
`sudo docker run -d -P --name pythontest sample-app-image`
* -d -> to run in the background "detached" or "daemon" mode
* -P -> to have the container listen on the same port it exposed internally
    * --port={host}:{container}
* --name -> to specify the container's name
# Saving a Docker image to the Registry
1. Run `docker login` to authenticate with your registry
2. Have a running container instance of your image
3. Commit the container, using `docker commit {container} {image}`
4. Give the image a tag, generally in the form of `{repository}/{imagename}:{tag}`
   *  Use the command `docker tag {imagename} {repository}/{imagename}:{tag}`
   *  Example: `docker tag sample-app devnetstudent/sample-app:v1`
5. Push the image to the repository
   * Format: `sudo docker push {repository}{imagename}:{tag}`
   * Example: `sudo docker push devnetstudent/sample-app:v1`
# 
