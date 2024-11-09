# 📘 WikipediaTool Integration with TinyAGI

The `WikipediaTool` is a powerful integration for TinyAGI, allowing agents to tap into Wikipedia for search and summary functions. This integration enriches the AI's responses, enabling it to deliver detailed and accurate information from Wikipedia directly to the user. Here’s how to set up and use `WikipediaTool` within TinyAGI.

---

## 🔧 Configuration

To configure `WikipediaTool` with TinyAGI, you'll need to add it to your `agent_config.json` file. This setup ensures that TinyAGI can utilize Wikipedia for both search and summary tasks, enhancing interactions by providing verified and relevant content.

### 1. **Update `agent_config.json`**

Add the `WikipediaTool` configuration to the `tools` section of your `agent_config.json`:

```json
{
  "tools": [
    {
      "name": "WikipediaTool",
      "module": "wikipedia_tool",
      "class": "WikipediaTool",
      "source": "local",
      "config": {
        "language": "en"  // 🌎 Define the language for Wikipedia content (default is 'en')
      }
    }
    // ... other tools
  ],
  // ... other configurations
}
```

### 2. **Define Tasks Using `WikipediaTool`**

Within the `tasks` section of your configuration file, set up tasks that will use `WikipediaTool` to fetch and use Wikipedia content for various plugins, such as `GenerateText` or `GenerateReferences`.

```json
{
  "tasks": [
    {
      "task_id": "fetch_and_rewrite_summary",
      "plugin": "GenerateText",
      "agent": "ollama_agent",
      "tool": "WikipediaTool",
      "input": {
        "prompt": "Artificial Intelligence"
      },
      "output": {
        "save_to_file": false
      },
      "options": {
        "stream": false
      }
    },
    {
      "task_id": "fetch_and_generate_references",
      "plugin": "GenerateReferences",
      "agent": "ollama_agent",
      "tool": "WikipediaTool",
      "input": {
        "query": "Machine Learning"
      },
      "output": {
        "save_to_file": false
      },
      "options": {
        "stream": false
      }
    }
    // ... other tasks
  ]
}
```

---

## ⚙️ Usage

With `WikipediaTool` configured, you can now use it within TinyAGI's task framework to enhance the AI’s capabilities with Wikipedia-sourced information.

### 1. **Running Tasks with `WikipediaTool`**

To execute tasks configured in `agent_config.json`, run the following command:

```bash
python TinyAGI --Config config/agent_config.json
```

### 2. **Using the CLI with `WikipediaTool`**

TinyAGI’s command-line interface (CLI) enables quick interactions involving `WikipediaTool`. Here’s how to use it to generate summaries or references.

#### Generate Text Using `WikipediaTool`

```bash
python -m TinyAGI.services.cli_manager generate --prompt "Artificial Intelligence"
```

#### Generate References Using `WikipediaTool`

```bash
python -m TinyAGI.services.cli_manager generate --prompt "Machine Learning"
```

### 3. **Accessing via API**

Use TinyAGI’s API to interact with `WikipediaTool` through custom tasks.

#### Chat Endpoint Example

```bash
curl -X POST http://localhost:5000/chat \
     -H "Content-Type: application/json" \
     -d '{
           "messages": [{"role": "user", "content": "Tell me about Artificial Intelligence."}],
           "stream": false
         }'
```

#### Generate Text Endpoint Example

```bash
curl -X POST http://localhost:5000/generate \
     -H "Content-Type: application/json" \
     -d '{
           "prompt": "Artificial Intelligence",
           "stream": false
         }'
```

---

With `WikipediaTool` integrated, TinyAGI agents can now access rich, accurate Wikipedia content, making them more informative and versatile for tasks like summarization, content generation, and research-based interactions. This integration enhances the overall utility and responsiveness of TinyAGI in delivering up-to-date knowledge.
