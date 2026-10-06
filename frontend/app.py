import streamlit as st
import requests

st.set_page_config(
	page_title="LegalEase",
	page_icon="⚖️"
)

st.title("⚖️ LegalEase")
st.subheader("AI-Powered Legal Document Generator")

document_type = st.selectbox(
	"Select Document Type",
	[
		"Rental Agreement",
		"Employment Agreement",
		"Non-Disclosure Agreement",
		"Leave and License Agreement",
		"Affidavit",
		"Legal Notice"
	]
)

user_details = st.text_area(
	"Enter the required details",
	placeholder="Enter names, dates, address, terms, etc."
)

if st.button("Generate Document"):

	if not user_details.strip():

		st.warning("Please enter the required details.")

	else:

		response = requests.post(
			"http://127.0.0.1:8000/generate",
			json={
				"document_type": document_type,
				"user_details": user_details
			}
		)

		if response.status_code == 200:

			result = response.json()

			st.success("Document generated!")

			st.text_area(
				"Generated Document",
				result["document"],
				height=500
			)

		else:

			st.error("Something went wrong.")
