# 📤 GitHub Push Guide

## 1. Initialize the repository

```bash
cd EchoSphere
git init
git add .
git commit -m "Initial commit: EchoSphere v1.0.0"
```

## 2. Create a new repository on GitHub

1. Go to https://github.com/new
2. Name it `EchoSphere` (or your preferred name)
3. Leave "Initialize with README" **unchecked** (you already have one)
4. Click **Create repository**

## 3. Connect and push

```bash
git branch -M main
git remote add origin https://github.com/<your-username>/EchoSphere.git
git push -u origin main
```

## 4. Recommended repo settings

- Add topics: `streamlit`, `python`, `internship-project`, `dashboard`
- Add a short description + the tagline as the repo description
- Enable **Issues** if you plan to track future-scope items
- Add a `docs/screenshots/` image to the repo's social preview

## 5. Keeping it updated

```bash
git add .
git commit -m "Describe your change"
git push
```
