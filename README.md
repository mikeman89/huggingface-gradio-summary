# Hugging Face News Summarizer

This is a simple Gradio app which loads a [Hugging Face](https://huggingface.co/) model, [Facebook Bart Large](https://huggingface.co/facebook/bart-large-cnn), to summarize news articles pulled by [Newspaper3k](https://newspaper.readthedocs.io/en/latest/).

# To Run Locally

1) First create a virtual envrionment with the environment.yml file using conda and the below code snippit.

    ```conda env create -f environment.yml```

    this will create a conda environment called "hf-gradio" you could edit that in the yml file.

2) activate your conda environment
    
    ```conda activate hf-gradio```

3) run the app.py file

    ```python app.py```
    
    Gradio will start a local server with an http link you can click similar to the below.

    Running on local URL:  http://127.0.0.1:7860

    Your browser should open up the Gradio app, add a news URL in the left box and click "Submit" for the model to summarize the article.

Have fun!