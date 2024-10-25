# AI Decision-Making Assistant

Welcome to the AI Decision-Making Assistant! This Streamlit application helps users determine the appropriate AI or machine learning approach based on their needs and provides AI-generated assistance using OpenAI's API.

Applink: https://thinkai.streamlit.app/

## Features

- **Goal Identification**: Helps users identify their main AI-related goals.
- **Data Assessment**: Guides users through assessing data availability and types.
- **Objective Definition**: Assists in defining objectives with the available data.
- **Business Considerations**: Considers business requirements like interpretability, accuracy, and resource constraints.
- **AI Assistance**: Generates prompts and retrieves AI-generated recommendations using OpenAI's GPT-4 model.

## Installation

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/abh2050/ThinkAI)
   cd your-repo-name
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key to the `.env` file:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

## Usage

1. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

2. **Interact with the application**:
   - Follow the on-screen instructions to input your goals, data types, and objectives.
   - Generate AI assistance prompts and view AI-generated recommendations.

## Requirements

- Python 3.x
- Streamlit
- OpenAI
- python-dotenv

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

