from youtube_utils import get_youtube_transcript
from pinecone_utils import upload_to_pinecone

#get the script from a given youtube link
yt_links = ["https://www.youtube.com/watch?v=OATCgQtNX2o"]

for link in yt_links:
    #get the link
    script = get_youtube_transcript(link)

    # upload to pinecone
    upload_to_pinecone(script, link, chunk_size = 1000)

print("Uploading process completed...")