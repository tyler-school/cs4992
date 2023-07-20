from skllm.config import SKLLMConfig
from skllm.preprocessing import GPTSummarizer

class Summarizer():

    def summarize(text):

        key_file = open("newsfeedKey2", 'r')
        SECRET_KEY = key_file.read().rstrip()
        orgkey_file = open("newsfeedOrgKey2", 'r')
        OPENAI_ORG_ID = orgkey_file.read().rstrip()
        SKLLMConfig.set_openai_key(SECRET_KEY)
        SKLLMConfig.set_openai_org(OPENAI_ORG_ID)

        gpt_summarizer = GPTSummarizer(openai_model = "gpt-3.5-turbo", max_words = 15)
        summaries = gpt_summarizer.fit_transform(text)
        print(summaries)


