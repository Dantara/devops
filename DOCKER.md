# Docker best practices

## List of best practices for Docker

1. Exclude unwanted files with `.dockerignore`
2. Don’t install unnecessary packages, use light base image
3. Keep the images small and standalone
4. Name different stages appropriately
5. Use multi-stage builds, when applicable
6. Avoid unnecessary dependencies
7. Clear space by removing package manager cache
8. Organize layers concisely to leverage build cache
9. Decouple different applications from each other
10. Prevent confidential data leaks (Do not put any credentials, use COPY over ADD)
11. Use linter to apply best practices to Docker images
