---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.1
  kernelspec:
    display_name: langchain
    language: python
    name: python3
---

# Demo Langchain

```python
# import the package we created
from  llm_query import langchain_example
```

```python
# create a class istance
predictor = langchain_example.Pred()
```

```python
# get an answer from ChatGpt
my_prompt = "hi"
predictor.answer(my_prompt)
```
