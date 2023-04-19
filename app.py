import gradio as gr

from article import extract_article, get_config

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"

DESC = """
        Let Hugging Face models summarize articles for you. 
        Note: Shorter articles generate faster summaries.
        This summarizer uses bart-large-cnn model by Facebook
        """
SAMPLE_URLS = [
    [
        "https://www.technologyreview.com/2021/07/22/1029973/deepmind-alphafold-protein-folding-biology-disease-drugs-proteome/"
    ],
    [
        "https://www.technologyreview.com/2021/07/21/1029860/disability-rights-employment-discrimination-ai-hiring/"
    ],
    [
        "https://www.technologyreview.com/2021/07/09/1028140/ai-voice-actors-sound-human/"
    ],
]

config = get_config(USER_AGENT)


def extract_article_partial(url: str):
    return extract_article(config=config, url=url)


extractor = gr.Interface(extract_article_partial, "text", "text")
summarizer = gr.load("huggingface/facebook/bart-large-cnn")

# mrm8488/camembert2camembert_shared-finetuned-french-summarization
# facebook/bart-large-cnn


iface = gr.Series(
    extractor,
    summarizer,
    inputs=gr.inputs.Textbox(lines=2, label="URL"),
    outputs="text",
    title="News Summarizer",
    theme="huggingface",
    descripion=DESC,
    examples=SAMPLE_URLS,
)

iface.launch()
