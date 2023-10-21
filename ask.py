from pinecone_utils import filter_matching_docs
from pinecone_utils import QA_with_your_docs


QUESTION = "What is semantic search?"

# get topks
top_ks = filter_matching_docs(QUESTION, top_chunks = 1)

# get response from the LLM
response = QA_with_your_docs(QUESTION, top_ks)

print("Question: {}".format(QUESTION))
print("Response: {}".format(response))