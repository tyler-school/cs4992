import sys
import getopt

from skllm.config import SKLLMConfig
from skllm.preprocessing import GPTSummarizer

# WARNING: We have a limited free trial with openAI. Try to limit the use of this function

class Summarizer():

    def __init__(self):

        # Ask Will for the keys
        key_file = open("secret_keys/secretKey", 'r')
        self.SECRET_KEY = key_file.read().rstrip()
        orgkey_file = open("secret_keys/secretOrgKey", 'r')
        self.OPENAI_ORG_ID = orgkey_file.read().rstrip()

    def summarize(self, text, max=15):

        wrap = [text]

        SKLLMConfig.set_openai_key(self.SECRET_KEY)
        SKLLMConfig.set_openai_org(self.OPENAI_ORG_ID)

        gpt_summarizer = GPTSummarizer(openai_model = "gpt-3.5-turbo", max_words = max)
        print("making api call $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        summaries = gpt_summarizer.fit_transform(wrap)
        print(summaries)
    
if __name__ == '__main__':
    args = sys.argv[1:]
    (opts, leftover) = getopt.getopt(args, "f:")

    for (opt, arg) in opts:
        if opt == "-f":
            file = open(arg, 'r')
            text = file.read().strip()
            #print(text)
            break
    else:
        text = leftover[0]

    print(text)
    Summarizer().summarize(text)


