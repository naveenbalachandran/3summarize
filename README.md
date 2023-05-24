## 3 Summarize

The 3 Summarize application leverages the power of GPT-3 to generate video summaries.

### Instructions to Run

To run the 3 Summarize application, follow these steps:

1. Clone the project repository to your local machine.
2. Install the necessary dependencies by running `pip install -r requirements.txt`.
3. Open the `call2llm.py` file and make any desired modifications, such as updating the endpoint or integrating your own OpenAI API key.
4. Run the application by executing the command `streamlit run app.py` in your terminal.
5. Access the application through your web browser at the provided URL (usually `localhost:8501`).

Please ensure that you have an internet connection and meet the system requirements to run the application successfully.

### Privacy and Usage Warning

**Important**: In order to make the app work without using an OpenAI API key, the app currently utilizes a GPT-3.5 endpoint exposed by the website [https://chat.theb.ai/](https://chat.theb.ai/). Please note that I have no affiliation with this website and cannot vouch for their privacy policies or data security measures.

When using this app, be cautious about the content you upload and the information you provide. Avoid uploading any sensitive or personal documents as they may be processed by the external endpoint.

If you prefer to use your own OpenAI API key for privacy and security reasons, you can update the `call2llm.py` file in the project. Replace the existing endpoint and implementation with your own API key integration. Please refer to the OpenAI documentation for more information on how to use the OpenAI API.

By using this app, you acknowledge and accept the potential risks associated with using the external GPT-3.5 endpoint and agree to take full responsibility for any data privacy concerns that may arise.

It is strongly recommended to review the privacy policies and terms of service of the external website [https://chat.theb.ai/](https://chat.theb.ai/) before using the app.

Please use the app responsibly and ensure that you comply with any applicable laws and regulations regarding data privacy and security.

### License

This project is licensed under the MIT License.
