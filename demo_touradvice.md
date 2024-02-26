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

# Bike tour advice for a given city

```python
from  llm_query import langchain_example
from llm_query import langchain_ridetour
import textwrap
```

```python
weather = langchain_ridetour.GetWeather()
```

```python
city = "Brussels"
#
```

```python
answer = weather.answer(city)
print(answer)
```

## Now I get the advice for a biketour in the selected city


```python
advice = langchain_ridetour.RideAdvice()
langchain_advice = advice.tour_advice(city)

```

```python
s =str(langchain_advice)
s_wrap = textwrap.wrap(s)
s_wrap
```
