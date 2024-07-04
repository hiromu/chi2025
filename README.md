# Redirector for CHI

This repository assumes a CSV file (`list.csv`) containing `id`, `pwa_url`, and `paper_url`.
Every time the CSV file is updated, its GitHub Actions prepare the following pages:

- `/link/paper/${id}/`: This redirects to the `paper_url` with the corresponding `id`.
- `/qr/paper/${id}/`: This shows a QR code for the `paper_url` with the corresponding `id`.
- `/link/pwa/${id}/`: This redirects to the `pwa_url` with the corresponding `id`.
- `/qr/pwa/${id}/`: This shows a QR code for the `pwa_url` with the corresponding `id`.
