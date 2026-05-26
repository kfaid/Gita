# Deploy to Vercel

Quick steps to deploy this project to Vercel (serves `templates/index.html` at root):

1. Install Vercel CLI:

```bash
npm i -g vercel
```

2. Login and deploy:

```bash
vercel login
vercel --prod
```

The app root `/` is rewritten to the Python serverless function at `/api/index.py` which returns `templates/index.html`.
