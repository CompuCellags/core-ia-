# 🛠️ GitHub Actions: Workflows Éticos y Modulares / Ethical Modular Workflows

Este documento describe los flujos CI/CD integrados en este repositorio, alineados con prácticas éticas, trazabilidad internacional y compatibilidad multiplataforma.

---

## 🐳 Docker Image Build & Push

**Acción:** [Docker Image by GitHub Actions](https://github.com/actions/starter-workflows/blob/main/ci/docker-publish.yml)  
**Propósito:** Construir y publicar imagen Docker inmutable (`v*`)  
**Archivo:** `.github/workflows/docker-build.yml`

```yaml
uses: docker/build-push-action@v5
tags: compucellags/cc-core-models:${{ github.ref_name }}
