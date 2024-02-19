# LangChain Demo
![LangChain logo](https://images.app.goo.gl/LH3snUwHdFDiuA5y5)

This repository allows using the [LangChain library](https://python.langchain.com/docs/get_started/introduction) for building powerful applications with large language models (LLMs). By following the instructions below you will be able to connect large language models (LLMs) like OpenAI's GPT-3.5 Turbo throug an APIs and run them from command line.
This approach is much more versatile than having to enter prompts manually using web interfaces. 
And you can build on it. LangChain is designed to allow training of LLMs on your own data. It integrates into several platforms such as MS Azure, Amazon Web Services. Google cloud...

### How to install it and run it on your PC

I assume that you have Python and Anaconda installed. The second is not mandatory but recommended.
Optional step: create a conda environment to run this package
Get to your terminal and run:
conda create -n langchain_demo python=3.11.4
conda activate langchain_demo

OK, now you will install the package and dependencies in your environment

git clone <address of this package on github>
pip install -r /path/to/requirements.txt

You are almost done. But you need to connect to OPENAI API with your own key.
[Create your key](https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/)

copy it and store it in a safe place. 
You will have to paste it into the .env file that you find in this repository.
You cannot go wrong, as there is written OPENAI_API_KEY = "paste value here".
Save and close.

Now you are ready to go. You can even run the jupyter notebook in this repo and play with your own prompts.
