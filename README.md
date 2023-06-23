<a name="readme-top"></a>
[![Contributors](https://shields.io/badge/Contributors-2-green)](https://github.com/oardilac/Conversational-AI-Chatbot/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/oardilac/Conversational-AI-Chatbot)](https://github.com/oardilac/Conversational-AI-Chatbot/network/members)
[![Stargazers](https://img.shields.io/github/stars/oardilac/Conversational-AI-Chatbot)](https://github.com/oardilac/Conversational-AI-Chatbot/stargazers)
[![Issues](https://img.shields.io/github/issues/oardilac/Conversational-AI-Chatbot)](https://github.com/oardilac/Conversational-AI-Chatbot/issues)
[![MIT License](https://img.shields.io/github/license/oardilac/Conversational-AI-Chatbot)](https://github.com/oardilac/Conversational-AI-Chatbot/blob/main/LICENSE)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555)](https://www.linkedin.com/in/oardilac/)
<br />
<div align="center">
    <h3 align="center">ChatBot using GPT-4 and Langchain</h3>

   <p align="center">
    An advanced Chatbot leveraging GPT-4 and Langchain library for memory and context management.
    <br />

  <p align="center">
    <a href="https://github.com/oardilac/Conversational-AI-Chatbot/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/oardilac/Conversational-AI-Chatbot/">View Demo</a>
    ·
    <a href="https://github.com/oardilac/Conversational-AI-Chatbot/issues">Report Bug</a>
    ·
    <a href="https://github.com/oardilac/Conversational-AI-Chatbot/issues">Request Feature</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

The project is a sophisticated AI-powered chatbot leveraging OpenAI's GPT-4 model and Langchain for memory and context management. The chatbot is capable of handling contextual and semantic nuances in a conversation, offering a realistic conversational experience. It also includes an advanced utility for generating embeddings for text, searching embeddings, and parsing PDF documents.

Here's why:
* The project is a great example of building a state-of-the-art chatbot with advanced context management.
* The use of Langchain and GPT-4 demonstrates a high degree of customization, offering developers a lot of flexibility.
* The chatbot is designed to be easily adaptable and scalable to different use-cases.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

This section lists major libraries and tools used in the project.

* [OpenAI](https://openai.com/)
* [Langchain](https://github.com/langchain/langchain)
* [Pandas](https://pandas.pydata.org/)
* [Gradio](https://www.gradio.app/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Installation

1. Clone the repo

    ```
    git clone https://github.com/oardilac/Conversational-AI-Chatbot.git
    ```

2. Install required packages

    ```
    pip install -r requirements.txt
    ```

3. Run the code
   ```
   jupyter notebook main.ipynb
   ```


## Project Files

- `main.ipynb`: The main notebook which runs the chatbot application using the OpenAI's GPT-4 model. It loads the data, initializes the chatbot model, and launches the chatbot interface.

- `utils/output_parser.py`: Utility file containing the `CommaSeparatedListOutputParser` class used to parse outputs in a comma-separated list format.

- `utils/prompt_template.py`: Utility file containing functions to generate prompt templates for the chatbot system.

- `chatbot/chat_memory.py`: Contains the `ChatMemory` class which utilizes the `ConversationBufferMemory` class from the Langchain library to store and retrieve chatbot conversations.

- `chatbot/chat_model.py`: Contains the `ChatModel` class which utilizes the `OpenAI` and `ChatOpenAI` classes from the Langchain library to generate predictions for the chatbot.

- `chatbot/embeddings.py`: Contains functions to generate, search and load embeddings for the chatbot.

- `chatbot/image_generator.py`: Contains the `generate_image` function which uses OpenAI's Image API to generate images based on descriptions.

- `chatbot/langchain_document_parser.py`: Contains the `LangchainDocumentParser` class used to load and split documents using the `PyPDFLoader` and `CharacterTextSplitter` classes from the Langchain library.

- `ChatGPT`: Not a file but a proposed class that encapsulates the methods used in the `main.ipynb` notebook.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Oliver Ardila - odardilacueto@gmail.com - @oardilac

Project Link: [https://github.com/oardilac/Conversational-AI-Chatbot](https://github.com/oardilac/Conversational-AI-Chatbot)

<p align="right">(<a href="#readme-top">back to top</a>)</p>