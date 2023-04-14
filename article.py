from newspaper import Article, Config


def get_config(user_agent: str) -> Config:
    config = Config()
    config.browser_user_agent = user_agent
    config.request_timeout = 10
    return config


def extract_article(config: Config, url: str) -> str:
    article = Article(url, config=config)
    article.download()
    article.parse()
    text = article.text
    return text
