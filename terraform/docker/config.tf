terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.13.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "web_app" {
  name         = "dantara/devops-python-app"
  keep_locally = false
}

resource "docker_container" "web_app" {
  image = docker_image.web_app.latest
  name  = "web-app"
  ports {
    internal = 5000
    external = 80
  }
}
