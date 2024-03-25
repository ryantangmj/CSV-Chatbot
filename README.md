# CellTalk

CellTalk is a chatbot designed to interact with data stored in CSV files. By leveraging Streamlit for an interactive web interface, and combining the cutting-edge capabilities of `pandasai` for intelligent data understanding with the `langchain_community`'s `Ollama` model for natural language processing, CellTalk enables users to engage in complex inquiries about their data through a conversational interface. This approach significantly simplifies data analysis, making it more intuitive and accessible to users.

## Features

- **Intuitive Data Uploads:** Seamlessly upload CSV files and view them within a user-friendly web interface.
- **Conversational Queries:** Ask complex, natural language questions about your dataset.
- **Intelligent Responses:** Receive insightful answers generated through the `Ollama` model and `SmartDataframe` technology from `pandasai`.

## Installation

1. **Clone the Repository:**
   - Clone this repository to your local machine using your preferred method.

2. **Navigate to the Project Directory:**
   - Open a terminal or command prompt and navigate to the directory containing the cloned repository.

3. **Install Dependencies:**
   - Install the required Python packages by running the following command:
     ```
     pip install -r requirements.txt
     ```

4. **Obtain a pandasAI API Key:**
   - Visit [https://pandabi.ai](https://pandabi.ai) to generate your pandasAI API Key.
   - Replace the placeholder in the script with your actual pandasAI API Key to ensure functionality.

5. **Launch the Application:**
   - Start the CellTalk application by executing:
     ```
     streamlit run <path_to_your_script.py>
     ```
   - Replace `<path_to_your_script.py>` with the actual path to your CellTalk script file.

## Usage

After successfully launching the application, use the Streamlit web interface to interact with your CSV data:

1. **Upload Your CSV File:** Use the file uploader to select and upload your CSV file.
2. **Enter Your Query:** Type your question about the data in the provided text area.
3. **Initiate the Conversation:** Click the "Chat with CSV" button to submit your query and view the response.

## Example runs
Querying information about the data in the csv file
<img src= "https://github.com/ryantangmj/CSV-Chatbot/assets/110431837/f9e07b9b-69a1-4ecd-9039-648717ce8618"/>

Plotting a graph 
<img src = "https://github.com/ryantangmj/CSV-Chatbot/assets/110431837/8a1746db-a9e9-4507-a9be-5a3d5150c3dc" />
<img src = "https://github.com/ryantangmj/CSV-Chatbot/assets/110431837/ecd66377-b200-47ab-b2a1-6d7fee6dce30" />
