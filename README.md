# AI Tourism Advice

## Description
AI Tourism Advice is a Streamlit-based web application that provides personalized travel recommendations using OpenAI's GPT-3.5 model. Users can input any destination, and the app will generate detailed information about tourist attractions and cultural insights for that location.

## Features
- User-friendly interface for entering travel destinations
- AI-powered tourism advice generation
- Detailed information about attractions and cultural insights
- Error handling for API issues and empty inputs

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ai-tourism-advice.git
   cd ai-tourism-advice
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key in Streamlit secrets:
   - Create a `.streamlit/secrets.toml` file in your project directory
   - Add your OpenAI API key to the file:
     ```
     OPENAI_API_KEY = "your-api-key-here"
     ```

## Usage

Run the Streamlit app:

streamlit run app.py


Then, open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

1. Enter a destination in the text input field.
2. Click the "Get Tourism Advice" button.
3. Wait for the AI to generate advice about your chosen destination.

## Dependencies
- streamlit
- openai

## Configuration
Make sure to set your OpenAI API key in the Streamlit secrets file as described in the Installation section.

## Error Handling
The app includes error handling for:
- Missing API key
- Empty destination input
- API request failures

## Contributing
Contributions to improve the app are welcome. Please fork the repository and create a pull request with your changes.

## License
MIT License

Copyright (c) 2024 Ryan Lazar

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM

## Acknowledgements
- This project uses the OpenAI GPT-3.5 model for generating tourism advice.
- Built with Streamlit for easy web app deployment.
