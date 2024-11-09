# TinyAGI Hub

Welcome to the **TinyAGI Hub**! This is the official community marketplace for sharing, discovering, and contributing AI agents, plugins, modules, and tools that expand the functionality of the TinyAGI framework. TinyAGI Hub is an open platform for the AI community to collaborate, innovate, and push the boundaries of what AGI can achieve.

[](LICENSE)

---

## 📖 **Table of Contents**

- [About TinyAGI Hub](#about-tinyagi-hub)
- [Categories](#categories)
  - [Agents](#agents)
  - [Plugins](#plugins)
  - [Modules](#modules)
  - [Tools](#tools)
- [🛠️ TinyAGI-Hub Streamlit UI](#-tinyagi-hub-streamlit-ui)
  - [🚀 Features](#-features)
  - [🧰 Setup Instructions](#-setup-instructions)
  - [📚 Documentation](#-documentation)
- [📝 **Contributing**](#contributing)
  - [Submitting Your Contribution](#submitting-your-contribution)
  - [Contribution Checklist](#contribution-checklist)
- [📜 **Code of Conduct**](#code-of-conduct)
- [📚 **Resources**](#resources)

---

## 🌌 **About TinyAGI Hub**

TinyAGI Hub is a **centralized marketplace** for community-contributed components that enhance the TinyAGI framework. By enabling users to share their own agents, plugins, modules, and tools, TinyAGI Hub accelerates AGI development and provides users with a rich repository of resources to create more powerful and adaptable AGI systems.

Contributions are organized into categories to make it easy for users to find the exact functionality they need, from specialized agents to API-integrated tools. Join the TinyAGI community in building a truly collaborative platform for AGI innovation!

---

## 📂 **Categories**

TinyAGI Hub organizes contributions into four primary categories. Each category is designed to support a unique aspect of TinyAGI’s functionality, making it easier for users to integrate and experiment with a diverse range of components.

### 🔹 **Agents**

The [Agents](https://github.com/SullyGreene/TinyAGI-Hub/Agents) category houses specialized AI agents with custom configurations and behaviors. These agents can be configured for tasks such as language generation, data analysis, interactive chat, and more. By downloading and configuring different agents, you can quickly create unique behaviors in your TinyAGI setup.

### 🔹 **Plugins**

Plugins in the [Plugins](https://github.com/SullyGreene/TinyAGI-Hub/Plugins) category extend the core functionality of TinyAGI by adding new capabilities. Examples include plugins for text summarization, content formatting, reference generation, and more. With plugins, TinyAGI becomes a flexible platform that adapts to your specific needs.

### 🔹 **Modules**

The [Modules](https://github.com/SullyGreene/TinyAGI-Hub/Modules) category includes reusable components that enhance the core architecture of TinyAGI. Modules may contain utilities, helper functions, or extensions that streamline development, data processing, and communication across agents.

### 🔹 **Tools**

The [Tools](https://github.com/SullyGreene/TinyAGI-Hub/Tools) category offers integrations with external resources such as APIs, data sources, and other libraries. Examples include Wikipedia lookup tools, data visualization tools, and API connectors that help agents access and process external information.

---

## 🛠️ **TinyAGI-Hub Streamlit UI**

The **TinyAGI-Hub Streamlit UI** is a comprehensive, user-friendly web application designed to manage and configure TinyAGI components seamlessly. This multi-page application allows users to:

- **Manage Agents, Plugins, Tools, Modules, and Services**: Add, remove, and configure each component with ease.
- **Build and Edit Configuration Files**: Create and modify `agent_config.json` through an intuitive interface.
- **Execute Predefined Tasks**: Run tasks directly from the UI and view outputs.
- **Integrate with TinyAGI Hub**: Clone or update the TinyAGI-Hub repository, browse available components, and import them into your setup.

### 🚀 **Features**

- **Multi-Page Interface**: Organized sections for different management tasks.
- **Real-Time Feedback**: Status messages and spinners provide user feedback during operations.
- **Configuration Builder**: View, edit, download, and upload configurations.
- **Task Execution**: Define and run tasks with configurable options.
- **Hub Integration**: Browse and import community-contributed components.

### 🧰 **Setup Instructions**

1. **Clone the Repository**

   Ensure you have [Git](https://git-scm.com/) installed.

   ```bash
   git clone https://github.com/SullyGreene/TinyAGI-Hub-Streamlit.git
   cd TinyAGI-Hub-Streamlit
   ```

2. **Create a Virtual Environment**

   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Open the `.env` file and replace `your_openai_api_key` with your actual OpenAI API key.

   ```env
   OPENAI_API_KEY=your_openai_api_key
   LOG_LEVEL=INFO
   ```

5. **Run the Streamlit App**

   ```bash
   streamlit run app.py
   ```

   This command will launch the Streamlit application in your default web browser.

### 📚 **Documentation**

For detailed usage instructions and further customization, refer to the [TinyAGI-Hub Streamlit Documentation](https://github.com/SullyGreene/TinyAGI-Hub-Streamlit/blob/main/README.md) (replace with the actual link if available).

---

## 📝 **Contributing**

TinyAGI Hub is powered by community contributions! We welcome your expertise and creativity in expanding the capabilities of TinyAGI. Follow these guidelines to submit your contributions to the Hub.

### Submitting Your Contribution

1. **Fork the Repository**
   
   Begin by forking the TinyAGI Hub repository to your GitHub account.
   
   ```bash
   git clone https://github.com/SullyGreene/TinyAGI-Hub.git
   cd TinyAGI-Hub
   ```
   
2. **Add Your Contribution**
   
   - **Navigate to the Appropriate Category Folder**: Choose `Agents`, `Plugins`, `Modules`, or `Tools`.
   - **Create a New Directory**: Name it descriptively based on the functionality (e.g., `TextSummarizer` or `DataAnalyzerAgent`).
   - **Include Necessary Files**: Add all relevant code, configuration, and assets for your contribution.
   - **Documentation**: Include a `README.md` file that follows this format:
     - **Overview**: Briefly describe what the contribution does.
     - **Installation**: Specify dependencies and installation steps if necessary.
     - **Usage**: Provide example usage within TinyAGI.
     - **Configuration**: Describe any adjustable settings.
     - **License**: Specify the license (TinyAGI Hub uses MIT by default).
3. **Commit and Push**
   
   - Commit your changes with a descriptive message:
     
     ```bash
     git commit -m "Add TextSummarizer plugin"
     ```
     
   - Push your changes to your fork.
     
4. **Submit a Pull Request**
   
   - Open a pull request to the main TinyAGI Hub repository.
   - Include a brief summary, installation instructions, and any additional setup steps.
   - Respond to any feedback from maintainers to ensure your contribution meets quality and compatibility standards.

---

### 🧩 **Contribution Checklist**

Before submitting your pull request, review this checklist to ensure your contribution meets the Hub’s guidelines:

- [ ] **Documentation**: A clear and descriptive README.md is included.
- [ ] **Code Quality**: Code is well-organized, follows PEP 8 guidelines, and includes comments where necessary.
- [ ] **Tested**: The component has been tested with TinyAGI to ensure it works as expected.
- [ ] **Dependencies**: All required dependencies are listed in the README.md.
- [ ] **No Conflicts**: Your contribution does not conflict with the core functionality of TinyAGI or other Hub contributions.

---

## 📜 **Code of Conduct**

To maintain a healthy and collaborative community, please adhere to these guidelines:

1. **Be Respectful**: Respect others’ contributions and opinions. Our community thrives on collaboration.
2. **Constructive Feedback**: When reviewing contributions, focus on providing constructive and respectful feedback.
3. **Follow Licensing Guidelines**: Ensure your contribution is compatible with the MIT license and that you have the rights to share any third-party code included in your contribution.

---

## 📚 **Resources**

- **[TinyAGI Documentation](https://github.com/SullyGreene/TinyAGI/tree/main/Documents)**: Get an in-depth understanding of TinyAGI's architecture.
- **[TinyAGI Hub Documentation](https://github.com/SullyGreene/TinyAGI-Hub/Documents)**: Learn more about existing Hub contributions.
- **[Core Repository Contribution Guide](https://github.com/SullyGreene/TinyAGI)**: For those interested in contributing directly to TinyAGI’s core repository.
- **[TinyAGI-Hub Streamlit UI](https://github.com/SullyGreene/TinyAGI-Hub-Streamlit)**: Manage and configure TinyAGI components through a user-friendly web interface.

---

**We’re excited to see what you create with TinyAGI!** Whether it’s a new agent, plugin, module, or tool, your contribution helps build a stronger, more capable AGI community. Thank you for helping make TinyAGI Hub a vibrant, collaborative space for AGI innovation. Happy coding! 🚀🤖

---

## 📦 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

