# CampusLink Uganda

A Streamlit student platform for:

- 🏠 Hostels
- 💼 Jobs and internships
- 🎓 Scholarships

## How the data works

All listings are stored in:

`data/listings.xlsx`

The workbook has three sheets:

- `Hostels`
- `Jobs`
- `Scholarships`

To add or edit a listing, edit the appropriate Excel sheet, save the workbook, commit it to Git, and push it to GitHub. Streamlit Cloud will redeploy the app after the repository changes.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Create a GitHub repository.
2. Upload this entire project.
3. Go to Streamlit Community Cloud.
4. Connect your GitHub account.
5. Select the repository.
6. Select `app.py` as the main file.
7. Deploy.

## Important

Replace the sample `example.com` links in `data/listings.xlsx` with real application, contact, Google Maps, university, employer, or scholarship-provider links.

## Suggested future features

- University-specific filtering
- User accounts
- Hostel owner submissions
- Job/scholarship submission form
- Expiry alerts
- WhatsApp contact buttons
- Google Maps hostel locations
- Saved/favourite listings
- Admin approval before listings appear